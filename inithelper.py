# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _inithelper

def _swig_setattr(self,class_type,name,value):
    if (name == "this"):
        if isinstance(value, class_type):
            self.__dict__[name] = value.this
            if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
            del value.thisown
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    self.__dict__[name] = value

def _swig_getattr(self,class_type,name):
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


try:
    from weakref import proxy as weakref_proxy
except:
    weakref_proxy = lambda x: x


cpColor = _inithelper.cpColor
cpBlackWhite = _inithelper.cpBlackWhite
cpMonochrome = _inithelper.cpMonochrome
class TProgInit(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TProgInit, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TProgInit, name)
    def __repr__(self):
        return "<C TProgInit instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TProgInit, 'this', _inithelper.new_TProgInit(*args))
        _swig_setattr(self, TProgInit, 'thisown', 1)
    def __del__(self, destroy=_inithelper.delete_TProgInit):
        try:
            if self.thisown: destroy(self)
        except: pass

class TProgInitPtr(TProgInit):
    def __init__(self, this):
        _swig_setattr(self, TProgInit, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TProgInit, 'thisown', 0)
        _swig_setattr(self, TProgInit,self.__class__,TProgInit)
_inithelper.TProgInit_swigregister(TProgInitPtr)
cvar = _inithelper.cvar

class TProgram(TProgInit):
    __swig_setmethods__ = {}
    for _s in [TProgInit]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TProgram, name, value)
    __swig_getmethods__ = {}
    for _s in [TProgInit]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TProgram, name)
    def __repr__(self):
        return "<C TProgram instance at %s>" % (self.this,)
    def __init__(self, *args):
        if self.__class__ == TProgram:
            args = (None,) + args
        else:
            args = (self,) + args
        _swig_setattr(self, TProgram, 'this', _inithelper.new_TProgram(*args))
        _swig_setattr(self, TProgram, 'thisown', 1)
    def __del__(self, destroy=_inithelper.delete_TProgram):
        try:
            if self.thisown: destroy(self)
        except: pass
    def getEvent(*args): return _inithelper.TProgram_getEvent(*args)
    def getPalette(*args): return _inithelper.TProgram_getPalette(*args)
    def handleEvent(*args): return _inithelper.TProgram_handleEvent(*args)
    def idle(*args): return _inithelper.TProgram_idle(*args)
    def initScreen(*args): return _inithelper.TProgram_initScreen(*args)
    def outOfMemory(*args): return _inithelper.TProgram_outOfMemory(*args)
    def putEvent(*args): return _inithelper.TProgram_putEvent(*args)
    def run(*args): return _inithelper.TProgram_run(*args)
    def setScreenMode(*args): return _inithelper.TProgram_setScreenMode(*args)
    def setScreenModeExt(*args): return _inithelper.TProgram_setScreenModeExt(*args)
    def validView(*args): return _inithelper.TProgram_validView(*args)
    def shutDown(*args): return _inithelper.TProgram_shutDown(*args)
    def suspend(*args): return _inithelper.TProgram_suspend(*args)
    def resume(*args): return _inithelper.TProgram_resume(*args)
    def syncScreenBuffer(*args): return _inithelper.TProgram_syncScreenBuffer(*args)
    __swig_getmethods__["initStatusLine"] = lambda x: _inithelper.TProgram_initStatusLine
    if _newclass:initStatusLine = staticmethod(_inithelper.TProgram_initStatusLine)
    __swig_getmethods__["initMenuBar"] = lambda x: _inithelper.TProgram_initMenuBar
    if _newclass:initMenuBar = staticmethod(_inithelper.TProgram_initMenuBar)
    __swig_getmethods__["initDeskTop"] = lambda x: _inithelper.TProgram_initDeskTop
    if _newclass:initDeskTop = staticmethod(_inithelper.TProgram_initDeskTop)
    __swig_getmethods__["resetIdleTime"] = lambda x: _inithelper.TProgram_resetIdleTime
    if _newclass:resetIdleTime = staticmethod(_inithelper.TProgram_resetIdleTime)
    def __disown__(self):
        self.thisown = 0
        _inithelper.disown_TProgram(self)
        return weakref_proxy(self)

class TProgramPtr(TProgram):
    def __init__(self, this):
        _swig_setattr(self, TProgram, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TProgram, 'thisown', 0)
        _swig_setattr(self, TProgram,self.__class__,TProgram)
