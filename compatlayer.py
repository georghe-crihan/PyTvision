# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _compatlayer

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


CLY_SizedTypesDefined = _compatlayer.CLY_SizedTypesDefined
streamableInit = _compatlayer.streamableInit
class TObject(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TObject, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TObject, name)
    def __repr__(self):
        return "<C TObject instance at %s>" % (self.this,)
    def __del__(self, destroy=_compatlayer.delete_TObject):
        try:
            if self.thisown: destroy(self)
        except: pass
    __swig_getmethods__["CLY_destroy"] = lambda x: _compatlayer.TObject_CLY_destroy
    if _newclass:CLY_destroy = staticmethod(_compatlayer.TObject_CLY_destroy)
    def shutDown(*args): return _compatlayer.TObject_shutDown(*args)
    def __init__(self, *args):
        _swig_setattr(self, TObject, 'this', _compatlayer.new_TObject(*args))
        _swig_setattr(self, TObject, 'thisown', 1)

class TObjectPtr(TObject):
    def __init__(self, this):
        _swig_setattr(self, TObject, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TObject, 'thisown', 0)
        _swig_setattr(self, TObject,self.__class__,TObject)
_compatlayer.TObject_swigregister(TObjectPtr)
cvar = _compatlayer.cvar
EOS = cvar.EOS
ccNotFound = cvar.ccNotFound
evMouseDown = cvar.evMouseDown
evMouseUp = cvar.evMouseUp
evMouseMove = cvar.evMouseMove
evMouseAuto = cvar.evMouseAuto
evKeyDown = cvar.evKeyDown
evCommand = cvar.evCommand
evBroadcast = cvar.evBroadcast
evNothing = cvar.evNothing
evMouse = cvar.evMouse
evKeyboard = cvar.evKeyboard
evMessage = cvar.evMessage
mbLeftButton = cvar.mbLeftButton
mbMiddleButton = cvar.mbMiddleButton
mbRightButton = cvar.mbRightButton
mbButton4 = cvar.mbButton4
mbButton5 = cvar.mbButton5

TObject_CLY_destroy = _compatlayer.TObject_CLY_destroy

class MouseEventType(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MouseEventType, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MouseEventType, name)
    def __repr__(self):
        return "<C MouseEventType instance at %s>" % (self.this,)
    __swig_setmethods__["buttons"] = _compatlayer.MouseEventType_buttons_set
    __swig_getmethods__["buttons"] = _compatlayer.MouseEventType_buttons_get
    if _newclass:buttons = property(_compatlayer.MouseEventType_buttons_get, _compatlayer.MouseEventType_buttons_set)
    __swig_setmethods__["doubleClick"] = _compatlayer.MouseEventType_doubleClick_set
    __swig_getmethods__["doubleClick"] = _compatlayer.MouseEventType_doubleClick_get
    if _newclass:doubleClick = property(_compatlayer.MouseEventType_doubleClick_get, _compatlayer.MouseEventType_doubleClick_set)
    __swig_setmethods__["where"] = _compatlayer.MouseEventType_where_set
    __swig_getmethods__["where"] = _compatlayer.MouseEventType_where_get
    if _newclass:where = property(_compatlayer.MouseEventType_where_get, _compatlayer.MouseEventType_where_set)
    def __init__(self, *args):
        _swig_setattr(self, MouseEventType, 'this', _compatlayer.new_MouseEventType(*args))
        _swig_setattr(self, MouseEventType, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_MouseEventType):
        try:
            if self.thisown: destroy(self)
        except: pass

class MouseEventTypePtr(MouseEventType):
    def __init__(self, this):
        _swig_setattr(self, MouseEventType, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, MouseEventType, 'thisown', 0)
        _swig_setattr(self, MouseEventType,self.__class__,MouseEventType)
_compatlayer.MouseEventType_swigregister(MouseEventTypePtr)

class THWMouse(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, THWMouse, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, THWMouse, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<C THWMouse instance at %s>" % (self.this,)
    __swig_getmethods__["forceEvent"] = lambda x: _compatlayer.THWMouse_forceEvent
    if _newclass:forceEvent = staticmethod(_compatlayer.THWMouse_forceEvent)

class THWMousePtr(THWMouse):
    def __init__(self, this):
        _swig_setattr(self, THWMouse, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, THWMouse, 'thisown', 0)
        _swig_setattr(self, THWMouse,self.__class__,THWMouse)
_compatlayer.THWMouse_swigregister(THWMousePtr)

THWMouse_forceEvent = _compatlayer.THWMouse_forceEvent

class TMouse(THWMouse):
    __swig_setmethods__ = {}
    for _s in [THWMouse]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TMouse, name, value)
    __swig_getmethods__ = {}
    for _s in [THWMouse]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TMouse, name)
    def __repr__(self):
        return "<C TMouse instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TMouse, 'this', _compatlayer.new_TMouse(*args))
        _swig_setattr(self, TMouse, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TMouse):
        try:
            if self.thisown: destroy(self)
        except: pass
    __swig_getmethods__["show"] = lambda x: _compatlayer.TMouse_show
    if _newclass:show = staticmethod(_compatlayer.TMouse_show)
    __swig_getmethods__["hide"] = lambda x: _compatlayer.TMouse_hide
    if _newclass:hide = staticmethod(_compatlayer.TMouse_hide)
    __swig_getmethods__["suspend"] = lambda x: _compatlayer.TMouse_suspend
    if _newclass:suspend = staticmethod(_compatlayer.TMouse_suspend)
    __swig_getmethods__["resume"] = lambda x: _compatlayer.TMouse_resume
    if _newclass:resume = staticmethod(_compatlayer.TMouse_resume)
    __swig_getmethods__["setRange"] = lambda x: _compatlayer.TMouse_setRange
    if _newclass:setRange = staticmethod(_compatlayer.TMouse_setRange)
    __swig_getmethods__["getEvent"] = lambda x: _compatlayer.TMouse_getEvent
    if _newclass:getEvent = staticmethod(_compatlayer.TMouse_getEvent)
    __swig_getmethods__["present"] = lambda x: _compatlayer.TMouse_present
    if _newclass:present = staticmethod(_compatlayer.TMouse_present)
    __swig_getmethods__["resetDrawCounter"] = lambda x: _compatlayer.TMouse_resetDrawCounter
    if _newclass:resetDrawCounter = staticmethod(_compatlayer.TMouse_resetDrawCounter)
    __swig_getmethods__["getDrawCounter"] = lambda x: _compatlayer.TMouse_getDrawCounter
    if _newclass:getDrawCounter = staticmethod(_compatlayer.TMouse_getDrawCounter)

class TMousePtr(TMouse):
    def __init__(self, this):
        _swig_setattr(self, TMouse, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TMouse, 'thisown', 0)
        _swig_setattr(self, TMouse,self.__class__,TMouse)
_compatlayer.TMouse_swigregister(TMousePtr)

TMouse_show = _compatlayer.TMouse_show

TMouse_hide = _compatlayer.TMouse_hide

TMouse_suspend = _compatlayer.TMouse_suspend

TMouse_resume = _compatlayer.TMouse_resume

TMouse_setRange = _compatlayer.TMouse_setRange

TMouse_getEvent = _compatlayer.TMouse_getEvent

TMouse_present = _compatlayer.TMouse_present

TMouse_resetDrawCounter = _compatlayer.TMouse_resetDrawCounter

TMouse_getDrawCounter = _compatlayer.TMouse_getDrawCounter

class CharScanType(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CharScanType, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CharScanType, name)
    def __repr__(self):
        return "<C CharScanType instance at %s>" % (self.this,)
    __swig_setmethods__["charCode"] = _compatlayer.CharScanType_charCode_set
    __swig_getmethods__["charCode"] = _compatlayer.CharScanType_charCode_get
    if _newclass:charCode = property(_compatlayer.CharScanType_charCode_get, _compatlayer.CharScanType_charCode_set)
    __swig_setmethods__["scanCode"] = _compatlayer.CharScanType_scanCode_set
    __swig_getmethods__["scanCode"] = _compatlayer.CharScanType_scanCode_get
    if _newclass:scanCode = property(_compatlayer.CharScanType_scanCode_get, _compatlayer.CharScanType_scanCode_set)
    def __init__(self, *args):
        _swig_setattr(self, CharScanType, 'this', _compatlayer.new_CharScanType(*args))
        _swig_setattr(self, CharScanType, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_CharScanType):
        try:
            if self.thisown: destroy(self)
        except: pass

class CharScanTypePtr(CharScanType):
    def __init__(self, this):
        _swig_setattr(self, CharScanType, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, CharScanType, 'thisown', 0)
        _swig_setattr(self, CharScanType,self.__class__,CharScanType)
_compatlayer.CharScanType_swigregister(CharScanTypePtr)

class KeyDownEvent(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, KeyDownEvent, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, KeyDownEvent, name)
    def __repr__(self):
        return "<C KeyDownEvent instance at %s>" % (self.this,)
    __swig_setmethods__["charScan"] = _compatlayer.KeyDownEvent_charScan_set
    __swig_getmethods__["charScan"] = _compatlayer.KeyDownEvent_charScan_get
    if _newclass:charScan = property(_compatlayer.KeyDownEvent_charScan_get, _compatlayer.KeyDownEvent_charScan_set)
    __swig_setmethods__["keyCode"] = _compatlayer.KeyDownEvent_keyCode_set
    __swig_getmethods__["keyCode"] = _compatlayer.KeyDownEvent_keyCode_get
    if _newclass:keyCode = property(_compatlayer.KeyDownEvent_keyCode_get, _compatlayer.KeyDownEvent_keyCode_set)
    __swig_setmethods__["shiftState"] = _compatlayer.KeyDownEvent_shiftState_set
    __swig_getmethods__["shiftState"] = _compatlayer.KeyDownEvent_shiftState_get
    if _newclass:shiftState = property(_compatlayer.KeyDownEvent_shiftState_get, _compatlayer.KeyDownEvent_shiftState_set)
    __swig_setmethods__["raw_scanCode"] = _compatlayer.KeyDownEvent_raw_scanCode_set
    __swig_getmethods__["raw_scanCode"] = _compatlayer.KeyDownEvent_raw_scanCode_get
    if _newclass:raw_scanCode = property(_compatlayer.KeyDownEvent_raw_scanCode_get, _compatlayer.KeyDownEvent_raw_scanCode_set)
    __swig_setmethods__["charCode"] = _compatlayer.KeyDownEvent_charCode_set
    __swig_getmethods__["charCode"] = _compatlayer.KeyDownEvent_charCode_get
    if _newclass:charCode = property(_compatlayer.KeyDownEvent_charCode_get, _compatlayer.KeyDownEvent_charCode_set)
    def __init__(self, *args):
        _swig_setattr(self, KeyDownEvent, 'this', _compatlayer.new_KeyDownEvent(*args))
        _swig_setattr(self, KeyDownEvent, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_KeyDownEvent):
        try:
            if self.thisown: destroy(self)
        except: pass

class KeyDownEventPtr(KeyDownEvent):
    def __init__(self, this):
        _swig_setattr(self, KeyDownEvent, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, KeyDownEvent, 'thisown', 0)
        _swig_setattr(self, KeyDownEvent,self.__class__,KeyDownEvent)
_compatlayer.KeyDownEvent_swigregister(KeyDownEventPtr)

class MessageEvent(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MessageEvent, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MessageEvent, name)
    def __repr__(self):
        return "<C MessageEvent instance at %s>" % (self.this,)
    __swig_setmethods__["command"] = _compatlayer.MessageEvent_command_set
    __swig_getmethods__["command"] = _compatlayer.MessageEvent_command_get
    if _newclass:command = property(_compatlayer.MessageEvent_command_get, _compatlayer.MessageEvent_command_set)
    __swig_setmethods__["infoPtr"] = _compatlayer.MessageEvent_infoPtr_set
    __swig_getmethods__["infoPtr"] = _compatlayer.MessageEvent_infoPtr_get
    if _newclass:infoPtr = property(_compatlayer.MessageEvent_infoPtr_get, _compatlayer.MessageEvent_infoPtr_set)
    __swig_setmethods__["infoLong"] = _compatlayer.MessageEvent_infoLong_set
    __swig_getmethods__["infoLong"] = _compatlayer.MessageEvent_infoLong_get
    if _newclass:infoLong = property(_compatlayer.MessageEvent_infoLong_get, _compatlayer.MessageEvent_infoLong_set)
    __swig_setmethods__["infoWord"] = _compatlayer.MessageEvent_infoWord_set
    __swig_getmethods__["infoWord"] = _compatlayer.MessageEvent_infoWord_get
    if _newclass:infoWord = property(_compatlayer.MessageEvent_infoWord_get, _compatlayer.MessageEvent_infoWord_set)
    __swig_setmethods__["infoInt"] = _compatlayer.MessageEvent_infoInt_set
    __swig_getmethods__["infoInt"] = _compatlayer.MessageEvent_infoInt_get
    if _newclass:infoInt = property(_compatlayer.MessageEvent_infoInt_get, _compatlayer.MessageEvent_infoInt_set)
    __swig_setmethods__["infoByte"] = _compatlayer.MessageEvent_infoByte_set
    __swig_getmethods__["infoByte"] = _compatlayer.MessageEvent_infoByte_get
    if _newclass:infoByte = property(_compatlayer.MessageEvent_infoByte_get, _compatlayer.MessageEvent_infoByte_set)
    __swig_setmethods__["infoChar"] = _compatlayer.MessageEvent_infoChar_set
    __swig_getmethods__["infoChar"] = _compatlayer.MessageEvent_infoChar_get
    if _newclass:infoChar = property(_compatlayer.MessageEvent_infoChar_get, _compatlayer.MessageEvent_infoChar_set)
    def __init__(self, *args):
        _swig_setattr(self, MessageEvent, 'this', _compatlayer.new_MessageEvent(*args))
        _swig_setattr(self, MessageEvent, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_MessageEvent):
        try:
            if self.thisown: destroy(self)
        except: pass

class MessageEventPtr(MessageEvent):
    def __init__(self, this):
        _swig_setattr(self, MessageEvent, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, MessageEvent, 'thisown', 0)
        _swig_setattr(self, MessageEvent,self.__class__,MessageEvent)
_compatlayer.MessageEvent_swigregister(MessageEventPtr)

class TEvent(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TEvent, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TEvent, name)
    def __repr__(self):
        return "<C TEvent instance at %s>" % (self.this,)
    __swig_setmethods__["what"] = _compatlayer.TEvent_what_set
    __swig_getmethods__["what"] = _compatlayer.TEvent_what_get
    if _newclass:what = property(_compatlayer.TEvent_what_get, _compatlayer.TEvent_what_set)
    __swig_setmethods__["mouse"] = _compatlayer.TEvent_mouse_set
    __swig_getmethods__["mouse"] = _compatlayer.TEvent_mouse_get
    if _newclass:mouse = property(_compatlayer.TEvent_mouse_get, _compatlayer.TEvent_mouse_set)
    __swig_setmethods__["keyDown"] = _compatlayer.TEvent_keyDown_set
    __swig_getmethods__["keyDown"] = _compatlayer.TEvent_keyDown_get
    if _newclass:keyDown = property(_compatlayer.TEvent_keyDown_get, _compatlayer.TEvent_keyDown_set)
    __swig_setmethods__["message"] = _compatlayer.TEvent_message_set
    __swig_getmethods__["message"] = _compatlayer.TEvent_message_get
    if _newclass:message = property(_compatlayer.TEvent_message_get, _compatlayer.TEvent_message_set)
    def __init__(self, *args):
        _swig_setattr(self, TEvent, 'this', _compatlayer.new_TEvent(*args))
        _swig_setattr(self, TEvent, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TEvent):
        try:
            if self.thisown: destroy(self)
        except: pass

class TEventPtr(TEvent):
    def __init__(self, this):
        _swig_setattr(self, TEvent, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TEvent, 'thisown', 0)
        _swig_setattr(self, TEvent,self.__class__,TEvent)
_compatlayer.TEvent_swigregister(TEventPtr)

class TStreamable(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TStreamable, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TStreamable, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<C TStreamable instance at %s>" % (self.this,)
    def __del__(self, destroy=_compatlayer.delete_TStreamable):
        try:
            if self.thisown: destroy(self)
        except: pass

class TStreamablePtr(TStreamable):
    def __init__(self, this):
        _swig_setattr(self, TStreamable, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TStreamable, 'thisown', 0)
        _swig_setattr(self, TStreamable,self.__class__,TStreamable)
_compatlayer.TStreamable_swigregister(TStreamablePtr)

class TNSCollection(TObject):
    __swig_setmethods__ = {}
    for _s in [TObject]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TNSCollection, name, value)
    __swig_getmethods__ = {}
    for _s in [TObject]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TNSCollection, name)
    def __repr__(self):
        return "<C TNSCollection instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TNSCollection, 'this', _compatlayer.new_TNSCollection(*args))
        _swig_setattr(self, TNSCollection, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TNSCollection):
        try:
            if self.thisown: destroy(self)
        except: pass
    def shutDown(*args): return _compatlayer.TNSCollection_shutDown(*args)
    def at(*args): return _compatlayer.TNSCollection_at(*args)
    def indexOf(*args): return _compatlayer.TNSCollection_indexOf(*args)
    def atFree(*args): return _compatlayer.TNSCollection_atFree(*args)
    def atRemove(*args): return _compatlayer.TNSCollection_atRemove(*args)
    def remove(*args): return _compatlayer.TNSCollection_remove(*args)
    def removeAll(*args): return _compatlayer.TNSCollection_removeAll(*args)
    def free(*args): return _compatlayer.TNSCollection_free(*args)
    def freeAll(*args): return _compatlayer.TNSCollection_freeAll(*args)
    def atInsert(*args): return _compatlayer.TNSCollection_atInsert(*args)
    def atPut(*args): return _compatlayer.TNSCollection_atPut(*args)
    def atReplace(*args): return _compatlayer.TNSCollection_atReplace(*args)
    def insert(*args): return _compatlayer.TNSCollection_insert(*args)
    def insert(self, p):
        p.thisown = 0
        return _tv.TNSCollection_insert(self, p)

    def error(*args): return _compatlayer.TNSCollection_error(*args)
    def firstThat(*args): return _compatlayer.TNSCollection_firstThat(*args)
    def lastThat(*args): return _compatlayer.TNSCollection_lastThat(*args)
    def forEach(*args): return _compatlayer.TNSCollection_forEach(*args)
    def pack(*args): return _compatlayer.TNSCollection_pack(*args)
    def setLimit(*args): return _compatlayer.TNSCollection_setLimit(*args)
    def getCount(*args): return _compatlayer.TNSCollection_getCount(*args)
    def setOwnerShip(*args): return _compatlayer.TNSCollection_setOwnerShip(*args)

class TNSCollectionPtr(TNSCollection):
    def __init__(self, this):
        _swig_setattr(self, TNSCollection, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TNSCollection, 'thisown', 0)
        _swig_setattr(self, TNSCollection,self.__class__,TNSCollection)
_compatlayer.TNSCollection_swigregister(TNSCollectionPtr)

class TNSSortedCollection(TNSCollection):
    __swig_setmethods__ = {}
    for _s in [TNSCollection]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TNSSortedCollection, name, value)
    __swig_getmethods__ = {}
    for _s in [TNSCollection]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TNSSortedCollection, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<C TNSSortedCollection instance at %s>" % (self.this,)
    def search(*args): return _compatlayer.TNSSortedCollection_search(*args)
    def indexOf(*args): return _compatlayer.TNSSortedCollection_indexOf(*args)
    def insert(*args): return _compatlayer.TNSSortedCollection_insert(*args)
    __swig_setmethods__["duplicates"] = _compatlayer.TNSSortedCollection_duplicates_set
    __swig_getmethods__["duplicates"] = _compatlayer.TNSSortedCollection_duplicates_get
    if _newclass:duplicates = property(_compatlayer.TNSSortedCollection_duplicates_get, _compatlayer.TNSSortedCollection_duplicates_set)
    def keyOf(*args): return _compatlayer.TNSSortedCollection_keyOf(*args)
    def __del__(self, destroy=_compatlayer.delete_TNSSortedCollection):
        try:
            if self.thisown: destroy(self)
        except: pass

