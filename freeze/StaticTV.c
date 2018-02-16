//-----------------------------------------------------------------------------
// StaticTV.c
//   Main routine for frozen programs linked with TVision.
//-----------------------------------------------------------------------------

#include <Python.h>

//-----------------------------------------------------------------------------
// FatalError()
//   Handle a fatal error.
//-----------------------------------------------------------------------------
static int FatalError(
    char *message)			// message to display
{
    Py_FatalError(message);
    return -1;
}

#include <Frozen.c>

//-----------------------------------------------------------------------------
// main()
//   Main routine for frozen programs.
//-----------------------------------------------------------------------------
void init_tv(void);

int main(int argc, char **argv)
{
    int importStatus, returnCode;

    // initialize Python
    InitializePython(NULL, argc, argv);

    // initialize _tv module
    init_tv();

    // run the program
    returnCode = 0;
    importStatus = PyImport_ImportFrozenModule("__main__");
    if (importStatus == 0) {
        FatalError("__main__ not frozen");
        returnCode = 1;
    }
    if (importStatus < 0) {
        PyErr_Print();
        returnCode = 1;
    }

    // terminate Python
    Py_Finalize();
    return returnCode;
}

