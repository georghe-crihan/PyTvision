"""Make the frozen base executables."""

import cx_OptionParser
import distutils.sysconfig
import os
import sys

# parse command line
parser = cx_OptionParser.OptionParser("MakeFrozenBases")
options = parser.Parse()

def runcmd(command):
    print command
    return os.system(command)

# define function for building a base executable
def BuildBase(name, linkerFlags = "", sharedLib = False):
    vars = distutils.sysconfig.get_config_vars()
    sourceName = name + ".c"
    objectName = name + ".o"
    targetName = name + "Base"
    targetName += vars["EXE"]
    compilerFlags = "-c -I. -I%s" % distutils.sysconfig.get_python_inc()
    linkerFlags += " -s"
    linkerFlags += " -L%s" % vars["LIBPL"]
    linkerFlags += " -L ../tvision-py/makes"
    linkerFlags += " ../all_wrap.o ../inithelper.o"
    linkerFlags += " " + objectName
    linkerFlags += " -lpython%d.%d" % sys.version_info[:2]
    linkerFlags += " -lrhtv -lstdc++ -lz"
    linkerFlags += " %s %s" % (vars["LIBS"], vars["LIBM"])
    command = "gcc %s -o %s %s" % (compilerFlags, objectName, sourceName)
    if runcmd(command) != 0:
        raise "Failed to compile %s" % sourceName
    command = "gcc -o %s %s" % (targetName, linkerFlags)
    if runcmd(command) != 0:
        raise "Failed to link %s" % sourceName
    os.unlink(objectName)

BuildBase("StaticTV")