_inithelper.TProgram_swigregister(TProgramPtr)
apColor = cvar.apColor
apBlackWhite = cvar.apBlackWhite
apMonochrome = cvar.apMonochrome

TProgram_initStatusLine = _inithelper.TProgram_initStatusLine

TProgram_initMenuBar = _inithelper.TProgram_initMenuBar

TProgram_initDeskTop = _inithelper.TProgram_initDeskTop

TProgram_resetIdleTime = _inithelper.TProgram_resetIdleTime

class TApplication(TProgram):
    __swig_setmethods__ = {}
    for _s in [TProgram]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TApplication, name, value)
    __swig_getmethods__ = {}
    for _s in [TProgram]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TApplication, name)
    def __repr__(self):
        return "<C TApplication instance at %s>" % (self.this,)
    def __init__(self, *args):
        if self.__class__ == TApplication:
            args = (None,) + args
        else:
            args = (self,) + args
        _swig_setattr(self, TApplication, 'this', _inithelper.new_TApplication(*args))
        _swig_setattr(self, TApplication, 'thisown', 1)
    def __del__(self, destroy=_inithelper.delete_TApplication):
        try:
            if self.thisown: destroy(self)
        except: pass
    def suspend(*args): return _inithelper.TApplication_suspend(*args)
    def resume(*args): return _inithelper.TApplication_resume(*args)
    def __disown__(self):
        self.thisown = 0
        _inithelper.disown_TApplication(self)
        return weakref_proxy(self)

class TApplicationPtr(TApplication):
    def __init__(self, this):
        _swig_setattr(self, TApplication, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TApplication, 'thisown', 0)
        _swig_setattr(self, TApplication,self.__class__,TApplication)
_inithelper.TApplication_swigregister(TApplicationPtr)

class TMethodHolder(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TMethodHolder, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TMethodHolder, name)
    def __repr__(self):
        return "<C TMethodHolder instance at %s>" % (self.this,)
    def initStatusLine(*args): return _inithelper.TMethodHolder_initStatusLine(*args)
    def initMenuBar(*args): return _inithelper.TMethodHolder_initMenuBar(*args)
    def initDeskTop(*args): return _inithelper.TMethodHolder_initDeskTop(*args)
    def __del__(self, destroy=_inithelper.delete_TMethodHolder):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __init__(self, *args):
        if self.__class__ == TMethodHolder:
            args = (None,) + args
        else:
            args = (self,) + args
        _swig_setattr(self, TMethodHolder, 'this', _inithelper.new_TMethodHolder(*args))
        _swig_setattr(self, TMethodHolder, 'thisown', 1)
    def __disown__(self):
        self.thisown = 0
        _inithelper.disown_TMethodHolder(self)
        return weakref_proxy(self)

class TMethodHolderPtr(TMethodHolder):
    def __init__(self, this):
        _swig_setattr(self, TMethodHolder, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TMethodHolder, 'thisown', 0)
        _swig_setattr(self, TMethodHolder,self.__class__,TMethodHolder)
_inithelper.TMethodHolder_swigregister(TMethodHolderPtr)

class TAppWrapper(TApplication):
    __swig_setmethods__ = {}
    for _s in [TApplication]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TAppWrapper, name, value)
    __swig_getmethods__ = {}
    for _s in [TApplication]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TAppWrapper, name)
    def __repr__(self):
        return "<C TAppWrapper instance at %s>" % (self.this,)
    def __init__(self, *args):
        if self.__class__ == TAppWrapper:
            args = (None,) + args
        else:
            args = (self,) + args
        _swig_setattr(self, TAppWrapper, 'this', _inithelper.new_TAppWrapper(*args))
        _swig_setattr(self, TAppWrapper, 'thisown', 1)
    def __del__(self, destroy=_inithelper.delete_TAppWrapper):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __disown__(self):
        self.thisown = 0
        _inithelper.disown_TAppWrapper(self)
        return weakref_proxy(self)

class TAppWrapperPtr(TAppWrapper):
    def __init__(self, this):
        _swig_setattr(self, TAppWrapper, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TAppWrapper, 'thisown', 0)
        _swig_setattr(self, TAppWrapper,self.__class__,TAppWrapper)
_inithelper.TAppWrapper_swigregister(TAppWrapperPtr)