class TNSSortedCollectionPtr(TNSSortedCollection):
    def __init__(self, this):
        _swig_setattr(self, TNSSortedCollection, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TNSSortedCollection, 'thisown', 0)
        _swig_setattr(self, TNSSortedCollection,self.__class__,TNSSortedCollection)
_compatlayer.TNSSortedCollection_swigregister(TNSSortedCollectionPtr)

class TCollection(TNSCollection):
    __swig_setmethods__ = {}
    for _s in [TNSCollection]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TCollection, name, value)
    __swig_getmethods__ = {}
    for _s in [TNSCollection]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TCollection, name)
    def __repr__(self):
        return "<C TCollection instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TCollection, 'this', _compatlayer.new_TCollection(*args))
        _swig_setattr(self, TCollection, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TCollection):
        try:
            if self.thisown: destroy(self)
        except: pass

class TCollectionPtr(TCollection):
    def __init__(self, this):
        _swig_setattr(self, TCollection, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TCollection, 'thisown', 0)
        _swig_setattr(self, TCollection,self.__class__,TCollection)
_compatlayer.TCollection_swigregister(TCollectionPtr)

class TSortedCollection(TNSSortedCollection,TCollection):
    __swig_setmethods__ = {}
    for _s in [TNSSortedCollection,TCollection]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TSortedCollection, name, value)
    __swig_getmethods__ = {}
    for _s in [TNSSortedCollection,TCollection]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TSortedCollection, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<C TSortedCollection instance at %s>" % (self.this,)
    def __del__(self, destroy=_compatlayer.delete_TSortedCollection):
        try:
            if self.thisown: destroy(self)
        except: pass

class TSortedCollectionPtr(TSortedCollection):
    def __init__(self, this):
        _swig_setattr(self, TSortedCollection, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TSortedCollection, 'thisown', 0)
        _swig_setattr(self, TSortedCollection,self.__class__,TSortedCollection)
_compatlayer.TSortedCollection_swigregister(TSortedCollectionPtr)

class TStringCollection(TSortedCollection):
    __swig_setmethods__ = {}
    for _s in [TSortedCollection]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TStringCollection, name, value)
    __swig_getmethods__ = {}
    for _s in [TSortedCollection]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TStringCollection, name)
    def __repr__(self):
        return "<C TStringCollection instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TStringCollection, 'this', _compatlayer.new_TStringCollection(*args))
        _swig_setattr(self, TStringCollection, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TStringCollection):
        try:
            if self.thisown: destroy(self)
        except: pass

class TStringCollectionPtr(TStringCollection):
    def __init__(self, this):
        _swig_setattr(self, TStringCollection, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TStringCollection, 'thisown', 0)
        _swig_setattr(self, TStringCollection,self.__class__,TStringCollection)
_compatlayer.TStringCollection_swigregister(TStringCollectionPtr)

class TPoint(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TPoint, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TPoint, name)
    def __repr__(self):
        return "<C TPoint instance at %s>" % (self.this,)
    def __iadd__(*args): return _compatlayer.TPoint___iadd__(*args)
    def __isub__(*args): return _compatlayer.TPoint___isub__(*args)
    __swig_setmethods__["x"] = _compatlayer.TPoint_x_set
    __swig_getmethods__["x"] = _compatlayer.TPoint_x_get
    if _newclass:x = property(_compatlayer.TPoint_x_get, _compatlayer.TPoint_x_set)
    __swig_setmethods__["y"] = _compatlayer.TPoint_y_set
    __swig_getmethods__["y"] = _compatlayer.TPoint_y_get
    if _newclass:y = property(_compatlayer.TPoint_y_get, _compatlayer.TPoint_y_set)
    def __init__(self, *args):
        _swig_setattr(self, TPoint, 'this', _compatlayer.new_TPoint(*args))
        _swig_setattr(self, TPoint, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TPoint):
        try:
            if self.thisown: destroy(self)
        except: pass

class TPointPtr(TPoint):
    def __init__(self, this):
        _swig_setattr(self, TPoint, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TPoint, 'thisown', 0)
        _swig_setattr(self, TPoint,self.__class__,TPoint)
_compatlayer.TPoint_swigregister(TPointPtr)

class TRect(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TRect, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TRect, name)
    def __repr__(self):
        return "<C TRect instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TRect, 'this', _compatlayer.new_TRect(*args))
        _swig_setattr(self, TRect, 'thisown', 1)
    def move(*args): return _compatlayer.TRect_move(*args)
    def grow(*args): return _compatlayer.TRect_grow(*args)
    def intersect(*args): return _compatlayer.TRect_intersect(*args)
    def Union(*args): return _compatlayer.TRect_Union(*args)
    def contains(*args): return _compatlayer.TRect_contains(*args)
    def __eq__(*args): return _compatlayer.TRect___eq__(*args)
    def __ne__(*args): return _compatlayer.TRect___ne__(*args)
    def isEmpty(*args): return _compatlayer.TRect_isEmpty(*args)
    __swig_setmethods__["a"] = _compatlayer.TRect_a_set
    __swig_getmethods__["a"] = _compatlayer.TRect_a_get
    if _newclass:a = property(_compatlayer.TRect_a_get, _compatlayer.TRect_a_set)
    __swig_setmethods__["b"] = _compatlayer.TRect_b_set
    __swig_getmethods__["b"] = _compatlayer.TRect_b_get
    if _newclass:b = property(_compatlayer.TRect_b_get, _compatlayer.TRect_b_set)
    def __del__(self, destroy=_compatlayer.delete_TRect):
        try:
            if self.thisown: destroy(self)
        except: pass

class TRectPtr(TRect):
    def __init__(self, this):
        _swig_setattr(self, TRect, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TRect, 'thisown', 0)
        _swig_setattr(self, TRect,self.__class__,TRect)
_compatlayer.TRect_swigregister(TRectPtr)

class TPalette(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TPalette, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TPalette, name)
    def __repr__(self):
        return "<C TPalette instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TPalette, 'this', _compatlayer.new_TPalette(*args))
        _swig_setattr(self, TPalette, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TPalette):
        try:
            if self.thisown: destroy(self)
        except: pass
    __swig_setmethods__["data"] = _compatlayer.TPalette_data_set
    __swig_getmethods__["data"] = _compatlayer.TPalette_data_get
    if _newclass:data = property(_compatlayer.TPalette_data_get, _compatlayer.TPalette_data_set)

class TPalettePtr(TPalette):
    def __init__(self, this):
        _swig_setattr(self, TPalette, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TPalette, 'thisown', 0)
        _swig_setattr(self, TPalette,self.__class__,TPalette)
_compatlayer.TPalette_swigregister(TPalettePtr)

class TCommandSet(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TCommandSet, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TCommandSet, name)
    def __repr__(self):
        return "<C TCommandSet instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TCommandSet, 'this', _compatlayer.new_TCommandSet(*args))
        _swig_setattr(self, TCommandSet, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TCommandSet):
        try:
            if self.thisown: destroy(self)
        except: pass
    def has(*args): return _compatlayer.TCommandSet_has(*args)
    def disableCmdInt(*args): return _compatlayer.TCommandSet_disableCmdInt(*args)
    def disableCmdRange(*args): return _compatlayer.TCommandSet_disableCmdRange(*args)
    def enableCmdInt(*args): return _compatlayer.TCommandSet_enableCmdInt(*args)
    def enableCmdRange(*args): return _compatlayer.TCommandSet_enableCmdRange(*args)
    def enableAllCommands(*args): return _compatlayer.TCommandSet_enableAllCommands(*args)
    def disableCmd(*args): return _compatlayer.TCommandSet_disableCmd(*args)
    def enableCmd(*args): return _compatlayer.TCommandSet_enableCmd(*args)
    def __iadd__(*args): return _compatlayer.TCommandSet___iadd__(*args)
    def __isub__(*args): return _compatlayer.TCommandSet___isub__(*args)
    def isEmpty(*args): return _compatlayer.TCommandSet_isEmpty(*args)
    def set(*args): return _compatlayer.TCommandSet_set(*args)
    def __iand__(*args): return _compatlayer.TCommandSet___iand__(*args)
    def __ior__(*args): return _compatlayer.TCommandSet___ior__(*args)

class TCommandSetPtr(TCommandSet):
    def __init__(self, this):
        _swig_setattr(self, TCommandSet, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TCommandSet, 'thisown', 0)
        _swig_setattr(self, TCommandSet,self.__class__,TCommandSet)
_compatlayer.TCommandSet_swigregister(TCommandSetPtr)

class write_args(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, write_args, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, write_args, name)
    def __repr__(self):
        return "<C write_args instance at %s>" % (self.this,)
    __swig_setmethods__["self"] = _compatlayer.write_args_self_set
    __swig_getmethods__["self"] = _compatlayer.write_args_self_get
    if _newclass:self = property(_compatlayer.write_args_self_get, _compatlayer.write_args_self_set)
    __swig_setmethods__["target"] = _compatlayer.write_args_target_set
    __swig_getmethods__["target"] = _compatlayer.write_args_target_get
    if _newclass:target = property(_compatlayer.write_args_target_get, _compatlayer.write_args_target_set)
    __swig_setmethods__["buf"] = _compatlayer.write_args_buf_set
    __swig_getmethods__["buf"] = _compatlayer.write_args_buf_get
    if _newclass:buf = property(_compatlayer.write_args_buf_get, _compatlayer.write_args_buf_set)
    __swig_setmethods__["offset"] = _compatlayer.write_args_offset_set
    __swig_getmethods__["offset"] = _compatlayer.write_args_offset_get
    if _newclass:offset = property(_compatlayer.write_args_offset_get, _compatlayer.write_args_offset_set)
    def __init__(self, *args):
        _swig_setattr(self, write_args, 'this', _compatlayer.new_write_args(*args))
        _swig_setattr(self, write_args, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_write_args):
        try:
            if self.thisown: destroy(self)
        except: pass

class write_argsPtr(write_args):
    def __init__(self, this):
        _swig_setattr(self, write_args, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, write_args, 'thisown', 0)
        _swig_setattr(self, write_args,self.__class__,write_args)
_compatlayer.write_args_swigregister(write_argsPtr)

class TView(TObject):
    __swig_setmethods__ = {}
    for _s in [TObject]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TView, name, value)
    __swig_getmethods__ = {}
    for _s in [TObject]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TView, name)
    def __repr__(self):
        return "<C TView instance at %s>" % (self.this,)
    phFocused = _compatlayer.TView_phFocused
    phPreProcess = _compatlayer.TView_phPreProcess
    phPostProcess = _compatlayer.TView_phPostProcess
    normalSelect = _compatlayer.TView_normalSelect
    enterSelect = _compatlayer.TView_enterSelect
    leaveSelect = _compatlayer.TView_leaveSelect
    def __init__(self, *args):
        _swig_setattr(self, TView, 'this', _compatlayer.new_TView(*args))
        _swig_setattr(self, TView, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TView):
        try:
            if self.thisown: destroy(self)
        except: pass
    def sizeLimits(*args): return _compatlayer.TView_sizeLimits(*args)
    def getBounds(*args): return _compatlayer.TView_getBounds(*args)
    def getExtent(*args): return _compatlayer.TView_getExtent(*args)
    def getClipRect(*args): return _compatlayer.TView_getClipRect(*args)
    def mouseInView(*args): return _compatlayer.TView_mouseInView(*args)
    def containsMouse(*args): return _compatlayer.TView_containsMouse(*args)
    def locate(*args): return _compatlayer.TView_locate(*args)
    def dragView(*args): return _compatlayer.TView_dragView(*args)
    def calcBounds(*args): return _compatlayer.TView_calcBounds(*args)
    def changeBounds(*args): return _compatlayer.TView_changeBounds(*args)
    def growTo(*args): return _compatlayer.TView_growTo(*args)
    def moveTo(*args): return _compatlayer.TView_moveTo(*args)
    def setBounds(*args): return _compatlayer.TView_setBounds(*args)
    def getHelpCtx(*args): return _compatlayer.TView_getHelpCtx(*args)
    def valid(*args): return _compatlayer.TView_valid(*args)
    def hide(*args): return _compatlayer.TView_hide(*args)
    def show(*args): return _compatlayer.TView_show(*args)
    def draw(*args): return _compatlayer.TView_draw(*args)
    def drawView(*args): return _compatlayer.TView_drawView(*args)
    def exposed(*args): return _compatlayer.TView_exposed(*args)
    def hideCursor(*args): return _compatlayer.TView_hideCursor(*args)
    def drawHide(*args): return _compatlayer.TView_drawHide(*args)
    def drawShow(*args): return _compatlayer.TView_drawShow(*args)
    def drawUnderRect(*args): return _compatlayer.TView_drawUnderRect(*args)
    def drawUnderView(*args): return _compatlayer.TView_drawUnderView(*args)
    def dataSize(*args): return _compatlayer.TView_dataSize(*args)
    def getData(*args): return _compatlayer.TView_getData(*args)
    def setData(*args): return _compatlayer.TView_setData(*args)
    def blockCursor(*args): return _compatlayer.TView_blockCursor(*args)
    def normalCursor(*args): return _compatlayer.TView_normalCursor(*args)
    def resetCursor(*args): return _compatlayer.TView_resetCursor(*args)
    def setCursor(*args): return _compatlayer.TView_setCursor(*args)
    def showCursor(*args): return _compatlayer.TView_showCursor(*args)
    def drawCursor(*args): return _compatlayer.TView_drawCursor(*args)
    def clearEvent(*args): return _compatlayer.TView_clearEvent(*args)
    def eventAvail(*args): return _compatlayer.TView_eventAvail(*args)
    def getEvent(*args): return _compatlayer.TView_getEvent(*args)
    def handleEvent(*args): return _compatlayer.TView_handleEvent(*args)
    def putEvent(*args): return _compatlayer.TView_putEvent(*args)
    __swig_getmethods__["commandEnabled"] = lambda x: _compatlayer.TView_commandEnabled
    if _newclass:commandEnabled = staticmethod(_compatlayer.TView_commandEnabled)
    __swig_getmethods__["disableCommands"] = lambda x: _compatlayer.TView_disableCommands
    if _newclass:disableCommands = staticmethod(_compatlayer.TView_disableCommands)
    __swig_getmethods__["enableCommands"] = lambda x: _compatlayer.TView_enableCommands
    if _newclass:enableCommands = staticmethod(_compatlayer.TView_enableCommands)
    __swig_getmethods__["disableCommand"] = lambda x: _compatlayer.TView_disableCommand
    if _newclass:disableCommand = staticmethod(_compatlayer.TView_disableCommand)
    __swig_getmethods__["enableCommand"] = lambda x: _compatlayer.TView_enableCommand
    if _newclass:enableCommand = staticmethod(_compatlayer.TView_enableCommand)
    __swig_getmethods__["getCommands"] = lambda x: _compatlayer.TView_getCommands
    if _newclass:getCommands = staticmethod(_compatlayer.TView_getCommands)
    __swig_getmethods__["setCommands"] = lambda x: _compatlayer.TView_setCommands
    if _newclass:setCommands = staticmethod(_compatlayer.TView_setCommands)
    def endModal(*args): return _compatlayer.TView_endModal(*args)
    def execute(*args): return _compatlayer.TView_execute(*args)
    def getColor(*args): return _compatlayer.TView_getColor(*args)
    def getPalette(*args): return _compatlayer.TView_getPalette(*args)
    def mapColor(*args): return _compatlayer.TView_mapColor(*args)
    def getState(*args): return _compatlayer.TView_getState(*args)
    def select(*args): return _compatlayer.TView_select(*args)
    def setState(*args): return _compatlayer.TView_setState(*args)
    def keyEvent(*args): return _compatlayer.TView_keyEvent(*args)
    def mouseEvent(*args): return _compatlayer.TView_mouseEvent(*args)
    def makeGlobal(*args): return _compatlayer.TView_makeGlobal(*args)
    def makeLocal(*args): return _compatlayer.TView_makeLocal(*args)
    def nextView(*args): return _compatlayer.TView_nextView(*args)
    def prevView(*args): return _compatlayer.TView_prevView(*args)
    def prev(*args): return _compatlayer.TView_prev(*args)
    __swig_setmethods__["next"] = _compatlayer.TView_next_set
    __swig_getmethods__["next"] = _compatlayer.TView_next_get
    if _newclass:next = property(_compatlayer.TView_next_get, _compatlayer.TView_next_set)
    def makeFirst(*args): return _compatlayer.TView_makeFirst(*args)
    def putInFrontOf(*args): return _compatlayer.TView_putInFrontOf(*args)
    def TopView(*args): return _compatlayer.TView_TopView(*args)
    def writeBuf(*args): return _compatlayer.TView_writeBuf(*args)
    def writeNativeBuf(*args): return _compatlayer.TView_writeNativeBuf(*args)
    def writeLine(*args): return _compatlayer.TView_writeLine(*args)
    def writeNativeLine(*args): return _compatlayer.TView_writeNativeLine(*args)
    def writeChar(*args): return _compatlayer.TView_writeChar(*args)
    def writeCharU16(*args): return _compatlayer.TView_writeCharU16(*args)
    def writeStr(*args): return _compatlayer.TView_writeStr(*args)
    def writeStrU16(*args): return _compatlayer.TView_writeStrU16(*args)
    __swig_setmethods__["size"] = _compatlayer.TView_size_set
    __swig_getmethods__["size"] = _compatlayer.TView_size_get
    if _newclass:size = property(_compatlayer.TView_size_get, _compatlayer.TView_size_set)
    __swig_setmethods__["options"] = _compatlayer.TView_options_set
    __swig_getmethods__["options"] = _compatlayer.TView_options_get
    if _newclass:options = property(_compatlayer.TView_options_get, _compatlayer.TView_options_set)
    __swig_setmethods__["eventMask"] = _compatlayer.TView_eventMask_set
    __swig_getmethods__["eventMask"] = _compatlayer.TView_eventMask_get
    if _newclass:eventMask = property(_compatlayer.TView_eventMask_get, _compatlayer.TView_eventMask_set)
    __swig_setmethods__["state"] = _compatlayer.TView_state_set
    __swig_getmethods__["state"] = _compatlayer.TView_state_get
    if _newclass:state = property(_compatlayer.TView_state_get, _compatlayer.TView_state_set)
    __swig_setmethods__["origin"] = _compatlayer.TView_origin_set
    __swig_getmethods__["origin"] = _compatlayer.TView_origin_get
    if _newclass:origin = property(_compatlayer.TView_origin_get, _compatlayer.TView_origin_set)
    __swig_setmethods__["cursor"] = _compatlayer.TView_cursor_set
    __swig_getmethods__["cursor"] = _compatlayer.TView_cursor_get
    if _newclass:cursor = property(_compatlayer.TView_cursor_get, _compatlayer.TView_cursor_set)
    __swig_setmethods__["growMode"] = _compatlayer.TView_growMode_set
    __swig_getmethods__["growMode"] = _compatlayer.TView_growMode_get
    if _newclass:growMode = property(_compatlayer.TView_growMode_get, _compatlayer.TView_growMode_set)
    __swig_setmethods__["dragMode"] = _compatlayer.TView_dragMode_set
    __swig_getmethods__["dragMode"] = _compatlayer.TView_dragMode_get
    if _newclass:dragMode = property(_compatlayer.TView_dragMode_get, _compatlayer.TView_dragMode_set)
    __swig_setmethods__["helpCtx"] = _compatlayer.TView_helpCtx_set
    __swig_getmethods__["helpCtx"] = _compatlayer.TView_helpCtx_get
    if _newclass:helpCtx = property(_compatlayer.TView_helpCtx_get, _compatlayer.TView_helpCtx_set)
    __swig_setmethods__["owner"] = _compatlayer.TView_owner_set
    __swig_getmethods__["owner"] = _compatlayer.TView_owner_get
    if _newclass:owner = property(_compatlayer.TView_owner_get, _compatlayer.TView_owner_set)
    def shutDown(*args): return _compatlayer.TView_shutDown(*args)

