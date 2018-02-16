"""Freeze a Python script and all of its referenced modules to a base
executable which can then be distributed without requiring a Python
installation."""

import cx_Freezer
import cx_OptionParser
import cx_ShellUtils
import os
import sys

# parse command line
parser = cx_OptionParser.OptionParser("FreezePython")
parser.AddOption("--base-binary", required = True, metavar = "NAME",
        default = os.environ.get("FREEZE_PYTHON_BASE"),
        help = "Base binary instead of $FREEZE_PYTHON_BASE")
parser.AddOption("--install-dir", required = True, metavar = "DIR",
        default = os.environ.get("FREEZE_PYTHON_INSTALL_DIR"),
        help = "Location to install binary instead of "
               "$FREEZE_PYTHON_INSTALL_DIR.")
parser.AddOption("--target-name", metavar = "NAME",
        help = "Name of binary to create instead of script.extension")
parser.AddOption("--shared-library", action = "store_true",
        help = "do not generate __main__ for the name of the module")
parser.AddOption("--keep-path", action = "store_false",
        dest = "overridePath", default = True,
        help = "do not override the path in the frozen executable")
parser.AddOption("--include-modules", action = "append", metavar = "LIST",
        help = "name(s) of module(s) to include in the frozen binary")
parser.AddOption("--exclude-modules", action = "append", metavar = "LIST",
        help = "name(s) of module(s) to exclude from the frozen binary")
parser.AddOption("--ext-list-file", metavar = "FILE",
        help = "name of file in which to place list of extensions")
parser.AddArgument("script", required = True,
        help = "the script to freeze")
options = parser.Parse()

# force the directory in which the script is found to be included in the path
dir, name = os.path.split(options.script)
sys.path.insert(0, dir)

# determine the name of the main module and the name of the binary to create
name, extension = os.path.splitext(os.path.basename(options.script))
baseBinaryName, extension = os.path.splitext(options.baseBinary)
if options.targetName:
    baseBinaryName = options.targetName
else:
    baseBinaryName = name + extension
targetName = os.path.join(options.installDir, baseBinaryName)

# determine the list of modules to exclude
excludes = []
if options.excludeModules:
    excludes = [s for v in options.excludeModules for s in v.split(",")]

# locate all of the modules
finder = cx_Freezer.ModuleFinder(excludes = excludes)
if options.sharedLibrary:
    finder.load_module(options.script)
else:
    finder.run_script(options.script)

# add additional modules that are requested
if options.includeModules:
    moduleNames = [s for v in options.includeModules for s in v.split(",")]
    for name in moduleNames:
        finder.import_hook(name)

# perform the work of freezing the found modules to a copy of the base binary
if not os.path.exists(options.installDir):
    os.makedirs(options.installDir)
cx_ShellUtils.Copy(options.baseBinary, targetName)
filesCopied = cx_Freezer.Freeze(targetName, finder, options.overridePath)
if options.extListFile:
    file(options.extListFile, "w").write("\n".join(filesCopied))
print "Frozen binary %s created." % targetName
print "Done."

