from distutils.core import setup
from distutils.extension import Extension
from distutils import sysconfig
from distutils.command.build_ext import build_ext

import os, sys


#save_init_posix = sysconfig._init_posix

#def my_init_posix():
#    print 'my_init_posix: changing gcc to g++'
#    save_init_posix()
#    g = sysconfig._config_vars
#    g['CC'] = 'gxx -fno-rtti'
#    g['LDSHARED'] = 'gxx -shared -fno-rtti'

#sysconfig._init_posix = my_init_posix

#PREFIX = os.environ.get("DJDIR") or os.environ["HOME"]
CWD = os.getcwd()

class build_pytv_ext(build_ext):
    def finalize_options(self):
        self.run_command('config')

#        # force use of C++ compiler (helps on some platforms)
#        import os
#        cc = os.environ.get('CXX', sysconfig.get_config_var('CXX'))
#        if not cc:
#            cc = sysconfig.get_config_var('CCC') # Python 1.5.2
#        if cc:
#            os.environ['CC'] = cc

        build_ext.finalize_options(self)


    def build_extension(self, ext):

        assert(os.system("swig -c++ -python -DNO_STREAM all.i") == 0)
                
        # patch C++ file produced by SWIG
        fd = open("all_wrap.cxx", "r+")
        text = fd.read()
        text = text.replace("TAppWrapper(),",
                            "TAppWrapper(arg0),TProgInit(&TAppWrapper::_sInitStatusLine,&TAppWrapper::_sInitMenuBar,&TAppWrapper::_sInitDeskTop),")
        fd.seek(0)
        fd.truncate()
        fd.write(text)
        fd.close()

        build_ext.build_extension(self, ext)

setup(
  name = 'PyTVision',
  include_dirs=[CWD + "/tvision-py/include"],
  cmdclass = {'build_ext': build_pytv_ext},
  ext_modules = [
    Extension("_tv",       ["all_wrap.cxx", "inithelper.cpp"],
#              extra_objects=[CWD + "/tvision-py/makes/librhtv.a"],
              library_dirs=[CWD + "/tvision-py/makes"],
              libraries=["rhtv", "stdc++"],
              define_macros=[("NO_STREAM", 1)],
              ),
    ],
)