class TViewPtr(TView):
    def __init__(self, this):
        _swig_setattr(self, TView, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TView, 'thisown', 0)
        _swig_setattr(self, TView,self.__class__,TView)
_compatlayer.TView_swigregister(TViewPtr)

TView_commandEnabled = _compatlayer.TView_commandEnabled

TView_disableCommands = _compatlayer.TView_disableCommands

TView_enableCommands = _compatlayer.TView_enableCommands

TView_disableCommand = _compatlayer.TView_disableCommand

TView_enableCommand = _compatlayer.TView_enableCommand

TView_getCommands = _compatlayer.TView_getCommands

TView_setCommands = _compatlayer.TView_setCommands

class TGroup(TView):
    __swig_setmethods__ = {}
    for _s in [TView]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TGroup, name, value)
    __swig_getmethods__ = {}
    for _s in [TView]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TGroup, name)
    def __repr__(self):
        return "<C TGroup instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TGroup, 'this', _compatlayer.new_TGroup(*args))
        _swig_setattr(self, TGroup, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TGroup):
        try:
            if self.thisown: destroy(self)
        except: pass
    def shutDown(*args): return _compatlayer.TGroup_shutDown(*args)
    def execView(*args): return _compatlayer.TGroup_execView(*args)
    def execute(*args): return _compatlayer.TGroup_execute(*args)
    def insertView(*args): return _compatlayer.TGroup_insertView(*args)
    def remove(*args): return _compatlayer.TGroup_remove(*args)
    def removeView(*args): return _compatlayer.TGroup_removeView(*args)
    def resetCurrent(*args): return _compatlayer.TGroup_resetCurrent(*args)
    def setCurrent(*args): return _compatlayer.TGroup_setCurrent(*args)
    def selectNext(*args): return _compatlayer.TGroup_selectNext(*args)
    def firstThat(*args): return _compatlayer.TGroup_firstThat(*args)
    def forEach(*args): return _compatlayer.TGroup_forEach(*args)
    def insert(*args): return _compatlayer.TGroup_insert(*args)
    def insert(self, p):
        p.thisown = 0
        return _tv.TGroup_insert(self, p)

    def insertBefore(*args): return _compatlayer.TGroup_insertBefore(*args)
    def insertBefore(self, p):
        p.thisown = 0
        return _tv.TGroup_insertBefore(self, p)

    __swig_setmethods__["current"] = _compatlayer.TGroup_current_set
    __swig_getmethods__["current"] = _compatlayer.TGroup_current_get
    if _newclass:current = property(_compatlayer.TGroup_current_get, _compatlayer.TGroup_current_set)
    def at(*args): return _compatlayer.TGroup_at(*args)
    def firstMatch(*args): return _compatlayer.TGroup_firstMatch(*args)
    def indexOf(*args): return _compatlayer.TGroup_indexOf(*args)
    def first(*args): return _compatlayer.TGroup_first(*args)
    def setState(*args): return _compatlayer.TGroup_setState(*args)
    def handleEvent(*args): return _compatlayer.TGroup_handleEvent(*args)
    def drawSubViews(*args): return _compatlayer.TGroup_drawSubViews(*args)
    def changeBounds(*args): return _compatlayer.TGroup_changeBounds(*args)
    def dataSize(*args): return _compatlayer.TGroup_dataSize(*args)
    def getData(*args): return _compatlayer.TGroup_getData(*args)
    def setData(*args): return _compatlayer.TGroup_setData(*args)
    def draw(*args): return _compatlayer.TGroup_draw(*args)
    def redraw(*args): return _compatlayer.TGroup_redraw(*args)
    def Redraw(*args): return _compatlayer.TGroup_Redraw(*args)
    def lock(*args): return _compatlayer.TGroup_lock(*args)
    def unlock(*args): return _compatlayer.TGroup_unlock(*args)
    def resetCursor(*args): return _compatlayer.TGroup_resetCursor(*args)
    def canShowCursor(*args): return _compatlayer.TGroup_canShowCursor(*args)
    def endModal(*args): return _compatlayer.TGroup_endModal(*args)
    def eventError(*args): return _compatlayer.TGroup_eventError(*args)
    def getHelpCtx(*args): return _compatlayer.TGroup_getHelpCtx(*args)
    def valid(*args): return _compatlayer.TGroup_valid(*args)
    def freeBuffer(*args): return _compatlayer.TGroup_freeBuffer(*args)
    def getBuffer(*args): return _compatlayer.TGroup_getBuffer(*args)
    __swig_setmethods__["last"] = _compatlayer.TGroup_last_set
    __swig_getmethods__["last"] = _compatlayer.TGroup_last_get
    if _newclass:last = property(_compatlayer.TGroup_last_get, _compatlayer.TGroup_last_set)
    __swig_setmethods__["clip"] = _compatlayer.TGroup_clip_set
    __swig_getmethods__["clip"] = _compatlayer.TGroup_clip_get
    if _newclass:clip = property(_compatlayer.TGroup_clip_get, _compatlayer.TGroup_clip_set)
    __swig_setmethods__["phase"] = _compatlayer.TGroup_phase_set
    __swig_getmethods__["phase"] = _compatlayer.TGroup_phase_get
    if _newclass:phase = property(_compatlayer.TGroup_phase_get, _compatlayer.TGroup_phase_set)
    __swig_setmethods__["buffer"] = _compatlayer.TGroup_buffer_set
    __swig_getmethods__["buffer"] = _compatlayer.TGroup_buffer_get
    if _newclass:buffer = property(_compatlayer.TGroup_buffer_get, _compatlayer.TGroup_buffer_set)
    __swig_setmethods__["lockFlag"] = _compatlayer.TGroup_lockFlag_set
    __swig_getmethods__["lockFlag"] = _compatlayer.TGroup_lockFlag_get
    if _newclass:lockFlag = property(_compatlayer.TGroup_lockFlag_get, _compatlayer.TGroup_lockFlag_set)
    __swig_setmethods__["endState"] = _compatlayer.TGroup_endState_set
    __swig_getmethods__["endState"] = _compatlayer.TGroup_endState_get
    if _newclass:endState = property(_compatlayer.TGroup_endState_get, _compatlayer.TGroup_endState_set)

class TGroupPtr(TGroup):
    def __init__(self, this):
        _swig_setattr(self, TGroup, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TGroup, 'thisown', 0)
        _swig_setattr(self, TGroup,self.__class__,TGroup)
_compatlayer.TGroup_swigregister(TGroupPtr)

class TWindowInit(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TWindowInit, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TWindowInit, name)
    def __repr__(self):
        return "<C TWindowInit instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TWindowInit, 'this', _compatlayer.new_TWindowInit(*args))
        _swig_setattr(self, TWindowInit, 'thisown', 1)
    def defaultInitFrame(*args): return _compatlayer.TWindowInit_defaultInitFrame(*args)
    def __del__(self, destroy=_compatlayer.delete_TWindowInit):
        try:
            if self.thisown: destroy(self)
        except: pass

class TWindowInitPtr(TWindowInit):
    def __init__(self, this):
        _swig_setattr(self, TWindowInit, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TWindowInit, 'thisown', 0)
        _swig_setattr(self, TWindowInit,self.__class__,TWindowInit)
_compatlayer.TWindowInit_swigregister(TWindowInitPtr)

class TWindow(TGroup,TWindowInit):
    __swig_setmethods__ = {}
    for _s in [TGroup,TWindowInit]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TWindow, name, value)
    __swig_getmethods__ = {}
    for _s in [TGroup,TWindowInit]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TWindow, name)
    def __repr__(self):
        return "<C TWindow instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TWindow, 'this', _compatlayer.new_TWindow(*args))
        _swig_setattr(self, TWindow, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TWindow):
        try:
            if self.thisown: destroy(self)
        except: pass
    def close(*args): return _compatlayer.TWindow_close(*args)
    def getPalette(*args): return _compatlayer.TWindow_getPalette(*args)
    def getTitle(*args): return _compatlayer.TWindow_getTitle(*args)
    def handleEvent(*args): return _compatlayer.TWindow_handleEvent(*args)
    __swig_getmethods__["initFrame"] = lambda x: _compatlayer.TWindow_initFrame
    if _newclass:initFrame = staticmethod(_compatlayer.TWindow_initFrame)
    def setState(*args): return _compatlayer.TWindow_setState(*args)
    def sizeLimits(*args): return _compatlayer.TWindow_sizeLimits(*args)
    def standardScrollBar(*args): return _compatlayer.TWindow_standardScrollBar(*args)
    def zoom(*args): return _compatlayer.TWindow_zoom(*args)
    def shutDown(*args): return _compatlayer.TWindow_shutDown(*args)
    __swig_setmethods__["flags"] = _compatlayer.TWindow_flags_set
    __swig_getmethods__["flags"] = _compatlayer.TWindow_flags_get
    if _newclass:flags = property(_compatlayer.TWindow_flags_get, _compatlayer.TWindow_flags_set)
    __swig_setmethods__["zoomRect"] = _compatlayer.TWindow_zoomRect_set
    __swig_getmethods__["zoomRect"] = _compatlayer.TWindow_zoomRect_get
    if _newclass:zoomRect = property(_compatlayer.TWindow_zoomRect_get, _compatlayer.TWindow_zoomRect_set)
    __swig_setmethods__["number"] = _compatlayer.TWindow_number_set
    __swig_getmethods__["number"] = _compatlayer.TWindow_number_get
    if _newclass:number = property(_compatlayer.TWindow_number_get, _compatlayer.TWindow_number_set)
    __swig_setmethods__["palette"] = _compatlayer.TWindow_palette_set
    __swig_getmethods__["palette"] = _compatlayer.TWindow_palette_get
    if _newclass:palette = property(_compatlayer.TWindow_palette_get, _compatlayer.TWindow_palette_set)
    __swig_setmethods__["frame"] = _compatlayer.TWindow_frame_set
    __swig_getmethods__["frame"] = _compatlayer.TWindow_frame_get
    if _newclass:frame = property(_compatlayer.TWindow_frame_get, _compatlayer.TWindow_frame_set)
    __swig_setmethods__["title"] = _compatlayer.TWindow_title_set
    __swig_getmethods__["title"] = _compatlayer.TWindow_title_get
    if _newclass:title = property(_compatlayer.TWindow_title_get, _compatlayer.TWindow_title_set)
    __swig_setmethods__["intlTitle"] = _compatlayer.TWindow_intlTitle_set
    __swig_getmethods__["intlTitle"] = _compatlayer.TWindow_intlTitle_get
    if _newclass:intlTitle = property(_compatlayer.TWindow_intlTitle_get, _compatlayer.TWindow_intlTitle_set)

class TWindowPtr(TWindow):
    def __init__(self, this):
        _swig_setattr(self, TWindow, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TWindow, 'thisown', 0)
        _swig_setattr(self, TWindow,self.__class__,TWindow)
_compatlayer.TWindow_swigregister(TWindowPtr)

TWindow_initFrame = _compatlayer.TWindow_initFrame

class TScrollBar(TView):
    __swig_setmethods__ = {}
    for _s in [TView]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TScrollBar, name, value)
    __swig_getmethods__ = {}
    for _s in [TView]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TScrollBar, name)
    def __repr__(self):
        return "<C TScrollBar instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TScrollBar, 'this', _compatlayer.new_TScrollBar(*args))
        _swig_setattr(self, TScrollBar, 'thisown', 1)
    def draw(*args): return _compatlayer.TScrollBar_draw(*args)
    def getPalette(*args): return _compatlayer.TScrollBar_getPalette(*args)
    def handleEvent(*args): return _compatlayer.TScrollBar_handleEvent(*args)
    def scrollDraw(*args): return _compatlayer.TScrollBar_scrollDraw(*args)
    def scrollStep(*args): return _compatlayer.TScrollBar_scrollStep(*args)
    def setParams(*args): return _compatlayer.TScrollBar_setParams(*args)
    def setRange(*args): return _compatlayer.TScrollBar_setRange(*args)
    def setStep(*args): return _compatlayer.TScrollBar_setStep(*args)
    def setValue(*args): return _compatlayer.TScrollBar_setValue(*args)
    def drawPos(*args): return _compatlayer.TScrollBar_drawPos(*args)
    def getPos(*args): return _compatlayer.TScrollBar_getPos(*args)
    def getSize(*args): return _compatlayer.TScrollBar_getSize(*args)
    __swig_setmethods__["value"] = _compatlayer.TScrollBar_value_set
    __swig_getmethods__["value"] = _compatlayer.TScrollBar_value_get
    if _newclass:value = property(_compatlayer.TScrollBar_value_get, _compatlayer.TScrollBar_value_set)
    __swig_setmethods__["chars"] = _compatlayer.TScrollBar_chars_set
    __swig_getmethods__["chars"] = _compatlayer.TScrollBar_chars_get
    if _newclass:chars = property(_compatlayer.TScrollBar_chars_get, _compatlayer.TScrollBar_chars_set)
    __swig_setmethods__["minVal"] = _compatlayer.TScrollBar_minVal_set
    __swig_getmethods__["minVal"] = _compatlayer.TScrollBar_minVal_get
    if _newclass:minVal = property(_compatlayer.TScrollBar_minVal_get, _compatlayer.TScrollBar_minVal_set)
    __swig_setmethods__["maxVal"] = _compatlayer.TScrollBar_maxVal_set
    __swig_getmethods__["maxVal"] = _compatlayer.TScrollBar_maxVal_get
    if _newclass:maxVal = property(_compatlayer.TScrollBar_maxVal_get, _compatlayer.TScrollBar_maxVal_set)
    __swig_setmethods__["pgStep"] = _compatlayer.TScrollBar_pgStep_set
    __swig_getmethods__["pgStep"] = _compatlayer.TScrollBar_pgStep_get
    if _newclass:pgStep = property(_compatlayer.TScrollBar_pgStep_get, _compatlayer.TScrollBar_pgStep_set)
    __swig_setmethods__["arStep"] = _compatlayer.TScrollBar_arStep_set
    __swig_getmethods__["arStep"] = _compatlayer.TScrollBar_arStep_get
    if _newclass:arStep = property(_compatlayer.TScrollBar_arStep_get, _compatlayer.TScrollBar_arStep_set)
    def __del__(self, destroy=_compatlayer.delete_TScrollBar):
        try:
            if self.thisown: destroy(self)
        except: pass

class TScrollBarPtr(TScrollBar):
    def __init__(self, this):
        _swig_setattr(self, TScrollBar, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TScrollBar, 'thisown', 0)
        _swig_setattr(self, TScrollBar,self.__class__,TScrollBar)
_compatlayer.TScrollBar_swigregister(TScrollBarPtr)

class TScroller(TView):
    __swig_setmethods__ = {}
    for _s in [TView]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TScroller, name, value)
    __swig_getmethods__ = {}
    for _s in [TView]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TScroller, name)
    def __repr__(self):
        return "<C TScroller instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TScroller, 'this', _compatlayer.new_TScroller(*args))
        _swig_setattr(self, TScroller, 'thisown', 1)
    def changeBounds(*args): return _compatlayer.TScroller_changeBounds(*args)
    def getPalette(*args): return _compatlayer.TScroller_getPalette(*args)
    def handleEvent(*args): return _compatlayer.TScroller_handleEvent(*args)
    def scrollDraw(*args): return _compatlayer.TScroller_scrollDraw(*args)
    def scrollTo(*args): return _compatlayer.TScroller_scrollTo(*args)
    def setLimit(*args): return _compatlayer.TScroller_setLimit(*args)
    def setState(*args): return _compatlayer.TScroller_setState(*args)
    def checkDraw(*args): return _compatlayer.TScroller_checkDraw(*args)
    def shutDown(*args): return _compatlayer.TScroller_shutDown(*args)
    __swig_setmethods__["wheelStep"] = _compatlayer.TScroller_wheelStep_set
    __swig_getmethods__["wheelStep"] = _compatlayer.TScroller_wheelStep_get
    if _newclass:wheelStep = property(_compatlayer.TScroller_wheelStep_get, _compatlayer.TScroller_wheelStep_set)
    def __del__(self, destroy=_compatlayer.delete_TScroller):
        try:
            if self.thisown: destroy(self)
        except: pass

class TScrollerPtr(TScroller):
    def __init__(self, this):
        _swig_setattr(self, TScroller, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TScroller, 'thisown', 0)
        _swig_setattr(self, TScroller,self.__class__,TScroller)
_compatlayer.TScroller_swigregister(TScrollerPtr)

class TButton(TView):
    __swig_setmethods__ = {}
    for _s in [TView]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TButton, name, value)
    __swig_getmethods__ = {}
    for _s in [TView]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TButton, name)
    def __repr__(self):
        return "<C TButton instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TButton, 'this', _compatlayer.new_TButton(*args))
        _swig_setattr(self, TButton, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TButton):
        try:
            if self.thisown: destroy(self)
        except: pass
    def draw(*args): return _compatlayer.TButton_draw(*args)
    def drawState(*args): return _compatlayer.TButton_drawState(*args)
    def getPalette(*args): return _compatlayer.TButton_getPalette(*args)
    def handleEvent(*args): return _compatlayer.TButton_handleEvent(*args)
    def makeDefault(*args): return _compatlayer.TButton_makeDefault(*args)
    def press(*args): return _compatlayer.TButton_press(*args)
    def setState(*args): return _compatlayer.TButton_setState(*args)
    def setCallBack(*args): return _compatlayer.TButton_setCallBack(*args)
    def getText(*args): return _compatlayer.TButton_getText(*args)
    __swig_setmethods__["title"] = _compatlayer.TButton_title_set
    __swig_getmethods__["title"] = _compatlayer.TButton_title_get
    if _newclass:title = property(_compatlayer.TButton_title_get, _compatlayer.TButton_title_set)
    __swig_setmethods__["intlTitle"] = _compatlayer.TButton_intlTitle_set
    __swig_getmethods__["intlTitle"] = _compatlayer.TButton_intlTitle_get
    if _newclass:intlTitle = property(_compatlayer.TButton_intlTitle_get, _compatlayer.TButton_intlTitle_set)

class TButtonPtr(TButton):
    def __init__(self, this):
        _swig_setattr(self, TButton, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TButton, 'thisown', 0)
        _swig_setattr(self, TButton,self.__class__,TButton)
_compatlayer.TButton_swigregister(TButtonPtr)
btcbGoOn = cvar.btcbGoOn
btcbEndModal = cvar.btcbEndModal

