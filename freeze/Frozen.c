//-----------------------------------------------------------------------------
// Frozen.c
//   Methods for handling the reading of frozen executables or DLLs.
//-----------------------------------------------------------------------------

#include <Python.h>

static char *gc_Magic = "cx_Freeze-v1";

//-----------------------------------------------------------------------------
// ReadInteger()
//   Read an integer from the file.
//-----------------------------------------------------------------------------
static int ReadInteger(
    FILE *file,				// file to read from
    int *value)				// value to populate
{
    if (fread(value, sizeof(int), 1, file) != 1)
        return -1;
    return 0;
}


//-----------------------------------------------------------------------------
// ReadString()
//   Read a string from the file.
//-----------------------------------------------------------------------------
static char *ReadString(
    FILE *file)				// file to read from
{
    int stringLength;
    char *value;

    if (ReadInteger(file, &stringLength) < 0)
        return NULL;
    value = PyMem_Malloc(stringLength + 1);
    if (!value)
        return NULL;
    if (fread(value, 1, stringLength, file) != stringLength)
        return NULL;
    value[stringLength] = '\0';
    return value;
}


//-----------------------------------------------------------------------------
// LoadFrozenModules()
//   Load the list of frozen modules.
//-----------------------------------------------------------------------------
static int LoadFrozenModules(
    char *fileName,			// file name to read modules from
    int *overridePath)			// override the path?
{
    int fileLength, magicLength, packageHeaderLength, packageLength;
    int dataLength, tocEntries, tocLength, i;
    char *moduleName, *moduleCode, temp[20];
    struct _frozen *modulePtr;
    FILE *file;

    // determine the length of the file
    file = fopen(fileName, "rb");
    if (!file)
        return FatalError("Cannot open archive");
    if (fseek(file, 0, SEEK_END) < 0)
        return FatalError("Cannot seek to end of file");
    fileLength = ftell(file);
    if (fileLength < 0)
        return FatalError("Cannot tell length of file");

    // read and verify the magic value from the file
    magicLength = strlen(gc_Magic);
    if (fseek(file, -magicLength, SEEK_END) < 0)
        return FatalError("Cannot determine magic");
    if (fread(temp, 1, magicLength, file) != magicLength)
        return FatalError("Cannot read magic");
    if (strncmp(gc_Magic, temp, magicLength) != 0)
        return FatalError("Invalid magic");

    // get the package header
    packageHeaderLength = magicLength + sizeof(int) * 4;
    if (fseek(file, -packageHeaderLength, SEEK_END) < 0)
        return FatalError("Cannot seek to beginning of package header");
    if (ReadInteger(file, &dataLength) < 0)
        return FatalError("Cannot read package data length");
    if (ReadInteger(file, &tocEntries) < 0)
        return FatalError("Cannot read package TOC entries");
    if (ReadInteger(file, &tocLength) < 0)
        return FatalError("Cannot read package TOC length");
    if (ReadInteger(file, overridePath) < 0)
        return FatalError("Cannot read override path flag");

    // create the frozen modules list
    modulePtr = malloc(sizeof(struct _frozen) * (tocEntries + 1));
    if (!modulePtr)
        return FatalError("Out of memory creating frozen modules list");

    // get the TOC
    packageLength = packageHeaderLength + dataLength + tocLength;
    if (fseek(file, -packageLength, SEEK_END) < 0)
        return FatalError("Cannot seek to beginning of package");
    for (i = 0; i < tocEntries; i++) {
        moduleName = ReadString(file);
        if (!moduleName)
            return FatalError("Cannot read module name");
        modulePtr[i].name = moduleName;
        modulePtr[i].code = NULL;
        if (ReadInteger(file, &modulePtr[i].size) < 0)
            return FatalError("Cannot read module data size");
    }

    // add the trailing entry
    modulePtr[tocEntries].name = NULL;
    modulePtr[tocEntries].code = NULL;
    modulePtr[tocEntries].size = 0;

    // read the module code
    moduleCode = malloc(dataLength);
    if (!moduleCode)
        return FatalError("Out of memory loading module code");
    if (fread(moduleCode, 1, dataLength, file) != dataLength)
        return FatalError("Cannot read module code");
    for (i = 0; i < tocEntries; i++) {
        if (modulePtr[i].size != 0) {
            modulePtr[i].code = moduleCode;
            moduleCode += abs(modulePtr[i].size);
        }
    }

    // set the list of frozen modules
    PyImport_FrozenModules = modulePtr;

    // close the file since it is no longer needed
    fclose(file);

    return 0;
}


//-----------------------------------------------------------------------------
// OverridePath()
//   Override the path for the binary.
//-----------------------------------------------------------------------------
static int OverridePath(
    char *fileName)			// file name
{
    PyObject *pathList, *path;
    char *ptr;

    for (ptr = fileName + strlen(fileName); ptr > fileName; ptr--) {
        if (*ptr == '/' || *ptr == '\\')
            break;
    }
    path = PyString_FromStringAndSize(fileName, ptr - fileName);
    if (!path)
         return FatalError("Cannot allocate path string variable");
    pathList = PyList_New(1);
    if (!pathList)
         return FatalError("Cannot allocate path list variable");
    PyList_SET_ITEM(pathList, 0, path);
    if (PySys_SetObject("path", pathList) != 0)
        return FatalError("Cannot set sys.path");
    Py_DECREF(pathList);

    return 0;
}


//-----------------------------------------------------------------------------
// InitializePython()
//   Main routine for frozen programs.
//-----------------------------------------------------------------------------
static int InitializePython(
    char *fileName,			// file name (optional)
    int argc,				// argument count
    char **argv)			// argument values
{
    int overridePath;
    PyObject *temp;

    // program is a frozen Python executable
    Py_FrozenFlag = 1;

    // don't attempt to load the site module
    Py_NoSiteFlag = 1;

    // get file name if one not specified
    if (!fileName && argc > 0) {
        Py_SetProgramName(argv[0]);
        fileName = Py_GetProgramFullPath();
    }

    // load frozen modules; before overriding sys.path in order to get access
    // to the "os" module which is always frozen
    if (LoadFrozenModules(fileName, &overridePath) < 0)
        return -1;

    // initialize Python
    Py_Initialize();
    if (argc > 0)
        PySys_SetArgv(argc, argv);

    // override sys.path to only include the directory in which the binary
    // is found; this eliminates potential distribution headaches where the
    // binary works on systems that have Python installed but not on systems
    // where Python is not installed
    if (overridePath) {
        if (OverridePath(fileName) < 0)
            return -1;

    // otherwise, proceed to import the site module as would normally take
    // place; the Py_NoSiteFlag must be set because it is unknown whether or
    // not this ought to take place and a nasty warning is printed if the
    // site module does not exist
    } else {
        temp = PyImport_ImportModule("site");
        if (!temp)
            PyErr_Clear();
    }

    // now override sys.executable which will be incorrect in the case where
    // a dll is actually being used instead of an executable
    temp = PyString_FromString(fileName);
    if (!temp)
        return FatalError("cannot allocate executable variable");
    if (PySys_SetObject("executable", temp) != 0)
        return FatalError("Cannot set sys.executable");
    Py_DECREF(temp);

    return 0;
}

