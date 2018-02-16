"""Make the frozen base executables."""

import cx_OptionParser
import distutils.sysconfig
import os
import sys

# parse command line
parser = cx_OptionParser.OptionParser("MakeFrozenBases")
options = parser.Parse()

# define function for building a base executable
def BuildBase(name, linkerFlags = "", sharedLib = False):
    vars = distutils.sysconfig.get_config_vars()
    sourceName = name + ".c"
    objectName = name + ".o"
    targetName = name + "Base"
    if sharedLib:
        if sys.platform == "win32":
            targetName += ".dll"
        else:
            targetName += vars["SO"]
        linkerFlags = "-shared %s" % linkerFlags
    else:
        targetName += vars["EXE"]
    compilerFlags = "-c -I. -I%s" % distutils.sysconfig.get_python_inc()
    linkerFlags += " -s"
    if sys.platform == "win32":
        import win32api
        linkerFlags += " " + win32api.GetModuleFileName(sys.dllhandle)
    else:
        if sys.platform == "linux2":
            linkerFlags += " -rdynamic"
        elif sys.platform == "hp-ux11":
            linkerFlags += " -Wl,-E -Wl,+s"
            linkerFlags += " -lcl"
        linkerFlags += " -L%s" % vars["LIBPL"]
        linkerFlags += " -lpython%d.%d -lz" % sys.version_info[:2]
        linkerFlags += " %s %s" % (vars["LIBS"], vars["LIBM"])
    command = "gcc %s -o %s %s" % (compilerFlags, objectName, sourceName)
    print command
    if os.system(command) != 0:
        raise "Failed to compile %s" % sourceName
    command = "gcc -o %s %s %s" % (targetName, objectName, linkerFlags)
    print command
    if os.system(command) != 0:
        raise "Failed to link %s" % sourceName
    os.unlink(objectName)

BuildBase("Console")
if sys.platform == "win32":
    BuildBase("Win32GUI", "-mwindows")
    baseName = "Win32ServerMessages"
    resourceTarget = baseName + ".o"
    command = "windres -i %s -o %s" % (baseName + ".res", resourceTarget)
    if os.system(command) != 0:
        raise "Failed to build resource %s" % resourceTarget
    BuildBase("Win32Service", resourceTarget)
    linkerFlags = "-Wl,--enable-stdcall-fixup %s %s" % \
            (resourceTarget, "Win32COM.def")
    BuildBase("Win32COM", resourceTarget, sharedLib = True)
    os.unlink(resourceTarget)
else:
    BuildBase("ConsoleSetLibPath")