class TInputLineBase(TView):
    __swig_setmethods__ = {}
    for _s in [TView]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TInputLineBase, name, value)
    __swig_getmethods__ = {}
    for _s in [TView]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TInputLineBase, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<C TInputLineBase instance at %s>" % (self.this,)
    def __del__(self, destroy=_compatlayer.delete_TInputLineBase):
        try:
            if self.thisown: destroy(self)
        except: pass
    def dataSize(*args): return _compatlayer.TInputLineBase_dataSize(*args)
    def getPalette(*args): return _compatlayer.TInputLineBase_getPalette(*args)
    def handleEvent(*args): return _compatlayer.TInputLineBase_handleEvent(*args)
    def selectAll(*args): return _compatlayer.TInputLineBase_selectAll(*args)
    def setState(*args): return _compatlayer.TInputLineBase_setState(*args)
    def SetValidator(*args): return _compatlayer.TInputLineBase_SetValidator(*args)
    def valid(*args): return _compatlayer.TInputLineBase_valid(*args)
    def insertChar(*args): return _compatlayer.TInputLineBase_insertChar(*args)
    def assignPos(*args): return _compatlayer.TInputLineBase_assignPos(*args)
    def pasteFromOSClipboard(*args): return _compatlayer.TInputLineBase_pasteFromOSClipboard(*args)
    def copyToOSClipboard(*args): return _compatlayer.TInputLineBase_copyToOSClipboard(*args)
    def setDataFromStr(*args): return _compatlayer.TInputLineBase_setDataFromStr(*args)
    def getData(*args): return _compatlayer.TInputLineBase_getData(*args)
    __swig_setmethods__["curPos"] = _compatlayer.TInputLineBase_curPos_set
    __swig_getmethods__["curPos"] = _compatlayer.TInputLineBase_curPos_get
    if _newclass:curPos = property(_compatlayer.TInputLineBase_curPos_get, _compatlayer.TInputLineBase_curPos_set)
    __swig_setmethods__["firstPos"] = _compatlayer.TInputLineBase_firstPos_set
    __swig_getmethods__["firstPos"] = _compatlayer.TInputLineBase_firstPos_get
    if _newclass:firstPos = property(_compatlayer.TInputLineBase_firstPos_get, _compatlayer.TInputLineBase_firstPos_set)
    __swig_setmethods__["selStart"] = _compatlayer.TInputLineBase_selStart_set
    __swig_getmethods__["selStart"] = _compatlayer.TInputLineBase_selStart_get
    if _newclass:selStart = property(_compatlayer.TInputLineBase_selStart_get, _compatlayer.TInputLineBase_selStart_set)
    __swig_setmethods__["selEnd"] = _compatlayer.TInputLineBase_selEnd_set
    __swig_getmethods__["selEnd"] = _compatlayer.TInputLineBase_selEnd_get
    if _newclass:selEnd = property(_compatlayer.TInputLineBase_selEnd_get, _compatlayer.TInputLineBase_selEnd_set)

class TInputLineBasePtr(TInputLineBase):
    def __init__(self, this):
        _swig_setattr(self, TInputLineBase, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TInputLineBase, 'thisown', 0)
        _swig_setattr(self, TInputLineBase,self.__class__,TInputLineBase)
_compatlayer.TInputLineBase_swigregister(TInputLineBasePtr)

class TInputLineBaseChar(TInputLineBase):
    __swig_setmethods__ = {}
    for _s in [TInputLineBase]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TInputLineBaseChar, name, value)
    __swig_getmethods__ = {}
    for _s in [TInputLineBase]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TInputLineBaseChar, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<C TInputLineBaseT<(char,TDrawBuffer)> instance at %s>" % (self.this,)
    def setData(*args): return _compatlayer.TInputLineBaseChar_setData(*args)
    def setDataFromStr(*args): return _compatlayer.TInputLineBaseChar_setDataFromStr(*args)
    def assignPos(*args): return _compatlayer.TInputLineBaseChar_assignPos(*args)
    def pasteFromOSClipboard(*args): return _compatlayer.TInputLineBaseChar_pasteFromOSClipboard(*args)
    def copyToOSClipboard(*args): return _compatlayer.TInputLineBaseChar_copyToOSClipboard(*args)
    def draw(*args): return _compatlayer.TInputLineBaseChar_draw(*args)
    def __del__(self, destroy=_compatlayer.delete_TInputLineBaseChar):
        try:
            if self.thisown: destroy(self)
        except: pass

class TInputLineBaseCharPtr(TInputLineBaseChar):
    def __init__(self, this):
        _swig_setattr(self, TInputLineBaseChar, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TInputLineBaseChar, 'thisown', 0)
        _swig_setattr(self, TInputLineBaseChar,self.__class__,TInputLineBaseChar)
_compatlayer.TInputLineBaseChar_swigregister(TInputLineBaseCharPtr)

class TInputLine(TInputLineBaseChar):
    __swig_setmethods__ = {}
    for _s in [TInputLineBaseChar]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TInputLine, name, value)
    __swig_getmethods__ = {}
    for _s in [TInputLineBaseChar]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TInputLine, name)
    def __repr__(self):
        return "<C TInputLine instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TInputLine, 'this', _compatlayer.new_TInputLine(*args))
        _swig_setattr(self, TInputLine, 'thisown', 1)
    def insertChar(*args): return _compatlayer.TInputLine_insertChar(*args)
    def __del__(self, destroy=_compatlayer.delete_TInputLine):
        try:
            if self.thisown: destroy(self)
        except: pass

class TInputLinePtr(TInputLine):
    def __init__(self, this):
        _swig_setattr(self, TInputLine, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TInputLine, 'thisown', 0)
        _swig_setattr(self, TInputLine,self.__class__,TInputLine)
_compatlayer.TInputLine_swigregister(TInputLinePtr)

class TInputLineBaseU16(TInputLineBase):
    __swig_setmethods__ = {}
    for _s in [TInputLineBase]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TInputLineBaseU16, name, value)
    __swig_getmethods__ = {}
    for _s in [TInputLineBase]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TInputLineBaseU16, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<C TInputLineBaseT<(uint16,TDrawBufferU16)> instance at %s>" % (self.this,)
    def setData(*args): return _compatlayer.TInputLineBaseU16_setData(*args)
    def setDataFromStr(*args): return _compatlayer.TInputLineBaseU16_setDataFromStr(*args)
    def assignPos(*args): return _compatlayer.TInputLineBaseU16_assignPos(*args)
    def pasteFromOSClipboard(*args): return _compatlayer.TInputLineBaseU16_pasteFromOSClipboard(*args)
    def copyToOSClipboard(*args): return _compatlayer.TInputLineBaseU16_copyToOSClipboard(*args)
    def draw(*args): return _compatlayer.TInputLineBaseU16_draw(*args)
    def __del__(self, destroy=_compatlayer.delete_TInputLineBaseU16):
        try:
            if self.thisown: destroy(self)
        except: pass

class TInputLineBaseU16Ptr(TInputLineBaseU16):
    def __init__(self, this):
        _swig_setattr(self, TInputLineBaseU16, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TInputLineBaseU16, 'thisown', 0)
        _swig_setattr(self, TInputLineBaseU16,self.__class__,TInputLineBaseU16)
_compatlayer.TInputLineBaseU16_swigregister(TInputLineBaseU16Ptr)

class TInputLineU16(TInputLineBaseU16):
    __swig_setmethods__ = {}
    for _s in [TInputLineBaseU16]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TInputLineU16, name, value)
    __swig_getmethods__ = {}
    for _s in [TInputLineBaseU16]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TInputLineU16, name)
    def __repr__(self):
        return "<C TInputLineU16 instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TInputLineU16, 'this', _compatlayer.new_TInputLineU16(*args))
        _swig_setattr(self, TInputLineU16, 'thisown', 1)
    def insertChar(*args): return _compatlayer.TInputLineU16_insertChar(*args)
    def __del__(self, destroy=_compatlayer.delete_TInputLineU16):
        try:
            if self.thisown: destroy(self)
        except: pass

class TInputLineU16Ptr(TInputLineU16):
    def __init__(self, this):
        _swig_setattr(self, TInputLineU16, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TInputLineU16, 'thisown', 0)
        _swig_setattr(self, TInputLineU16,self.__class__,TInputLineU16)
_compatlayer.TInputLineU16_swigregister(TInputLineU16Ptr)

class TStaticText(TView):
    __swig_setmethods__ = {}
    for _s in [TView]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TStaticText, name, value)
    __swig_getmethods__ = {}
    for _s in [TView]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TStaticText, name)
    def __repr__(self):
        return "<C TStaticText instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TStaticText, 'this', _compatlayer.new_TStaticText(*args))
        _swig_setattr(self, TStaticText, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TStaticText):
        try:
            if self.thisown: destroy(self)
        except: pass
    def draw(*args): return _compatlayer.TStaticText_draw(*args)
    def getPalette(*args): return _compatlayer.TStaticText_getPalette(*args)
    def getText(*args): return _compatlayer.TStaticText_getText(*args)

class TStaticTextPtr(TStaticText):
    def __init__(self, this):
        _swig_setattr(self, TStaticText, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TStaticText, 'thisown', 0)
        _swig_setattr(self, TStaticText,self.__class__,TStaticText)
_compatlayer.TStaticText_swigregister(TStaticTextPtr)

class T1StaticText(TStaticText):
    __swig_setmethods__ = {}
    for _s in [TStaticText]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, T1StaticText, name, value)
    __swig_getmethods__ = {}
    for _s in [TStaticText]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, T1StaticText, name)
    def __repr__(self):
        return "<C T1StaticText instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, T1StaticText, 'this', _compatlayer.new_T1StaticText(*args))
        _swig_setattr(self, T1StaticText, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_T1StaticText):
        try:
            if self.thisown: destroy(self)
        except: pass

class T1StaticTextPtr(T1StaticText):
    def __init__(self, this):
        _swig_setattr(self, T1StaticText, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, T1StaticText, 'thisown', 0)
        _swig_setattr(self, T1StaticText,self.__class__,T1StaticText)
_compatlayer.T1StaticText_swigregister(T1StaticTextPtr)

class TLabel(TStaticText):
    __swig_setmethods__ = {}
    for _s in [TStaticText]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TLabel, name, value)
    __swig_getmethods__ = {}
    for _s in [TStaticText]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TLabel, name)
    def __repr__(self):
        return "<C TLabel instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TLabel, 'this', _compatlayer.new_TLabel(*args))
        _swig_setattr(self, TLabel, 'thisown', 1)
    def draw(*args): return _compatlayer.TLabel_draw(*args)
    def getPalette(*args): return _compatlayer.TLabel_getPalette(*args)
    def handleEvent(*args): return _compatlayer.TLabel_handleEvent(*args)
    def shutDown(*args): return _compatlayer.TLabel_shutDown(*args)
    __swig_setmethods__["link"] = _compatlayer.TLabel_link_set
    __swig_getmethods__["link"] = _compatlayer.TLabel_link_get
    if _newclass:link = property(_compatlayer.TLabel_link_get, _compatlayer.TLabel_link_set)
    def __del__(self, destroy=_compatlayer.delete_TLabel):
        try:
            if self.thisown: destroy(self)
        except: pass

class TLabelPtr(TLabel):
    def __init__(self, this):
        _swig_setattr(self, TLabel, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TLabel, 'thisown', 0)
        _swig_setattr(self, TLabel,self.__class__,TLabel)
_compatlayer.TLabel_swigregister(TLabelPtr)

class T1Label(TLabel):
    __swig_setmethods__ = {}
    for _s in [TLabel]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, T1Label, name, value)
    __swig_getmethods__ = {}
    for _s in [TLabel]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, T1Label, name)
    def __repr__(self):
        return "<C T1Label instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, T1Label, 'this', _compatlayer.new_T1Label(*args))
        _swig_setattr(self, T1Label, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_T1Label):
        try:
            if self.thisown: destroy(self)
        except: pass

class T1LabelPtr(T1Label):
    def __init__(self, this):
        _swig_setattr(self, T1Label, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, T1Label, 'thisown', 0)
        _swig_setattr(self, T1Label,self.__class__,T1Label)
_compatlayer.T1Label_swigregister(T1LabelPtr)

class TSItem(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TSItem, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TSItem, name)
    def __repr__(self):
        return "<C TSItem instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TSItem, 'this', _compatlayer.new_TSItem(*args))
        _swig_setattr(self, TSItem, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TSItem):
        try:
            if self.thisown: destroy(self)
        except: pass
    def append(*args): return _compatlayer.TSItem_append(*args)
    def __add__(self, b):
        self.append(b)
        return self

    __swig_setmethods__["value"] = _compatlayer.TSItem_value_set
    __swig_getmethods__["value"] = _compatlayer.TSItem_value_get
    if _newclass:value = property(_compatlayer.TSItem_value_get, _compatlayer.TSItem_value_set)
    __swig_setmethods__["next"] = _compatlayer.TSItem_next_set
    __swig_getmethods__["next"] = _compatlayer.TSItem_next_get
    if _newclass:next = property(_compatlayer.TSItem_next_get, _compatlayer.TSItem_next_set)

class TSItemPtr(TSItem):
    def __init__(self, this):
        _swig_setattr(self, TSItem, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TSItem, 'thisown', 0)
        _swig_setattr(self, TSItem,self.__class__,TSItem)
_compatlayer.TSItem_swigregister(TSItemPtr)

class TCluster(TView):
    __swig_setmethods__ = {}
    for _s in [TView]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TCluster, name, value)
    __swig_getmethods__ = {}
    for _s in [TView]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TCluster, name)
    def __repr__(self):
        return "<C TCluster instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TCluster, 'this', _compatlayer.new_TCluster(*args))
        _swig_setattr(self, TCluster, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TCluster):
        try:
            if self.thisown: destroy(self)
        except: pass
    def dataSize(*args): return _compatlayer.TCluster_dataSize(*args)
    def drawBox(*args): return _compatlayer.TCluster_drawBox(*args)
    def getData(*args): return _compatlayer.TCluster_getData(*args)
    def getHelpCtx(*args): return _compatlayer.TCluster_getHelpCtx(*args)
    def getPalette(*args): return _compatlayer.TCluster_getPalette(*args)
    def handleEvent(*args): return _compatlayer.TCluster_handleEvent(*args)
    def mark(*args): return _compatlayer.TCluster_mark(*args)
    def press(*args): return _compatlayer.TCluster_press(*args)
    def movedTo(*args): return _compatlayer.TCluster_movedTo(*args)
    def setData(*args): return _compatlayer.TCluster_setData(*args)
    def setState(*args): return _compatlayer.TCluster_setState(*args)
    def getExtraOptions(*args): return _compatlayer.TCluster_getExtraOptions(*args)
    def setExtraOptions(*args): return _compatlayer.TCluster_setExtraOptions(*args)
    def getItemText(*args): return _compatlayer.TCluster_getItemText(*args)

class TClusterPtr(TCluster):
    def __init__(self, this):
        _swig_setattr(self, TCluster, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TCluster, 'thisown', 0)
        _swig_setattr(self, TCluster,self.__class__,TCluster)
_compatlayer.TCluster_swigregister(TClusterPtr)

class TRadioButtons(TCluster):
    __swig_setmethods__ = {}
    for _s in [TCluster]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TRadioButtons, name, value)
    __swig_getmethods__ = {}
    for _s in [TCluster]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TRadioButtons, name)
    def __repr__(self):
        return "<C TRadioButtons instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TRadioButtons, 'this', _compatlayer.new_TRadioButtons(*args))
        _swig_setattr(self, TRadioButtons, 'thisown', 1)
    def draw(*args): return _compatlayer.TRadioButtons_draw(*args)
    def mark(*args): return _compatlayer.TRadioButtons_mark(*args)
    def movedTo(*args): return _compatlayer.TRadioButtons_movedTo(*args)
    def press(*args): return _compatlayer.TRadioButtons_press(*args)
    def setData(*args): return _compatlayer.TRadioButtons_setData(*args)
    def __del__(self, destroy=_compatlayer.delete_TRadioButtons):
        try:
            if self.thisown: destroy(self)
        except: pass

class TRadioButtonsPtr(TRadioButtons):
    def __init__(self, this):
        _swig_setattr(self, TRadioButtons, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TRadioButtons, 'thisown', 0)
        _swig_setattr(self, TRadioButtons,self.__class__,TRadioButtons)
_compatlayer.TRadioButtons_swigregister(TRadioButtonsPtr)

class TRadioButtons32(TRadioButtons):
    __swig_setmethods__ = {}
    for _s in [TRadioButtons]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TRadioButtons32, name, value)
    __swig_getmethods__ = {}
    for _s in [TRadioButtons]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TRadioButtons32, name)
    def __repr__(self):
        return "<C TRadioButtons32 instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TRadioButtons32, 'this', _compatlayer.new_TRadioButtons32(*args))
        _swig_setattr(self, TRadioButtons32, 'thisown', 1)
    def dataSize(*args): return _compatlayer.TRadioButtons32_dataSize(*args)
    def __del__(self, destroy=_compatlayer.delete_TRadioButtons32):
        try:
            if self.thisown: destroy(self)
        except: pass

class TRadioButtons32Ptr(TRadioButtons32):
    def __init__(self, this):
        _swig_setattr(self, TRadioButtons32, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TRadioButtons32, 'thisown', 0)
        _swig_setattr(self, TRadioButtons32,self.__class__,TRadioButtons32)
_compatlayer.TRadioButtons32_swigregister(TRadioButtons32Ptr)

class TCheckBoxes(TCluster):
    __swig_setmethods__ = {}
    for _s in [TCluster]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TCheckBoxes, name, value)
    __swig_getmethods__ = {}
    for _s in [TCluster]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TCheckBoxes, name)
    def __repr__(self):
        return "<C TCheckBoxes instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TCheckBoxes, 'this', _compatlayer.new_TCheckBoxes(*args))
        _swig_setattr(self, TCheckBoxes, 'thisown', 1)
    def draw(*args): return _compatlayer.TCheckBoxes_draw(*args)
    def mark(*args): return _compatlayer.TCheckBoxes_mark(*args)
    def press(*args): return _compatlayer.TCheckBoxes_press(*args)
    def __del__(self, destroy=_compatlayer.delete_TCheckBoxes):
        try:
            if self.thisown: destroy(self)
        except: pass

class TCheckBoxesPtr(TCheckBoxes):
    def __init__(self, this):
        _swig_setattr(self, TCheckBoxes, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TCheckBoxes, 'thisown', 0)
        _swig_setattr(self, TCheckBoxes,self.__class__,TCheckBoxes)
_compatlayer.TCheckBoxes_swigregister(TCheckBoxesPtr)

class TCheckBoxes32(TCheckBoxes):
    __swig_setmethods__ = {}
    for _s in [TCheckBoxes]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TCheckBoxes32, name, value)
    __swig_getmethods__ = {}
    for _s in [TCheckBoxes]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TCheckBoxes32, name)
    def __repr__(self):
        return "<C TCheckBoxes32 instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TCheckBoxes32, 'this', _compatlayer.new_TCheckBoxes32(*args))
        _swig_setattr(self, TCheckBoxes32, 'thisown', 1)
    def dataSize(*args): return _compatlayer.TCheckBoxes32_dataSize(*args)
    def __del__(self, destroy=_compatlayer.delete_TCheckBoxes32):
        try:
            if self.thisown: destroy(self)
        except: pass

class TCheckBoxes32Ptr(TCheckBoxes32):
    def __init__(self, this):
        _swig_setattr(self, TCheckBoxes32, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TCheckBoxes32, 'thisown', 0)
        _swig_setattr(self, TCheckBoxes32,self.__class__,TCheckBoxes32)
_compatlayer.TCheckBoxes32_swigregister(TCheckBoxes32Ptr)

class TMenuItem(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TMenuItem, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TMenuItem, name)
    def __repr__(self):
        return "<C TMenuItem instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TMenuItem, 'this', _compatlayer.new_TMenuItem(*args))
        _swig_setattr(self, TMenuItem, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TMenuItem):
        try:
            if self.thisown: destroy(self)
        except: pass
    def append(*args): return _compatlayer.TMenuItem_append(*args)
    def append(self, p):
        p.thisown = 0
        return _tv.TMenuItem_append(self, p)

    __swig_setmethods__["next"] = _compatlayer.TMenuItem_next_set
    __swig_getmethods__["next"] = _compatlayer.TMenuItem_next_get
    if _newclass:next = property(_compatlayer.TMenuItem_next_get, _compatlayer.TMenuItem_next_set)
    __swig_setmethods__["name"] = _compatlayer.TMenuItem_name_set
    __swig_getmethods__["name"] = _compatlayer.TMenuItem_name_get
    if _newclass:name = property(_compatlayer.TMenuItem_name_get, _compatlayer.TMenuItem_name_set)
    __swig_setmethods__["intlName"] = _compatlayer.TMenuItem_intlName_set
    __swig_getmethods__["intlName"] = _compatlayer.TMenuItem_intlName_get
    if _newclass:intlName = property(_compatlayer.TMenuItem_intlName_get, _compatlayer.TMenuItem_intlName_set)
    __swig_setmethods__["command"] = _compatlayer.TMenuItem_command_set
    __swig_getmethods__["command"] = _compatlayer.TMenuItem_command_get
    if _newclass:command = property(_compatlayer.TMenuItem_command_get, _compatlayer.TMenuItem_command_set)
    __swig_setmethods__["disabled"] = _compatlayer.TMenuItem_disabled_set
    __swig_getmethods__["disabled"] = _compatlayer.TMenuItem_disabled_get
    if _newclass:disabled = property(_compatlayer.TMenuItem_disabled_get, _compatlayer.TMenuItem_disabled_set)
    __swig_setmethods__["keyCode"] = _compatlayer.TMenuItem_keyCode_set
    __swig_getmethods__["keyCode"] = _compatlayer.TMenuItem_keyCode_get
    if _newclass:keyCode = property(_compatlayer.TMenuItem_keyCode_get, _compatlayer.TMenuItem_keyCode_set)
    __swig_setmethods__["helpCtx"] = _compatlayer.TMenuItem_helpCtx_set
    __swig_getmethods__["helpCtx"] = _compatlayer.TMenuItem_helpCtx_get
    if _newclass:helpCtx = property(_compatlayer.TMenuItem_helpCtx_get, _compatlayer.TMenuItem_helpCtx_set)

class TMenuItemPtr(TMenuItem):
    def __init__(self, this):
        _swig_setattr(self, TMenuItem, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TMenuItem, 'thisown', 0)
        _swig_setattr(self, TMenuItem,self.__class__,TMenuItem)
_compatlayer.TMenuItem_swigregister(TMenuItemPtr)

class TSubMenu(TMenuItem):
    __swig_setmethods__ = {}
    for _s in [TMenuItem]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TSubMenu, name, value)
    __swig_getmethods__ = {}
    for _s in [TMenuItem]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TSubMenu, name)
    def __repr__(self):
        return "<C TSubMenu instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TSubMenu, 'this', _compatlayer.new_TSubMenu(*args))
        _swig_setattr(self, TSubMenu, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TSubMenu):
        try:
            if self.thisown: destroy(self)
        except: pass

class TSubMenuPtr(TSubMenu):
    def __init__(self, this):
        _swig_setattr(self, TSubMenu, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TSubMenu, 'thisown', 0)
        _swig_setattr(self, TSubMenu,self.__class__,TSubMenu)
_compatlayer.TSubMenu_swigregister(TSubMenuPtr)


makeMenu__ = _compatlayer.makeMenu__

cMakeMenu = _compatlayer.cMakeMenu
class TMenu(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TMenu, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TMenu, name)
    def __repr__(self):
        return "<C TMenu instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TMenu, 'this', _compatlayer.new_TMenu(*args))
        _swig_setattr(self, TMenu, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TMenu):
        try:
            if self.thisown: destroy(self)
        except: pass
    __swig_setmethods__["items"] = _compatlayer.TMenu_items_set
    __swig_getmethods__["items"] = _compatlayer.TMenu_items_get
    if _newclass:items = property(_compatlayer.TMenu_items_get, _compatlayer.TMenu_items_set)
    __swig_setmethods__["deflt"] = _compatlayer.TMenu_deflt_set
    __swig_getmethods__["deflt"] = _compatlayer.TMenu_deflt_get
    if _newclass:deflt = property(_compatlayer.TMenu_deflt_get, _compatlayer.TMenu_deflt_set)

class TMenuPtr(TMenu):
    def __init__(self, this):
        _swig_setattr(self, TMenu, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TMenu, 'thisown', 0)
        _swig_setattr(self, TMenu,self.__class__,TMenu)
_compatlayer.TMenu_swigregister(TMenuPtr)

class TMenuView(TView):
    __swig_setmethods__ = {}
    for _s in [TView]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TMenuView, name, value)
    __swig_getmethods__ = {}
    for _s in [TView]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TMenuView, name)
    def __repr__(self):
        return "<C TMenuView instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TMenuView, 'this', _compatlayer.new_TMenuView(*args))
        _swig_setattr(self, TMenuView, 'thisown', 1)
    def execute(*args): return _compatlayer.TMenuView_execute(*args)
    def findItem(*args): return _compatlayer.TMenuView_findItem(*args)
    def getItemRect(*args): return _compatlayer.TMenuView_getItemRect(*args)
    def getHelpCtx(*args): return _compatlayer.TMenuView_getHelpCtx(*args)
    def getPalette(*args): return _compatlayer.TMenuView_getPalette(*args)
    def handleEvent(*args): return _compatlayer.TMenuView_handleEvent(*args)
    def hotKey(*args): return _compatlayer.TMenuView_hotKey(*args)
    def newSubView(*args): return _compatlayer.TMenuView_newSubView(*args)
    __swig_setmethods__["compactMenu"] = _compatlayer.TMenuView_compactMenu_set
    __swig_getmethods__["compactMenu"] = _compatlayer.TMenuView_compactMenu_get
    if _newclass:compactMenu = property(_compatlayer.TMenuView_compactMenu_get, _compatlayer.TMenuView_compactMenu_set)
    def __del__(self, destroy=_compatlayer.delete_TMenuView):
        try:
            if self.thisown: destroy(self)
        except: pass

class TMenuViewPtr(TMenuView):
    def __init__(self, this):
        _swig_setattr(self, TMenuView, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TMenuView, 'thisown', 0)
        _swig_setattr(self, TMenuView,self.__class__,TMenuView)
_compatlayer.TMenuView_swigregister(TMenuViewPtr)

class TMenuBox(TMenuView):
    __swig_setmethods__ = {}
    for _s in [TMenuView]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TMenuBox, name, value)
    __swig_getmethods__ = {}
    for _s in [TMenuView]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TMenuBox, name)
    def __repr__(self):
        return "<C TMenuBox instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TMenuBox, 'this', _compatlayer.new_TMenuBox(*args))
        _swig_setattr(self, TMenuBox, 'thisown', 1)
    def draw(*args): return _compatlayer.TMenuBox_draw(*args)
    def getItemRect(*args): return _compatlayer.TMenuBox_getItemRect(*args)
    def __del__(self, destroy=_compatlayer.delete_TMenuBox):
        try:
            if self.thisown: destroy(self)
        except: pass

class TMenuBoxPtr(TMenuBox):
    def __init__(self, this):
        _swig_setattr(self, TMenuBox, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TMenuBox, 'thisown', 0)
        _swig_setattr(self, TMenuBox,self.__class__,TMenuBox)
_compatlayer.TMenuBox_swigregister(TMenuBoxPtr)

class TMenuBar(TMenuView):
    __swig_setmethods__ = {}
    for _s in [TMenuView]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TMenuBar, name, value)
    __swig_getmethods__ = {}
    for _s in [TMenuView]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TMenuBar, name)
    def __repr__(self):
        return "<C TMenuBar instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TMenuBar, 'this', _compatlayer.new_TMenuBar(*args))
        _swig_setattr(self, TMenuBar, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TMenuBar):
        try:
            if self.thisown: destroy(self)
        except: pass
    def computeLength(*args): return _compatlayer.TMenuBar_computeLength(*args)
    def draw(*args): return _compatlayer.TMenuBar_draw(*args)
    def getItemRect(*args): return _compatlayer.TMenuBar_getItemRect(*args)
    def changeBounds(*args): return _compatlayer.TMenuBar_changeBounds(*args)

class TMenuBarPtr(TMenuBar):
    def __init__(self, this):
        _swig_setattr(self, TMenuBar, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TMenuBar, 'thisown', 0)
        _swig_setattr(self, TMenuBar,self.__class__,TMenuBar)
_compatlayer.TMenuBar_swigregister(TMenuBarPtr)

class TStatusItem(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TStatusItem, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TStatusItem, name)
    def __repr__(self):
        return "<C TStatusItem instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TStatusItem, 'this', _compatlayer.new_TStatusItem(*args))
        _swig_setattr(self, TStatusItem, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TStatusItem):
        try:
            if self.thisown: destroy(self)
        except: pass
    __swig_setmethods__["next"] = _compatlayer.TStatusItem_next_set
    __swig_getmethods__["next"] = _compatlayer.TStatusItem_next_get
    if _newclass:next = property(_compatlayer.TStatusItem_next_get, _compatlayer.TStatusItem_next_set)
    __swig_setmethods__["text"] = _compatlayer.TStatusItem_text_set
    __swig_getmethods__["text"] = _compatlayer.TStatusItem_text_get
    if _newclass:text = property(_compatlayer.TStatusItem_text_get, _compatlayer.TStatusItem_text_set)
    __swig_setmethods__["intlText"] = _compatlayer.TStatusItem_intlText_set
    __swig_getmethods__["intlText"] = _compatlayer.TStatusItem_intlText_get
    if _newclass:intlText = property(_compatlayer.TStatusItem_intlText_get, _compatlayer.TStatusItem_intlText_set)
    __swig_setmethods__["keyCode"] = _compatlayer.TStatusItem_keyCode_set
    __swig_getmethods__["keyCode"] = _compatlayer.TStatusItem_keyCode_get
    if _newclass:keyCode = property(_compatlayer.TStatusItem_keyCode_get, _compatlayer.TStatusItem_keyCode_set)
    __swig_setmethods__["command"] = _compatlayer.TStatusItem_command_set
    __swig_getmethods__["command"] = _compatlayer.TStatusItem_command_get
    if _newclass:command = property(_compatlayer.TStatusItem_command_get, _compatlayer.TStatusItem_command_set)

class TStatusItemPtr(TStatusItem):
    def __init__(self, this):
        _swig_setattr(self, TStatusItem, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TStatusItem, 'thisown', 0)
        _swig_setattr(self, TStatusItem,self.__class__,TStatusItem)
_compatlayer.TStatusItem_swigregister(TStatusItemPtr)

class TStatusDef(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TStatusDef, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TStatusDef, name)
    def __repr__(self):
        return "<C TStatusDef instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TStatusDef, 'this', _compatlayer.new_TStatusDef(*args))
        _swig_setattr(self, TStatusDef, 'thisown', 1)
    __swig_setmethods__["next"] = _compatlayer.TStatusDef_next_set
    __swig_getmethods__["next"] = _compatlayer.TStatusDef_next_get
    if _newclass:next = property(_compatlayer.TStatusDef_next_get, _compatlayer.TStatusDef_next_set)
    __swig_setmethods__["min"] = _compatlayer.TStatusDef_min_set
    __swig_getmethods__["min"] = _compatlayer.TStatusDef_min_get
    if _newclass:min = property(_compatlayer.TStatusDef_min_get, _compatlayer.TStatusDef_min_set)
    __swig_setmethods__["max"] = _compatlayer.TStatusDef_max_set
    __swig_getmethods__["max"] = _compatlayer.TStatusDef_max_get
    if _newclass:max = property(_compatlayer.TStatusDef_max_get, _compatlayer.TStatusDef_max_set)
    __swig_setmethods__["items"] = _compatlayer.TStatusDef_items_set
    __swig_getmethods__["items"] = _compatlayer.TStatusDef_items_get
    if _newclass:items = property(_compatlayer.TStatusDef_items_get, _compatlayer.TStatusDef_items_set)
    def __del__(self, destroy=_compatlayer.delete_TStatusDef):
        try:
            if self.thisown: destroy(self)
        except: pass

class TStatusDefPtr(TStatusDef):
    def __init__(self, this):
        _swig_setattr(self, TStatusDef, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TStatusDef, 'thisown', 0)
        _swig_setattr(self, TStatusDef,self.__class__,TStatusDef)
_compatlayer.TStatusDef_swigregister(TStatusDefPtr)

class TStatusLine(TView):
    __swig_setmethods__ = {}
    for _s in [TView]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TStatusLine, name, value)
    __swig_getmethods__ = {}
    for _s in [TView]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TStatusLine, name)
    def __repr__(self):
        return "<C TStatusLine instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TStatusLine, 'this', _compatlayer.new_TStatusLine(*args))
        _swig_setattr(self, TStatusLine, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TStatusLine):
        try:
            if self.thisown: destroy(self)
        except: pass
    def draw(*args): return _compatlayer.TStatusLine_draw(*args)
    def getPalette(*args): return _compatlayer.TStatusLine_getPalette(*args)
    def handleEvent(*args): return _compatlayer.TStatusLine_handleEvent(*args)
    def hint(*args): return _compatlayer.TStatusLine_hint(*args)
    def update(*args): return _compatlayer.TStatusLine_update(*args)
    def computeLength(*args): return _compatlayer.TStatusLine_computeLength(*args)
    def changeBounds(*args): return _compatlayer.TStatusLine_changeBounds(*args)
    __swig_setmethods__["compactStatus"] = _compatlayer.TStatusLine_compactStatus_set
    __swig_getmethods__["compactStatus"] = _compatlayer.TStatusLine_compactStatus_get
    if _newclass:compactStatus = property(_compatlayer.TStatusLine_compactStatus_get, _compatlayer.TStatusLine_compactStatus_set)

class TStatusLinePtr(TStatusLine):
    def __init__(self, this):
        _swig_setattr(self, TStatusLine, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TStatusLine, 'thisown', 0)
        _swig_setattr(self, TStatusLine,self.__class__,TStatusLine)
_compatlayer.TStatusLine_swigregister(TStatusLinePtr)

dsktTileVertical = _compatlayer.dsktTileVertical
dsktTileHorizontal = _compatlayer.dsktTileHorizontal
class TDeskInit(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TDeskInit, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TDeskInit, name)
    def __repr__(self):
        return "<C TDeskInit instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TDeskInit, 'this', _compatlayer.new_TDeskInit(*args))
        _swig_setattr(self, TDeskInit, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TDeskInit):
        try:
            if self.thisown: destroy(self)
        except: pass

class TDeskInitPtr(TDeskInit):
    def __init__(self, this):
        _swig_setattr(self, TDeskInit, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TDeskInit, 'thisown', 0)
        _swig_setattr(self, TDeskInit,self.__class__,TDeskInit)
_compatlayer.TDeskInit_swigregister(TDeskInitPtr)

class TDeskTop(TGroup,TDeskInit):
    __swig_setmethods__ = {}
    for _s in [TGroup,TDeskInit]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TDeskTop, name, value)
    __swig_getmethods__ = {}
    for _s in [TGroup,TDeskInit]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TDeskTop, name)
    def __repr__(self):
        return "<C TDeskTop instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TDeskTop, 'this', _compatlayer.new_TDeskTop(*args))
        _swig_setattr(self, TDeskTop, 'thisown', 1)
    def cascade(*args): return _compatlayer.TDeskTop_cascade(*args)
    def handleEvent(*args): return _compatlayer.TDeskTop_handleEvent(*args)
    __swig_getmethods__["initBackground"] = lambda x: _compatlayer.TDeskTop_initBackground
    if _newclass:initBackground = staticmethod(_compatlayer.TDeskTop_initBackground)
    def tile(*args): return _compatlayer.TDeskTop_tile(*args)
    def tileError(*args): return _compatlayer.TDeskTop_tileError(*args)
    def shutDown(*args): return _compatlayer.TDeskTop_shutDown(*args)
    def getBackground(*args): return _compatlayer.TDeskTop_getBackground(*args)
    def getOptions(*args): return _compatlayer.TDeskTop_getOptions(*args)
    def setOptions(*args): return _compatlayer.TDeskTop_setOptions(*args)
    def canShowCursor(*args): return _compatlayer.TDeskTop_canShowCursor(*args)
    def execView(*args): return _compatlayer.TDeskTop_execView(*args)
    def __del__(self, destroy=_compatlayer.delete_TDeskTop):
        try:
            if self.thisown: destroy(self)
        except: pass

class TDeskTopPtr(TDeskTop):
    def __init__(self, this):
        _swig_setattr(self, TDeskTop, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TDeskTop, 'thisown', 0)
        _swig_setattr(self, TDeskTop,self.__class__,TDeskTop)
_compatlayer.TDeskTop_swigregister(TDeskTopPtr)

TDeskTop_initBackground = _compatlayer.TDeskTop_initBackground

cpColor = _compatlayer.cpColor
cpBlackWhite = _compatlayer.cpBlackWhite
cpMonochrome = _compatlayer.cpMonochrome
class TProgInit(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TProgInit, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TProgInit, name)
    def __repr__(self):
        return "<C TProgInit instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TProgInit, 'this', _compatlayer.new_TProgInit(*args))
        _swig_setattr(self, TProgInit, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TProgInit):
        try:
            if self.thisown: destroy(self)
        except: pass

class TProgInitPtr(TProgInit):
    def __init__(self, this):
        _swig_setattr(self, TProgInit, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TProgInit, 'thisown', 0)
        _swig_setattr(self, TProgInit,self.__class__,TProgInit)
_compatlayer.TProgInit_swigregister(TProgInitPtr)

class TProgram(TGroup,TProgInit):
    __swig_setmethods__ = {}
    for _s in [TGroup,TProgInit]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TProgram, name, value)
    __swig_getmethods__ = {}
    for _s in [TGroup,TProgInit]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TProgram, name)
    def __repr__(self):
        return "<C TProgram instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TProgram, 'this', _compatlayer.new_TProgram(*args))
        _swig_setattr(self, TProgram, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TProgram):
        try:
            if self.thisown: destroy(self)
        except: pass
    def getEvent(*args): return _compatlayer.TProgram_getEvent(*args)
    def getPalette(*args): return _compatlayer.TProgram_getPalette(*args)
    def handleEvent(*args): return _compatlayer.TProgram_handleEvent(*args)
    def idle(*args): return _compatlayer.TProgram_idle(*args)
    def initScreen(*args): return _compatlayer.TProgram_initScreen(*args)
    def outOfMemory(*args): return _compatlayer.TProgram_outOfMemory(*args)
    def putEvent(*args): return _compatlayer.TProgram_putEvent(*args)
    def run(*args): return _compatlayer.TProgram_run(*args)
    def setScreenMode(*args): return _compatlayer.TProgram_setScreenMode(*args)
    def setScreenModeExt(*args): return _compatlayer.TProgram_setScreenModeExt(*args)
    def validView(*args): return _compatlayer.TProgram_validView(*args)
    def shutDown(*args): return _compatlayer.TProgram_shutDown(*args)
    def suspend(*args): return _compatlayer.TProgram_suspend(*args)
    def resume(*args): return _compatlayer.TProgram_resume(*args)
    def syncScreenBuffer(*args): return _compatlayer.TProgram_syncScreenBuffer(*args)
    __swig_getmethods__["initStatusLine"] = lambda x: _compatlayer.TProgram_initStatusLine
    if _newclass:initStatusLine = staticmethod(_compatlayer.TProgram_initStatusLine)
    __swig_getmethods__["initMenuBar"] = lambda x: _compatlayer.TProgram_initMenuBar
    if _newclass:initMenuBar = staticmethod(_compatlayer.TProgram_initMenuBar)
    __swig_getmethods__["initDeskTop"] = lambda x: _compatlayer.TProgram_initDeskTop
    if _newclass:initDeskTop = staticmethod(_compatlayer.TProgram_initDeskTop)
    __swig_getmethods__["resetIdleTime"] = lambda x: _compatlayer.TProgram_resetIdleTime
    if _newclass:resetIdleTime = staticmethod(_compatlayer.TProgram_resetIdleTime)

class TProgramPtr(TProgram):
    def __init__(self, this):
        _swig_setattr(self, TProgram, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TProgram, 'thisown', 0)
        _swig_setattr(self, TProgram,self.__class__,TProgram)
_compatlayer.TProgram_swigregister(TProgramPtr)
apColor = cvar.apColor
apBlackWhite = cvar.apBlackWhite
apMonochrome = cvar.apMonochrome

TProgram_initStatusLine = _compatlayer.TProgram_initStatusLine

TProgram_initMenuBar = _compatlayer.TProgram_initMenuBar

TProgram_initDeskTop = _compatlayer.TProgram_initDeskTop

TProgram_resetIdleTime = _compatlayer.TProgram_resetIdleTime

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
        _swig_setattr(self, TApplication, 'this', _compatlayer.new_TApplication(*args))
        _swig_setattr(self, TApplication, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TApplication):
        try:
            if self.thisown: destroy(self)
        except: pass
    def suspend(*args): return _compatlayer.TApplication_suspend(*args)
    def resume(*args): return _compatlayer.TApplication_resume(*args)

class TApplicationPtr(TApplication):
    def __init__(self, this):
        _swig_setattr(self, TApplication, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TApplication, 'thisown', 0)
        _swig_setattr(self, TApplication,self.__class__,TApplication)
_compatlayer.TApplication_swigregister(TApplicationPtr)

cmValid = _compatlayer.cmValid
cmQuit = _compatlayer.cmQuit
cmError = _compatlayer.cmError
cmMenu = _compatlayer.cmMenu
cmClose = _compatlayer.cmClose
cmZoom = _compatlayer.cmZoom
cmResize = _compatlayer.cmResize
cmNext = _compatlayer.cmNext
cmPrev = _compatlayer.cmPrev
cmHelp = _compatlayer.cmHelp
cmOK = _compatlayer.cmOK
cmCancel = _compatlayer.cmCancel
cmYes = _compatlayer.cmYes
cmNo = _compatlayer.cmNo
cmDefault = _compatlayer.cmDefault
sfVisible = _compatlayer.sfVisible
sfCursorVis = _compatlayer.sfCursorVis
sfCursorIns = _compatlayer.sfCursorIns
sfShadow = _compatlayer.sfShadow
sfActive = _compatlayer.sfActive
sfSelected = _compatlayer.sfSelected
sfFocused = _compatlayer.sfFocused
sfDragging = _compatlayer.sfDragging
sfDisabled = _compatlayer.sfDisabled
sfModal = _compatlayer.sfModal
sfDefault = _compatlayer.sfDefault
sfExposed = _compatlayer.sfExposed
ofSelectable = _compatlayer.ofSelectable
ofTopSelect = _compatlayer.ofTopSelect
ofFirstClick = _compatlayer.ofFirstClick
ofFramed = _compatlayer.ofFramed
ofPreProcess = _compatlayer.ofPreProcess
ofPostProcess = _compatlayer.ofPostProcess
ofBuffered = _compatlayer.ofBuffered
ofTileable = _compatlayer.ofTileable
ofCenterX = _compatlayer.ofCenterX
ofCenterY = _compatlayer.ofCenterY
ofCentered = _compatlayer.ofCentered
ofBeVerbose = _compatlayer.ofBeVerbose
gfGrowLoX = _compatlayer.gfGrowLoX
gfGrowLoY = _compatlayer.gfGrowLoY
gfGrowHiX = _compatlayer.gfGrowHiX
gfGrowHiY = _compatlayer.gfGrowHiY
gfGrowAll = _compatlayer.gfGrowAll
gfGrowRel = _compatlayer.gfGrowRel
dmDragMove = _compatlayer.dmDragMove
dmDragGrow = _compatlayer.dmDragGrow
dmLimitLoX = _compatlayer.dmLimitLoX
dmLimitLoY = _compatlayer.dmLimitLoY
dmLimitHiX = _compatlayer.dmLimitHiX
dmLimitHiY = _compatlayer.dmLimitHiY
dmLimitAll = _compatlayer.dmLimitAll
hcNoContext = _compatlayer.hcNoContext
hcDragging = _compatlayer.hcDragging
sbLeftArrow = _compatlayer.sbLeftArrow
sbRightArrow = _compatlayer.sbRightArrow
sbPageLeft = _compatlayer.sbPageLeft
sbPageRight = _compatlayer.sbPageRight
sbUpArrow = _compatlayer.sbUpArrow
sbDownArrow = _compatlayer.sbDownArrow
sbPageUp = _compatlayer.sbPageUp
sbPageDown = _compatlayer.sbPageDown
sbIndicator = _compatlayer.sbIndicator
sbHorizontal = _compatlayer.sbHorizontal
sbVertical = _compatlayer.sbVertical
sbHandleKeyboard = _compatlayer.sbHandleKeyboard
wfMove = _compatlayer.wfMove
wfGrow = _compatlayer.wfGrow
wfClose = _compatlayer.wfClose
wfZoom = _compatlayer.wfZoom
noMenuBar = _compatlayer.noMenuBar
noDeskTop = _compatlayer.noDeskTop
noStatusLine = _compatlayer.noStatusLine
noBackground = _compatlayer.noBackground
noFrame = _compatlayer.noFrame
noViewer = _compatlayer.noViewer
noHistory = _compatlayer.noHistory
wnNoNumber = _compatlayer.wnNoNumber
wpBlueWindow = _compatlayer.wpBlueWindow
wpCyanWindow = _compatlayer.wpCyanWindow
wpGrayWindow = _compatlayer.wpGrayWindow
cmCut = _compatlayer.cmCut
cmCopy = _compatlayer.cmCopy
cmPaste = _compatlayer.cmPaste
cmUndo = _compatlayer.cmUndo
cmClear = _compatlayer.cmClear
cmTile = _compatlayer.cmTile
cmCascade = _compatlayer.cmCascade
cmReceivedFocus = _compatlayer.cmReceivedFocus
cmReleasedFocus = _compatlayer.cmReleasedFocus
cmCommandSetChanged = _compatlayer.cmCommandSetChanged
cmScrollBarChanged = _compatlayer.cmScrollBarChanged
cmScrollBarClicked = _compatlayer.cmScrollBarClicked
cmSelectWindowNum = _compatlayer.cmSelectWindowNum
cmListItemSelected = _compatlayer.cmListItemSelected
cmClosingWindow = _compatlayer.cmClosingWindow
cmClusterMovedTo = _compatlayer.cmClusterMovedTo
cmClusterPress = _compatlayer.cmClusterPress
cmRecordHistory = _compatlayer.cmRecordHistory
cmListItemFocused = _compatlayer.cmListItemFocused
cmGrabDefault = _compatlayer.cmGrabDefault
cmReleaseDefault = _compatlayer.cmReleaseDefault
cmUpdateCodePage = _compatlayer.cmUpdateCodePage
cmCallShell = _compatlayer.cmCallShell
positionalEvents = _compatlayer.positionalEvents
focusedEvents = _compatlayer.focusedEvents
kbSpace = _compatlayer.kbSpace
kbCtrlA = _compatlayer.kbCtrlA
kbCtrlB = _compatlayer.kbCtrlB
kbCtrlC = _compatlayer.kbCtrlC
kbCtrlD = _compatlayer.kbCtrlD
kbCtrlE = _compatlayer.kbCtrlE
kbCtrlF = _compatlayer.kbCtrlF
kbCtrlG = _compatlayer.kbCtrlG
kbCtrlH = _compatlayer.kbCtrlH
kbCtrlI = _compatlayer.kbCtrlI
kbCtrlJ = _compatlayer.kbCtrlJ
kbCtrlK = _compatlayer.kbCtrlK
kbCtrlL = _compatlayer.kbCtrlL
kbCtrlM = _compatlayer.kbCtrlM
kbCtrlN = _compatlayer.kbCtrlN
kbCtrlO = _compatlayer.kbCtrlO
kbCtrlP = _compatlayer.kbCtrlP
kbCtrlQ = _compatlayer.kbCtrlQ
kbCtrlR = _compatlayer.kbCtrlR
kbCtrlS = _compatlayer.kbCtrlS
kbCtrlT = _compatlayer.kbCtrlT
kbCtrlU = _compatlayer.kbCtrlU
kbCtrlV = _compatlayer.kbCtrlV
kbCtrlW = _compatlayer.kbCtrlW
kbCtrlX = _compatlayer.kbCtrlX
kbCtrlY = _compatlayer.kbCtrlY
kbCtrlZ = _compatlayer.kbCtrlZ
kbEsc = _compatlayer.kbEsc
kbAltSpace = _compatlayer.kbAltSpace
kbCtrlIns = _compatlayer.kbCtrlIns
kbShiftIns = _compatlayer.kbShiftIns
kbCtrlDel = _compatlayer.kbCtrlDel
kbShiftDel = _compatlayer.kbShiftDel
kbCtrlShiftIns = _compatlayer.kbCtrlShiftIns
kbCtrlShiftDel = _compatlayer.kbCtrlShiftDel
kbBack = _compatlayer.kbBack
kbCtrlBack = _compatlayer.kbCtrlBack
kbShiftTab = _compatlayer.kbShiftTab
kbTab = _compatlayer.kbTab
kbAltA = _compatlayer.kbAltA
kbAltB = _compatlayer.kbAltB
kbAltC = _compatlayer.kbAltC
kbAltD = _compatlayer.kbAltD
kbAltE = _compatlayer.kbAltE
kbAltF = _compatlayer.kbAltF
kbAltG = _compatlayer.kbAltG
kbAltH = _compatlayer.kbAltH
kbAltI = _compatlayer.kbAltI
kbAltJ = _compatlayer.kbAltJ
kbAltK = _compatlayer.kbAltK
kbAltL = _compatlayer.kbAltL
kbAltM = _compatlayer.kbAltM
kbAltN = _compatlayer.kbAltN
kbAltO = _compatlayer.kbAltO
kbAltP = _compatlayer.kbAltP
kbAltQ = _compatlayer.kbAltQ
kbAltR = _compatlayer.kbAltR
kbAltS = _compatlayer.kbAltS
kbAltT = _compatlayer.kbAltT
kbAltU = _compatlayer.kbAltU
kbAltV = _compatlayer.kbAltV
kbAltW = _compatlayer.kbAltW
kbAltX = _compatlayer.kbAltX
kbAltY = _compatlayer.kbAltY
kbAltZ = _compatlayer.kbAltZ
kbCtrlEnter = _compatlayer.kbCtrlEnter
kbEnter = _compatlayer.kbEnter
kbF1 = _compatlayer.kbF1
kbF2 = _compatlayer.kbF2
kbF3 = _compatlayer.kbF3
kbF4 = _compatlayer.kbF4
kbF5 = _compatlayer.kbF5
kbF6 = _compatlayer.kbF6
kbF7 = _compatlayer.kbF7
kbF8 = _compatlayer.kbF8
kbF9 = _compatlayer.kbF9
kbF10 = _compatlayer.kbF10
kbF11 = _compatlayer.kbF11
kbF12 = _compatlayer.kbF12
kbHome = _compatlayer.kbHome
kbUp = _compatlayer.kbUp
kbPgUp = _compatlayer.kbPgUp
kbLeft = _compatlayer.kbLeft
kbRight = _compatlayer.kbRight
kbEnd = _compatlayer.kbEnd
kbDown = _compatlayer.kbDown
kbPgDn = _compatlayer.kbPgDn
kbIns = _compatlayer.kbIns
kbDel = _compatlayer.kbDel
kbGrayMinus = _compatlayer.kbGrayMinus
kbGrayPlus = _compatlayer.kbGrayPlus
kbShiftF1 = _compatlayer.kbShiftF1
kbShiftF2 = _compatlayer.kbShiftF2
kbShiftF3 = _compatlayer.kbShiftF3
kbShiftF4 = _compatlayer.kbShiftF4
kbShiftF5 = _compatlayer.kbShiftF5
kbShiftF6 = _compatlayer.kbShiftF6
kbShiftF7 = _compatlayer.kbShiftF7
kbShiftF8 = _compatlayer.kbShiftF8
kbShiftF9 = _compatlayer.kbShiftF9
kbShiftF10 = _compatlayer.kbShiftF10
kbShiftF11 = _compatlayer.kbShiftF11
kbShiftF12 = _compatlayer.kbShiftF12
kbCtrlF1 = _compatlayer.kbCtrlF1
kbCtrlF2 = _compatlayer.kbCtrlF2
kbCtrlF3 = _compatlayer.kbCtrlF3
kbCtrlF4 = _compatlayer.kbCtrlF4
kbCtrlF5 = _compatlayer.kbCtrlF5
kbCtrlF6 = _compatlayer.kbCtrlF6
kbCtrlF7 = _compatlayer.kbCtrlF7
kbCtrlF8 = _compatlayer.kbCtrlF8
kbCtrlF9 = _compatlayer.kbCtrlF9
kbCtrlF10 = _compatlayer.kbCtrlF10
kbCtrlF11 = _compatlayer.kbCtrlF11
kbCtrlF12 = _compatlayer.kbCtrlF12
kbAltF1 = _compatlayer.kbAltF1
kbAltF2 = _compatlayer.kbAltF2
kbAltF3 = _compatlayer.kbAltF3
kbAltF4 = _compatlayer.kbAltF4
kbAltF5 = _compatlayer.kbAltF5
kbAltF6 = _compatlayer.kbAltF6
kbAltF7 = _compatlayer.kbAltF7
kbAltF8 = _compatlayer.kbAltF8
kbAltF9 = _compatlayer.kbAltF9
kbAltF10 = _compatlayer.kbAltF10
kbAltF11 = _compatlayer.kbAltF11
kbAltF12 = _compatlayer.kbAltF12
kbCtrlPrtSc = _compatlayer.kbCtrlPrtSc
kbCtrlLeft = _compatlayer.kbCtrlLeft
kbCtrlRight = _compatlayer.kbCtrlRight
kbCtrlEnd = _compatlayer.kbCtrlEnd
kbCtrlPgDn = _compatlayer.kbCtrlPgDn
kbCtrlHome = _compatlayer.kbCtrlHome
kbAlt1 = _compatlayer.kbAlt1
kbAlt2 = _compatlayer.kbAlt2
kbAlt3 = _compatlayer.kbAlt3
kbAlt4 = _compatlayer.kbAlt4
kbAlt5 = _compatlayer.kbAlt5
kbAlt6 = _compatlayer.kbAlt6
kbAlt7 = _compatlayer.kbAlt7
kbAlt8 = _compatlayer.kbAlt8
kbAlt9 = _compatlayer.kbAlt9
kbAlt0 = _compatlayer.kbAlt0
kbAltMinus = _compatlayer.kbAltMinus
kbAltEqual = _compatlayer.kbAltEqual
kbCtrlPgUp = _compatlayer.kbCtrlPgUp
kbNoKey = _compatlayer.kbNoKey
kbAltBack = _compatlayer.kbAltBack
kbRightShift = _compatlayer.kbRightShift
kbLeftShift = _compatlayer.kbLeftShift
kbShift = _compatlayer.kbShift
kbLeftCtrl = _compatlayer.kbLeftCtrl
kbRightCtrl = _compatlayer.kbRightCtrl
kbCtrlShift = _compatlayer.kbCtrlShift
kbLeftAlt = _compatlayer.kbLeftAlt
kbRightAlt = _compatlayer.kbRightAlt
kbAltShift = _compatlayer.kbAltShift
kbScrollState = _compatlayer.kbScrollState
kbNumState = _compatlayer.kbNumState
kbCapsState = _compatlayer.kbCapsState
kbInsState = _compatlayer.kbInsState
class TDialog(TWindow):
    __swig_setmethods__ = {}
    for _s in [TWindow]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TDialog, name, value)
    __swig_getmethods__ = {}
    for _s in [TWindow]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TDialog, name)
    def __repr__(self):
        return "<C TDialog instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TDialog, 'this', _compatlayer.new_TDialog(*args))
        _swig_setattr(self, TDialog, 'thisown', 1)
    def getPalette(*args): return _compatlayer.TDialog_getPalette(*args)
    def handleEvent(*args): return _compatlayer.TDialog_handleEvent(*args)
    def valid(*args): return _compatlayer.TDialog_valid(*args)
    def __del__(self, destroy=_compatlayer.delete_TDialog):
        try:
            if self.thisown: destroy(self)
        except: pass

class TDialogPtr(TDialog):
    def __init__(self, this):
        _swig_setattr(self, TDialog, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TDialog, 'thisown', 0)
        _swig_setattr(self, TDialog,self.__class__,TDialog)
_compatlayer.TDialog_swigregister(TDialogPtr)

fdOKButton = _compatlayer.fdOKButton
fdOpenButton = _compatlayer.fdOpenButton
fdReplaceButton = _compatlayer.fdReplaceButton
fdClearButton = _compatlayer.fdClearButton
fdHelpButton = _compatlayer.fdHelpButton
fdSelectButton = _compatlayer.fdSelectButton
fdDoneButton = _compatlayer.fdDoneButton
fdAddButton = _compatlayer.fdAddButton
fdNoLoadDir = _compatlayer.fdNoLoadDir
class TFileDialog(TDialog):
    __swig_setmethods__ = {}
    for _s in [TDialog]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TFileDialog, name, value)
    __swig_getmethods__ = {}
    for _s in [TDialog]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TFileDialog, name)
    def __repr__(self):
        return "<C TFileDialog instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TFileDialog, 'this', _compatlayer.new_TFileDialog(*args))
        _swig_setattr(self, TFileDialog, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TFileDialog):
        try:
            if self.thisown: destroy(self)
        except: pass
    def getData(*args): return _compatlayer.TFileDialog_getData(*args)
    def getFileName(*args): return _compatlayer.TFileDialog_getFileName(*args)
    def handleEvent(*args): return _compatlayer.TFileDialog_handleEvent(*args)
    def setData(*args): return _compatlayer.TFileDialog_setData(*args)
    def valid(*args): return _compatlayer.TFileDialog_valid(*args)
    def shutDown(*args): return _compatlayer.TFileDialog_shutDown(*args)
    def sizeLimits(*args): return _compatlayer.TFileDialog_sizeLimits(*args)
    __swig_setmethods__["fileName"] = _compatlayer.TFileDialog_fileName_set
    __swig_getmethods__["fileName"] = _compatlayer.TFileDialog_fileName_get
    if _newclass:fileName = property(_compatlayer.TFileDialog_fileName_get, _compatlayer.TFileDialog_fileName_set)
    __swig_setmethods__["fileList"] = _compatlayer.TFileDialog_fileList_set
    __swig_getmethods__["fileList"] = _compatlayer.TFileDialog_fileList_get
    if _newclass:fileList = property(_compatlayer.TFileDialog_fileList_get, _compatlayer.TFileDialog_fileList_set)
    __swig_setmethods__["wildCard"] = _compatlayer.TFileDialog_wildCard_set
    __swig_getmethods__["wildCard"] = _compatlayer.TFileDialog_wildCard_get
    if _newclass:wildCard = property(_compatlayer.TFileDialog_wildCard_get, _compatlayer.TFileDialog_wildCard_set)
    __swig_setmethods__["directory"] = _compatlayer.TFileDialog_directory_set
    __swig_getmethods__["directory"] = _compatlayer.TFileDialog_directory_get
    if _newclass:directory = property(_compatlayer.TFileDialog_directory_get, _compatlayer.TFileDialog_directory_set)

class TFileDialogPtr(TFileDialog):
    def __init__(self, this):
        _swig_setattr(self, TFileDialog, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TFileDialog, 'thisown', 0)
        _swig_setattr(self, TFileDialog,self.__class__,TFileDialog)
_compatlayer.TFileDialog_swigregister(TFileDialogPtr)

class TEditorApp(TApplication):
    __swig_setmethods__ = {}
    for _s in [TApplication]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TEditorApp, name, value)
    __swig_getmethods__ = {}
    for _s in [TApplication]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TEditorApp, name)
    def __repr__(self):
        return "<C TEditorApp instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TEditorApp, 'this', _compatlayer.new_TEditorApp(*args))
        _swig_setattr(self, TEditorApp, 'thisown', 1)
    def handleEvent(*args): return _compatlayer.TEditorApp_handleEvent(*args)
    __swig_getmethods__["initMenuBar"] = lambda x: _compatlayer.TEditorApp_initMenuBar
    if _newclass:initMenuBar = staticmethod(_compatlayer.TEditorApp_initMenuBar)
    __swig_getmethods__["initStatusLine"] = lambda x: _compatlayer.TEditorApp_initStatusLine
    if _newclass:initStatusLine = staticmethod(_compatlayer.TEditorApp_initStatusLine)
    def outOfMemory(*args): return _compatlayer.TEditorApp_outOfMemory(*args)
    def openEditor(*args): return _compatlayer.TEditorApp_openEditor(*args)
    def __del__(self, destroy=_compatlayer.delete_TEditorApp):
        try:
            if self.thisown: destroy(self)
        except: pass

class TEditorAppPtr(TEditorApp):
    def __init__(self, this):
        _swig_setattr(self, TEditorApp, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TEditorApp, 'thisown', 0)
        _swig_setattr(self, TEditorApp,self.__class__,TEditorApp)
_compatlayer.TEditorApp_swigregister(TEditorAppPtr)

TEditorApp_initMenuBar = _compatlayer.TEditorApp_initMenuBar

TEditorApp_initStatusLine = _compatlayer.TEditorApp_initStatusLine


execDialog = _compatlayer.execDialog

createFindDialog = _compatlayer.createFindDialog

createReplaceDialog = _compatlayer.createReplaceDialog
bfNormal = _compatlayer.bfNormal
bfDefault = _compatlayer.bfDefault
bfLeftJust = _compatlayer.bfLeftJust
bfBroadcast = _compatlayer.bfBroadcast

messageBox = _compatlayer.messageBox

messageBoxRect = _compatlayer.messageBoxRect

inputBox = _compatlayer.inputBox

inputBoxRect = _compatlayer.inputBoxRect
mfWarning = _compatlayer.mfWarning
mfError = _compatlayer.mfError
mfInformation = _compatlayer.mfInformation
mfConfirmation = _compatlayer.mfConfirmation
mfYesButton = _compatlayer.mfYesButton
mfNoButton = _compatlayer.mfNoButton
mfOKButton = _compatlayer.mfOKButton
mfCancelButton = _compatlayer.mfCancelButton
mfDontTranslate = _compatlayer.mfDontTranslate
mfDontShowAgain = _compatlayer.mfDontShowAgain
mfYesNoCancel = _compatlayer.mfYesNoCancel
mfOKCancel = _compatlayer.mfOKCancel
class MsgBoxText(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MsgBoxText, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MsgBoxText, name)
    def __repr__(self):
        return "<C MsgBoxText instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, MsgBoxText, 'this', _compatlayer.new_MsgBoxText(*args))
        _swig_setattr(self, MsgBoxText, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_MsgBoxText):
        try:
            if self.thisown: destroy(self)
        except: pass

class MsgBoxTextPtr(MsgBoxText):
    def __init__(self, this):
        _swig_setattr(self, MsgBoxText, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, MsgBoxText, 'thisown', 0)
        _swig_setattr(self, MsgBoxText,self.__class__,MsgBoxText)
_compatlayer.MsgBoxText_swigregister(MsgBoxTextPtr)

class TListViewer(TView):
    __swig_setmethods__ = {}
    for _s in [TView]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TListViewer, name, value)
    __swig_getmethods__ = {}
    for _s in [TView]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TListViewer, name)
    def __repr__(self):
        return "<C TListViewer instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TListViewer, 'this', _compatlayer.new_TListViewer(*args))
        _swig_setattr(self, TListViewer, 'thisown', 1)
    def changeBounds(*args): return _compatlayer.TListViewer_changeBounds(*args)
    def draw(*args): return _compatlayer.TListViewer_draw(*args)
    def focusItem(*args): return _compatlayer.TListViewer_focusItem(*args)
    def getPalette(*args): return _compatlayer.TListViewer_getPalette(*args)
    def getText(*args): return _compatlayer.TListViewer_getText(*args)
    def isSelected(*args): return _compatlayer.TListViewer_isSelected(*args)
    def handleEvent(*args): return _compatlayer.TListViewer_handleEvent(*args)
    def selectItem(*args): return _compatlayer.TListViewer_selectItem(*args)
    def setRange(*args): return _compatlayer.TListViewer_setRange(*args)
    def setState(*args): return _compatlayer.TListViewer_setState(*args)
    def focusItemNum(*args): return _compatlayer.TListViewer_focusItemNum(*args)
    def shutDown(*args): return _compatlayer.TListViewer_shutDown(*args)
    __swig_setmethods__["hScrollBar"] = _compatlayer.TListViewer_hScrollBar_set
    __swig_getmethods__["hScrollBar"] = _compatlayer.TListViewer_hScrollBar_get
    if _newclass:hScrollBar = property(_compatlayer.TListViewer_hScrollBar_get, _compatlayer.TListViewer_hScrollBar_set)
    __swig_setmethods__["vScrollBar"] = _compatlayer.TListViewer_vScrollBar_set
    __swig_getmethods__["vScrollBar"] = _compatlayer.TListViewer_vScrollBar_get
    if _newclass:vScrollBar = property(_compatlayer.TListViewer_vScrollBar_get, _compatlayer.TListViewer_vScrollBar_set)
    __swig_setmethods__["numCols"] = _compatlayer.TListViewer_numCols_set
    __swig_getmethods__["numCols"] = _compatlayer.TListViewer_numCols_get
    if _newclass:numCols = property(_compatlayer.TListViewer_numCols_get, _compatlayer.TListViewer_numCols_set)
    __swig_setmethods__["topItem"] = _compatlayer.TListViewer_topItem_set
    __swig_getmethods__["topItem"] = _compatlayer.TListViewer_topItem_get
    if _newclass:topItem = property(_compatlayer.TListViewer_topItem_get, _compatlayer.TListViewer_topItem_set)
    __swig_setmethods__["focused"] = _compatlayer.TListViewer_focused_set
    __swig_getmethods__["focused"] = _compatlayer.TListViewer_focused_get
    if _newclass:focused = property(_compatlayer.TListViewer_focused_get, _compatlayer.TListViewer_focused_set)
    __swig_setmethods__["range"] = _compatlayer.TListViewer_range_set
    __swig_getmethods__["range"] = _compatlayer.TListViewer_range_get
    if _newclass:range = property(_compatlayer.TListViewer_range_get, _compatlayer.TListViewer_range_set)
    __swig_setmethods__["handleSpace"] = _compatlayer.TListViewer_handleSpace_set
    __swig_getmethods__["handleSpace"] = _compatlayer.TListViewer_handleSpace_get
    if _newclass:handleSpace = property(_compatlayer.TListViewer_handleSpace_get, _compatlayer.TListViewer_handleSpace_set)
    def getExtraOptions(*args): return _compatlayer.TListViewer_getExtraOptions(*args)
    def setExtraOptions(*args): return _compatlayer.TListViewer_setExtraOptions(*args)
    def __del__(self, destroy=_compatlayer.delete_TListViewer):
        try:
            if self.thisown: destroy(self)
        except: pass

class TListViewerPtr(TListViewer):
    def __init__(self, this):
        _swig_setattr(self, TListViewer, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TListViewer, 'thisown', 0)
        _swig_setattr(self, TListViewer,self.__class__,TListViewer)
_compatlayer.TListViewer_swigregister(TListViewerPtr)

class TListBoxRec(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TListBoxRec, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TListBoxRec, name)
    def __repr__(self):
        return "<C TListBoxRec instance at %s>" % (self.this,)
    __swig_setmethods__["items"] = _compatlayer.TListBoxRec_items_set
    __swig_getmethods__["items"] = _compatlayer.TListBoxRec_items_get
    if _newclass:items = property(_compatlayer.TListBoxRec_items_get, _compatlayer.TListBoxRec_items_set)
    __swig_setmethods__["selection"] = _compatlayer.TListBoxRec_selection_set
    __swig_getmethods__["selection"] = _compatlayer.TListBoxRec_selection_get
    if _newclass:selection = property(_compatlayer.TListBoxRec_selection_get, _compatlayer.TListBoxRec_selection_set)
    def __init__(self, *args):
        _swig_setattr(self, TListBoxRec, 'this', _compatlayer.new_TListBoxRec(*args))
        _swig_setattr(self, TListBoxRec, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TListBoxRec):
        try:
            if self.thisown: destroy(self)
        except: pass

class TListBoxRecPtr(TListBoxRec):
    def __init__(self, this):
        _swig_setattr(self, TListBoxRec, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TListBoxRec, 'thisown', 0)
        _swig_setattr(self, TListBoxRec,self.__class__,TListBoxRec)
_compatlayer.TListBoxRec_swigregister(TListBoxRecPtr)

class TListBox(TListViewer):
    __swig_setmethods__ = {}
    for _s in [TListViewer]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TListBox, name, value)
    __swig_getmethods__ = {}
    for _s in [TListViewer]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TListBox, name)
    def __repr__(self):
        return "<C TListBox instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TListBox, 'this', _compatlayer.new_TListBox(*args))
        _swig_setattr(self, TListBox, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TListBox):
        try:
            if self.thisown: destroy(self)
        except: pass
    def dataSize(*args): return _compatlayer.TListBox_dataSize(*args)
    def getData(*args): return _compatlayer.TListBox_getData(*args)
    def getText(*args): return _compatlayer.TListBox_getText(*args)
    def newList(*args): return _compatlayer.TListBox_newList(*args)
    def newList(self, p):
        p.thisown = 0
        return _tv.TListBox_newList(self, p)

    def setData(*args): return _compatlayer.TListBox_setData(*args)
    def list(*args): return _compatlayer.TListBox_list(*args)

class TListBoxPtr(TListBox):
    def __init__(self, this):
        _swig_setattr(self, TListBox, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TListBox, 'thisown', 0)
        _swig_setattr(self, TListBox,self.__class__,TListBox)
_compatlayer.TListBox_swigregister(TListBoxPtr)

ufUpdate = _compatlayer.ufUpdate
ufLine = _compatlayer.ufLine
ufView = _compatlayer.ufView
smExtend = _compatlayer.smExtend
smDouble = _compatlayer.smDouble
sfSearchFailed = _compatlayer.sfSearchFailed
cmSave = _compatlayer.cmSave
cmSaveAs = _compatlayer.cmSaveAs
cmFind = _compatlayer.cmFind
cmReplace = _compatlayer.cmReplace
cmSearchAgain = _compatlayer.cmSearchAgain
cmCharLeft = _compatlayer.cmCharLeft
cmCharRight = _compatlayer.cmCharRight
cmWordLeft = _compatlayer.cmWordLeft
cmWordRight = _compatlayer.cmWordRight
cmLineStart = _compatlayer.cmLineStart
cmLineEnd = _compatlayer.cmLineEnd
cmLineUp = _compatlayer.cmLineUp
cmLineDown = _compatlayer.cmLineDown
cmPageUp = _compatlayer.cmPageUp
cmPageDown = _compatlayer.cmPageDown
cmTextStart = _compatlayer.cmTextStart
cmTextEnd = _compatlayer.cmTextEnd
cmNewLine = _compatlayer.cmNewLine
cmBackSpace = _compatlayer.cmBackSpace
cmDelChar = _compatlayer.cmDelChar
cmDelWord = _compatlayer.cmDelWord
cmDelStart = _compatlayer.cmDelStart
cmDelEnd = _compatlayer.cmDelEnd
cmDelLine = _compatlayer.cmDelLine
cmInsMode = _compatlayer.cmInsMode
cmStartSelect = _compatlayer.cmStartSelect
cmHideSelect = _compatlayer.cmHideSelect
cmIndentMode = _compatlayer.cmIndentMode
cmUpdateTitle = _compatlayer.cmUpdateTitle
cmInsertText = _compatlayer.cmInsertText
edOutOfMemory = _compatlayer.edOutOfMemory
edReadError = _compatlayer.edReadError
edWriteError = _compatlayer.edWriteError
edCreateError = _compatlayer.edCreateError
edSaveModify = _compatlayer.edSaveModify
edSaveUntitled = _compatlayer.edSaveUntitled
edSaveAs = _compatlayer.edSaveAs
edFind = _compatlayer.edFind
edSearchFailed = _compatlayer.edSearchFailed
edReplace = _compatlayer.edReplace
edReplacePrompt = _compatlayer.edReplacePrompt
efCaseSensitive = _compatlayer.efCaseSensitive
efWholeWordsOnly = _compatlayer.efWholeWordsOnly
efPromptOnReplace = _compatlayer.efPromptOnReplace
efReplaceAll = _compatlayer.efReplaceAll
efDoReplace = _compatlayer.efDoReplace
efBackupFiles = _compatlayer.efBackupFiles
cmOpen = _compatlayer.cmOpen
cmNew = _compatlayer.cmNew
cmChangeDrct = _compatlayer.cmChangeDrct
cmDosShell = _compatlayer.cmDosShell
cmCalculator = _compatlayer.cmCalculator
cmShowClip = _compatlayer.cmShowClip
cmMacros = _compatlayer.cmMacros

defEditorDialog = _compatlayer.defEditorDialog
class TIndicator(TView):
    __swig_setmethods__ = {}
    for _s in [TView]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TIndicator, name, value)
    __swig_getmethods__ = {}
    for _s in [TView]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TIndicator, name)
    def __repr__(self):
        return "<C TIndicator instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TIndicator, 'this', _compatlayer.new_TIndicator(*args))
        _swig_setattr(self, TIndicator, 'thisown', 1)
    def draw(*args): return _compatlayer.TIndicator_draw(*args)
    def getPalette(*args): return _compatlayer.TIndicator_getPalette(*args)
    def setState(*args): return _compatlayer.TIndicator_setState(*args)
    def setValue(*args): return _compatlayer.TIndicator_setValue(*args)
    def __del__(self, destroy=_compatlayer.delete_TIndicator):
        try:
            if self.thisown: destroy(self)
        except: pass

class TIndicatorPtr(TIndicator):
    def __init__(self, this):
        _swig_setattr(self, TIndicator, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TIndicator, 'thisown', 0)
        _swig_setattr(self, TIndicator,self.__class__,TIndicator)
_compatlayer.TIndicator_swigregister(TIndicatorPtr)
maxLineLength = cvar.maxLineLength

class TEditor(TView):
    __swig_setmethods__ = {}
    for _s in [TView]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TEditor, name, value)
    __swig_getmethods__ = {}
    for _s in [TView]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TEditor, name)
    def __repr__(self):
        return "<C TEditor instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TEditor, 'this', _compatlayer.new_TEditor(*args))
        _swig_setattr(self, TEditor, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TEditor):
        try:
            if self.thisown: destroy(self)
        except: pass
    def shutDown(*args): return _compatlayer.TEditor_shutDown(*args)
    def bufChar(*args): return _compatlayer.TEditor_bufChar(*args)
    def bufPtr(*args): return _compatlayer.TEditor_bufPtr(*args)
    def changeBounds(*args): return _compatlayer.TEditor_changeBounds(*args)
    def convertEvent(*args): return _compatlayer.TEditor_convertEvent(*args)
    def cursorVisible(*args): return _compatlayer.TEditor_cursorVisible(*args)
    def deleteSelect(*args): return _compatlayer.TEditor_deleteSelect(*args)
    def doneBuffer(*args): return _compatlayer.TEditor_doneBuffer(*args)
    def draw(*args): return _compatlayer.TEditor_draw(*args)
    def getPalette(*args): return _compatlayer.TEditor_getPalette(*args)
    def handleEvent(*args): return _compatlayer.TEditor_handleEvent(*args)
    def initBuffer(*args): return _compatlayer.TEditor_initBuffer(*args)
    def insertBuffer(*args): return _compatlayer.TEditor_insertBuffer(*args)
    def insertFrom(*args): return _compatlayer.TEditor_insertFrom(*args)
    def insertText(*args): return _compatlayer.TEditor_insertText(*args)
    def scrollTo(*args): return _compatlayer.TEditor_scrollTo(*args)
    def search(*args): return _compatlayer.TEditor_search(*args)
    def setBufSize(*args): return _compatlayer.TEditor_setBufSize(*args)
    def setCmdState(*args): return _compatlayer.TEditor_setCmdState(*args)
    def setSelect(*args): return _compatlayer.TEditor_setSelect(*args)
    def setState(*args): return _compatlayer.TEditor_setState(*args)
    def trackCursor(*args): return _compatlayer.TEditor_trackCursor(*args)
    def undo(*args): return _compatlayer.TEditor_undo(*args)
    def updateCommands(*args): return _compatlayer.TEditor_updateCommands(*args)
    def valid(*args): return _compatlayer.TEditor_valid(*args)
    def charPos(*args): return _compatlayer.TEditor_charPos(*args)
    def charPtr(*args): return _compatlayer.TEditor_charPtr(*args)
    def clipCopy(*args): return _compatlayer.TEditor_clipCopy(*args)
    def clipCut(*args): return _compatlayer.TEditor_clipCut(*args)
    def clipPaste(*args): return _compatlayer.TEditor_clipPaste(*args)
    def deleteRange(*args): return _compatlayer.TEditor_deleteRange(*args)
    def doUpdate(*args): return _compatlayer.TEditor_doUpdate(*args)
    def doSearchReplace(*args): return _compatlayer.TEditor_doSearchReplace(*args)
    def drawLines(*args): return _compatlayer.TEditor_drawLines(*args)
    def formatLine(*args): return _compatlayer.TEditor_formatLine(*args)
    def find(*args): return _compatlayer.TEditor_find(*args)
    def getMousePtr(*args): return _compatlayer.TEditor_getMousePtr(*args)
    def hasSelection(*args): return _compatlayer.TEditor_hasSelection(*args)
    def hideSelect(*args): return _compatlayer.TEditor_hideSelect(*args)
    def isClipboard(*args): return _compatlayer.TEditor_isClipboard(*args)
    def lineEnd(*args): return _compatlayer.TEditor_lineEnd(*args)
    def lineMove(*args): return _compatlayer.TEditor_lineMove(*args)
    def lineStart(*args): return _compatlayer.TEditor_lineStart(*args)
    def lock(*args): return _compatlayer.TEditor_lock(*args)
    def newLine(*args): return _compatlayer.TEditor_newLine(*args)
    def nextChar(*args): return _compatlayer.TEditor_nextChar(*args)
    def nextLine(*args): return _compatlayer.TEditor_nextLine(*args)
    def nextWord(*args): return _compatlayer.TEditor_nextWord(*args)
    def prevChar(*args): return _compatlayer.TEditor_prevChar(*args)
    def prevLine(*args): return _compatlayer.TEditor_prevLine(*args)
    def prevWord(*args): return _compatlayer.TEditor_prevWord(*args)
    def replace(*args): return _compatlayer.TEditor_replace(*args)
    def setBufLen(*args): return _compatlayer.TEditor_setBufLen(*args)
    def setCurPtr(*args): return _compatlayer.TEditor_setCurPtr(*args)
    def startSelect(*args): return _compatlayer.TEditor_startSelect(*args)
    def toggleInsMode(*args): return _compatlayer.TEditor_toggleInsMode(*args)
    def unlock(*args): return _compatlayer.TEditor_unlock(*args)
    def update(*args): return _compatlayer.TEditor_update(*args)
    def checkScrollBar(*args): return _compatlayer.TEditor_checkScrollBar(*args)
    __swig_setmethods__["hScrollBar"] = _compatlayer.TEditor_hScrollBar_set
    __swig_getmethods__["hScrollBar"] = _compatlayer.TEditor_hScrollBar_get
    if _newclass:hScrollBar = property(_compatlayer.TEditor_hScrollBar_get, _compatlayer.TEditor_hScrollBar_set)
    __swig_setmethods__["vScrollBar"] = _compatlayer.TEditor_vScrollBar_set
    __swig_getmethods__["vScrollBar"] = _compatlayer.TEditor_vScrollBar_get
    if _newclass:vScrollBar = property(_compatlayer.TEditor_vScrollBar_get, _compatlayer.TEditor_vScrollBar_set)
    __swig_setmethods__["indicator"] = _compatlayer.TEditor_indicator_set
    __swig_getmethods__["indicator"] = _compatlayer.TEditor_indicator_get
    if _newclass:indicator = property(_compatlayer.TEditor_indicator_get, _compatlayer.TEditor_indicator_set)
    __swig_setmethods__["buffer"] = _compatlayer.TEditor_buffer_set
    __swig_getmethods__["buffer"] = _compatlayer.TEditor_buffer_get
    if _newclass:buffer = property(_compatlayer.TEditor_buffer_get, _compatlayer.TEditor_buffer_set)
    __swig_setmethods__["bufSize"] = _compatlayer.TEditor_bufSize_set
    __swig_getmethods__["bufSize"] = _compatlayer.TEditor_bufSize_get
    if _newclass:bufSize = property(_compatlayer.TEditor_bufSize_get, _compatlayer.TEditor_bufSize_set)
    __swig_setmethods__["bufLen"] = _compatlayer.TEditor_bufLen_set
    __swig_getmethods__["bufLen"] = _compatlayer.TEditor_bufLen_get
    if _newclass:bufLen = property(_compatlayer.TEditor_bufLen_get, _compatlayer.TEditor_bufLen_set)
    __swig_setmethods__["gapLen"] = _compatlayer.TEditor_gapLen_set
    __swig_getmethods__["gapLen"] = _compatlayer.TEditor_gapLen_get
    if _newclass:gapLen = property(_compatlayer.TEditor_gapLen_get, _compatlayer.TEditor_gapLen_set)
    __swig_setmethods__["selStart"] = _compatlayer.TEditor_selStart_set
    __swig_getmethods__["selStart"] = _compatlayer.TEditor_selStart_get
    if _newclass:selStart = property(_compatlayer.TEditor_selStart_get, _compatlayer.TEditor_selStart_set)
    __swig_setmethods__["selEnd"] = _compatlayer.TEditor_selEnd_set
    __swig_getmethods__["selEnd"] = _compatlayer.TEditor_selEnd_get
    if _newclass:selEnd = property(_compatlayer.TEditor_selEnd_get, _compatlayer.TEditor_selEnd_set)
    __swig_setmethods__["curPtr"] = _compatlayer.TEditor_curPtr_set
    __swig_getmethods__["curPtr"] = _compatlayer.TEditor_curPtr_get
    if _newclass:curPtr = property(_compatlayer.TEditor_curPtr_get, _compatlayer.TEditor_curPtr_set)
    __swig_setmethods__["curPos"] = _compatlayer.TEditor_curPos_set
    __swig_getmethods__["curPos"] = _compatlayer.TEditor_curPos_get
    if _newclass:curPos = property(_compatlayer.TEditor_curPos_get, _compatlayer.TEditor_curPos_set)
    __swig_setmethods__["delta"] = _compatlayer.TEditor_delta_set
    __swig_getmethods__["delta"] = _compatlayer.TEditor_delta_get
    if _newclass:delta = property(_compatlayer.TEditor_delta_get, _compatlayer.TEditor_delta_set)
    __swig_setmethods__["limit"] = _compatlayer.TEditor_limit_set
    __swig_getmethods__["limit"] = _compatlayer.TEditor_limit_get
    if _newclass:limit = property(_compatlayer.TEditor_limit_get, _compatlayer.TEditor_limit_set)
    __swig_setmethods__["drawLine"] = _compatlayer.TEditor_drawLine_set
    __swig_getmethods__["drawLine"] = _compatlayer.TEditor_drawLine_get
    if _newclass:drawLine = property(_compatlayer.TEditor_drawLine_get, _compatlayer.TEditor_drawLine_set)
    __swig_setmethods__["drawPtr"] = _compatlayer.TEditor_drawPtr_set
    __swig_getmethods__["drawPtr"] = _compatlayer.TEditor_drawPtr_get
    if _newclass:drawPtr = property(_compatlayer.TEditor_drawPtr_get, _compatlayer.TEditor_drawPtr_set)
    __swig_setmethods__["delCount"] = _compatlayer.TEditor_delCount_set
    __swig_getmethods__["delCount"] = _compatlayer.TEditor_delCount_get
    if _newclass:delCount = property(_compatlayer.TEditor_delCount_get, _compatlayer.TEditor_delCount_set)
    __swig_setmethods__["insCount"] = _compatlayer.TEditor_insCount_set
    __swig_getmethods__["insCount"] = _compatlayer.TEditor_insCount_get
    if _newclass:insCount = property(_compatlayer.TEditor_insCount_get, _compatlayer.TEditor_insCount_set)
    __swig_setmethods__["isValid"] = _compatlayer.TEditor_isValid_set
    __swig_getmethods__["isValid"] = _compatlayer.TEditor_isValid_get
    if _newclass:isValid = property(_compatlayer.TEditor_isValid_get, _compatlayer.TEditor_isValid_set)
    __swig_setmethods__["canUndo"] = _compatlayer.TEditor_canUndo_set
    __swig_getmethods__["canUndo"] = _compatlayer.TEditor_canUndo_get
    if _newclass:canUndo = property(_compatlayer.TEditor_canUndo_get, _compatlayer.TEditor_canUndo_set)
    __swig_setmethods__["modified"] = _compatlayer.TEditor_modified_set
    __swig_getmethods__["modified"] = _compatlayer.TEditor_modified_get
    if _newclass:modified = property(_compatlayer.TEditor_modified_get, _compatlayer.TEditor_modified_set)
    __swig_setmethods__["selecting"] = _compatlayer.TEditor_selecting_set
    __swig_getmethods__["selecting"] = _compatlayer.TEditor_selecting_get
    if _newclass:selecting = property(_compatlayer.TEditor_selecting_get, _compatlayer.TEditor_selecting_set)
    __swig_setmethods__["overwrite"] = _compatlayer.TEditor_overwrite_set
    __swig_getmethods__["overwrite"] = _compatlayer.TEditor_overwrite_get
    if _newclass:overwrite = property(_compatlayer.TEditor_overwrite_get, _compatlayer.TEditor_overwrite_set)
    __swig_setmethods__["autoIndent"] = _compatlayer.TEditor_autoIndent_set
    __swig_getmethods__["autoIndent"] = _compatlayer.TEditor_autoIndent_get
    if _newclass:autoIndent = property(_compatlayer.TEditor_autoIndent_get, _compatlayer.TEditor_autoIndent_set)
    __swig_setmethods__["lockCount"] = _compatlayer.TEditor_lockCount_set
    __swig_getmethods__["lockCount"] = _compatlayer.TEditor_lockCount_get
    if _newclass:lockCount = property(_compatlayer.TEditor_lockCount_get, _compatlayer.TEditor_lockCount_set)
    __swig_setmethods__["updateFlags"] = _compatlayer.TEditor_updateFlags_set
    __swig_getmethods__["updateFlags"] = _compatlayer.TEditor_updateFlags_get
    if _newclass:updateFlags = property(_compatlayer.TEditor_updateFlags_get, _compatlayer.TEditor_updateFlags_set)
    __swig_setmethods__["keyState"] = _compatlayer.TEditor_keyState_set
    __swig_getmethods__["keyState"] = _compatlayer.TEditor_keyState_get
    if _newclass:keyState = property(_compatlayer.TEditor_keyState_get, _compatlayer.TEditor_keyState_set)

class TEditorPtr(TEditor):
    def __init__(self, this):
        _swig_setattr(self, TEditor, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TEditor, 'thisown', 0)
        _swig_setattr(self, TEditor,self.__class__,TEditor)
_compatlayer.TEditor_swigregister(TEditorPtr)

class TMemoData(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TMemoData, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TMemoData, name)
    def __repr__(self):
        return "<C TMemoData instance at %s>" % (self.this,)
    __swig_setmethods__["length"] = _compatlayer.TMemoData_length_set
    __swig_getmethods__["length"] = _compatlayer.TMemoData_length_get
    if _newclass:length = property(_compatlayer.TMemoData_length_get, _compatlayer.TMemoData_length_set)
    __swig_setmethods__["buffer"] = _compatlayer.TMemoData_buffer_set
    __swig_getmethods__["buffer"] = _compatlayer.TMemoData_buffer_get
    if _newclass:buffer = property(_compatlayer.TMemoData_buffer_get, _compatlayer.TMemoData_buffer_set)
    def __init__(self, *args):
        _swig_setattr(self, TMemoData, 'this', _compatlayer.new_TMemoData(*args))
        _swig_setattr(self, TMemoData, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TMemoData):
        try:
            if self.thisown: destroy(self)
        except: pass

class TMemoDataPtr(TMemoData):
    def __init__(self, this):
        _swig_setattr(self, TMemoData, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TMemoData, 'thisown', 0)
        _swig_setattr(self, TMemoData,self.__class__,TMemoData)
_compatlayer.TMemoData_swigregister(TMemoDataPtr)

class TMemo(TEditor):
    __swig_setmethods__ = {}
    for _s in [TEditor]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TMemo, name, value)
    __swig_getmethods__ = {}
    for _s in [TEditor]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TMemo, name)
    def __repr__(self):
        return "<C TMemo instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TMemo, 'this', _compatlayer.new_TMemo(*args))
        _swig_setattr(self, TMemo, 'thisown', 1)
    def getData(*args): return _compatlayer.TMemo_getData(*args)
    def setData(*args): return _compatlayer.TMemo_setData(*args)
    def dataSize(*args): return _compatlayer.TMemo_dataSize(*args)
    def getPalette(*args): return _compatlayer.TMemo_getPalette(*args)
    def handleEvent(*args): return _compatlayer.TMemo_handleEvent(*args)
    def __del__(self, destroy=_compatlayer.delete_TMemo):
        try:
            if self.thisown: destroy(self)
        except: pass

class TMemoPtr(TMemo):
    def __init__(self, this):
        _swig_setattr(self, TMemo, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TMemo, 'thisown', 0)
        _swig_setattr(self, TMemo,self.__class__,TMemo)
_compatlayer.TMemo_swigregister(TMemoPtr)

class TFileEditor(TEditor):
    __swig_setmethods__ = {}
    for _s in [TEditor]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TFileEditor, name, value)
    __swig_getmethods__ = {}
    for _s in [TEditor]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TFileEditor, name)
    def __repr__(self):
        return "<C TFileEditor instance at %s>" % (self.this,)
    __swig_setmethods__["fileName"] = _compatlayer.TFileEditor_fileName_set
    __swig_getmethods__["fileName"] = _compatlayer.TFileEditor_fileName_get
    if _newclass:fileName = property(_compatlayer.TFileEditor_fileName_get, _compatlayer.TFileEditor_fileName_set)
    def __init__(self, *args):
        _swig_setattr(self, TFileEditor, 'this', _compatlayer.new_TFileEditor(*args))
        _swig_setattr(self, TFileEditor, 'thisown', 1)
    def doneBuffer(*args): return _compatlayer.TFileEditor_doneBuffer(*args)
    def handleEvent(*args): return _compatlayer.TFileEditor_handleEvent(*args)
    def initBuffer(*args): return _compatlayer.TFileEditor_initBuffer(*args)
    def loadFile(*args): return _compatlayer.TFileEditor_loadFile(*args)
    def save(*args): return _compatlayer.TFileEditor_save(*args)
    def saveAs(*args): return _compatlayer.TFileEditor_saveAs(*args)
    def saveFile(*args): return _compatlayer.TFileEditor_saveFile(*args)
    def setBufSize(*args): return _compatlayer.TFileEditor_setBufSize(*args)
    def shutDown(*args): return _compatlayer.TFileEditor_shutDown(*args)
    def updateCommands(*args): return _compatlayer.TFileEditor_updateCommands(*args)
    def valid(*args): return _compatlayer.TFileEditor_valid(*args)
    def __del__(self, destroy=_compatlayer.delete_TFileEditor):
        try:
            if self.thisown: destroy(self)
        except: pass

class TFileEditorPtr(TFileEditor):
    def __init__(self, this):
        _swig_setattr(self, TFileEditor, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TFileEditor, 'thisown', 0)
        _swig_setattr(self, TFileEditor,self.__class__,TFileEditor)
_compatlayer.TFileEditor_swigregister(TFileEditorPtr)

class TEditWindow(TWindow):
    __swig_setmethods__ = {}
    for _s in [TWindow]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TEditWindow, name, value)
    __swig_getmethods__ = {}
    for _s in [TWindow]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TEditWindow, name)
    def __repr__(self):
        return "<C TEditWindow instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TEditWindow, 'this', _compatlayer.new_TEditWindow(*args))
        _swig_setattr(self, TEditWindow, 'thisown', 1)
    def close(*args): return _compatlayer.TEditWindow_close(*args)
    def getTitle(*args): return _compatlayer.TEditWindow_getTitle(*args)
    def handleEvent(*args): return _compatlayer.TEditWindow_handleEvent(*args)
    def sizeLimits(*args): return _compatlayer.TEditWindow_sizeLimits(*args)
    __swig_setmethods__["editor"] = _compatlayer.TEditWindow_editor_set
    __swig_getmethods__["editor"] = _compatlayer.TEditWindow_editor_get
    if _newclass:editor = property(_compatlayer.TEditWindow_editor_get, _compatlayer.TEditWindow_editor_set)
    def __del__(self, destroy=_compatlayer.delete_TEditWindow):
        try:
            if self.thisown: destroy(self)
        except: pass

class TEditWindowPtr(TEditWindow):
    def __init__(self, this):
        _swig_setattr(self, TEditWindow, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TEditWindow, 'thisown', 0)
        _swig_setattr(self, TEditWindow,self.__class__,TEditWindow)
_compatlayer.TEditWindow_swigregister(TEditWindowPtr)

class TFindDialogRec(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TFindDialogRec, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TFindDialogRec, name)
    def __repr__(self):
        return "<C TFindDialogRec instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TFindDialogRec, 'this', _compatlayer.new_TFindDialogRec(*args))
        _swig_setattr(self, TFindDialogRec, 'thisown', 1)
    __swig_setmethods__["find"] = _compatlayer.TFindDialogRec_find_set
    __swig_getmethods__["find"] = _compatlayer.TFindDialogRec_find_get
    if _newclass:find = property(_compatlayer.TFindDialogRec_find_get, _compatlayer.TFindDialogRec_find_set)
    __swig_setmethods__["options"] = _compatlayer.TFindDialogRec_options_set
    __swig_getmethods__["options"] = _compatlayer.TFindDialogRec_options_get
    if _newclass:options = property(_compatlayer.TFindDialogRec_options_get, _compatlayer.TFindDialogRec_options_set)
    def __del__(self, destroy=_compatlayer.delete_TFindDialogRec):
        try:
            if self.thisown: destroy(self)
        except: pass

class TFindDialogRecPtr(TFindDialogRec):
    def __init__(self, this):
        _swig_setattr(self, TFindDialogRec, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TFindDialogRec, 'thisown', 0)
        _swig_setattr(self, TFindDialogRec,self.__class__,TFindDialogRec)
_compatlayer.TFindDialogRec_swigregister(TFindDialogRecPtr)

class TReplaceDialogRec(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TReplaceDialogRec, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TReplaceDialogRec, name)
    def __repr__(self):
        return "<C TReplaceDialogRec instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TReplaceDialogRec, 'this', _compatlayer.new_TReplaceDialogRec(*args))
        _swig_setattr(self, TReplaceDialogRec, 'thisown', 1)
    __swig_setmethods__["find"] = _compatlayer.TReplaceDialogRec_find_set
    __swig_getmethods__["find"] = _compatlayer.TReplaceDialogRec_find_get
    if _newclass:find = property(_compatlayer.TReplaceDialogRec_find_get, _compatlayer.TReplaceDialogRec_find_set)
    __swig_setmethods__["replace"] = _compatlayer.TReplaceDialogRec_replace_set
    __swig_getmethods__["replace"] = _compatlayer.TReplaceDialogRec_replace_get
    if _newclass:replace = property(_compatlayer.TReplaceDialogRec_replace_get, _compatlayer.TReplaceDialogRec_replace_set)
    __swig_setmethods__["options"] = _compatlayer.TReplaceDialogRec_options_set
    __swig_getmethods__["options"] = _compatlayer.TReplaceDialogRec_options_get
    if _newclass:options = property(_compatlayer.TReplaceDialogRec_options_get, _compatlayer.TReplaceDialogRec_options_set)
    def __del__(self, destroy=_compatlayer.delete_TReplaceDialogRec):
        try:
            if self.thisown: destroy(self)
        except: pass

class TReplaceDialogRecPtr(TReplaceDialogRec):
    def __init__(self, this):
        _swig_setattr(self, TReplaceDialogRec, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TReplaceDialogRec, 'thisown', 0)
        _swig_setattr(self, TReplaceDialogRec,self.__class__,TReplaceDialogRec)
_compatlayer.TReplaceDialogRec_swigregister(TReplaceDialogRecPtr)

cmFileOpen = _compatlayer.cmFileOpen
cmFileReplace = _compatlayer.cmFileReplace
cmFileClear = _compatlayer.cmFileClear
cmFileInit = _compatlayer.cmFileInit
cmChangeDir = _compatlayer.cmChangeDir
cmRevert = _compatlayer.cmRevert
cmFileSelect = _compatlayer.cmFileSelect
cmDirSelection = _compatlayer.cmDirSelection
cmFileFocused = _compatlayer.cmFileFocused
cmFileDoubleClicked = _compatlayer.cmFileDoubleClicked
class TMethodHolder(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TMethodHolder, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TMethodHolder, name)
    def __repr__(self):
        return "<C TMethodHolder instance at %s>" % (self.this,)
    def initStatusLine(*args): return _compatlayer.TMethodHolder_initStatusLine(*args)
    def initMenuBar(*args): return _compatlayer.TMethodHolder_initMenuBar(*args)
    def initDeskTop(*args): return _compatlayer.TMethodHolder_initDeskTop(*args)
    def __del__(self, destroy=_compatlayer.delete_TMethodHolder):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __init__(self, *args):
        _swig_setattr(self, TMethodHolder, 'this', _compatlayer.new_TMethodHolder(*args))
        _swig_setattr(self, TMethodHolder, 'thisown', 1)

class TMethodHolderPtr(TMethodHolder):
    def __init__(self, this):
        _swig_setattr(self, TMethodHolder, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TMethodHolder, 'thisown', 0)
        _swig_setattr(self, TMethodHolder,self.__class__,TMethodHolder)
_compatlayer.TMethodHolder_swigregister(TMethodHolderPtr)

class TAppWrapper(TApplication):
    __swig_setmethods__ = {}
    for _s in [TApplication]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TAppWrapper, name, value)
    __swig_getmethods__ = {}
    for _s in [TApplication]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TAppWrapper, name)
    def __repr__(self):
        return "<C TAppWrapper instance at %s>" % (self.this,)
    __swig_getmethods__["_sInitStatusLine"] = lambda x: _compatlayer.TAppWrapper__sInitStatusLine
    if _newclass:_sInitStatusLine = staticmethod(_compatlayer.TAppWrapper__sInitStatusLine)
    __swig_getmethods__["_sInitMenuBar"] = lambda x: _compatlayer.TAppWrapper__sInitMenuBar
    if _newclass:_sInitMenuBar = staticmethod(_compatlayer.TAppWrapper__sInitMenuBar)
    __swig_getmethods__["_sInitDeskTop"] = lambda x: _compatlayer.TAppWrapper__sInitDeskTop
    if _newclass:_sInitDeskTop = staticmethod(_compatlayer.TAppWrapper__sInitDeskTop)
    def __init__(self, *args):
        _swig_setattr(self, TAppWrapper, 'this', _compatlayer.new_TAppWrapper(*args))
        _swig_setattr(self, TAppWrapper, 'thisown', 1)
    def __del__(self, destroy=_compatlayer.delete_TAppWrapper):
        try:
            if self.thisown: destroy(self)
        except: pass

class TAppWrapperPtr(TAppWrapper):
    def __init__(self, this):
        _swig_setattr(self, TAppWrapper, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TAppWrapper, 'thisown', 0)
        _swig_setattr(self, TAppWrapper,self.__class__,TAppWrapper)
_compatlayer.TAppWrapper_swigregister(TAppWrapperPtr)

TAppWrapper__sInitStatusLine = _compatlayer.TAppWrapper__sInitStatusLine

TAppWrapper__sInitMenuBar = _compatlayer.TAppWrapper__sInitMenuBar

TAppWrapper__sInitDeskTop = _compatlayer.TAppWrapper__sInitDeskTop


