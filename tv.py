# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _tv

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


CLY_SizedTypesDefined = _tv.CLY_SizedTypesDefined
streamableInit = _tv.streamableInit
class TObject(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TObject, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TObject, name)
    def __repr__(self):
        return "<C TObject instance at %s>" % (self.this,)
    def __del__(self, destroy=_tv.delete_TObject):
        try:
            if self.thisown: destroy(self)
        except: pass
    __swig_getmethods__["CLY_destroy"] = lambda x: _tv.TObject_CLY_destroy
    if _newclass:CLY_destroy = staticmethod(_tv.TObject_CLY_destroy)
    def shutDown(*args): return _tv.TObject_shutDown(*args)
    def __init__(self, *args):
        _swig_setattr(self, TObject, 'this', _tv.new_TObject(*args))
        _swig_setattr(self, TObject, 'thisown', 1)

class TObjectPtr(TObject):
    def __init__(self, this):
        _swig_setattr(self, TObject, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TObject, 'thisown', 0)
        _swig_setattr(self, TObject,self.__class__,TObject)
_tv.TObject_swigregister(TObjectPtr)
cvar = _tv.cvar
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

TObject_CLY_destroy = _tv.TObject_CLY_destroy

class MouseEventType(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MouseEventType, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MouseEventType, name)
    def __repr__(self):
        return "<C MouseEventType instance at %s>" % (self.this,)
    __swig_setmethods__["buttons"] = _tv.MouseEventType_buttons_set
    __swig_getmethods__["buttons"] = _tv.MouseEventType_buttons_get
    if _newclass:buttons = property(_tv.MouseEventType_buttons_get, _tv.MouseEventType_buttons_set)
    __swig_setmethods__["doubleClick"] = _tv.MouseEventType_doubleClick_set
    __swig_getmethods__["doubleClick"] = _tv.MouseEventType_doubleClick_get
    if _newclass:doubleClick = property(_tv.MouseEventType_doubleClick_get, _tv.MouseEventType_doubleClick_set)
    __swig_setmethods__["where"] = _tv.MouseEventType_where_set
    __swig_getmethods__["where"] = _tv.MouseEventType_where_get
    if _newclass:where = property(_tv.MouseEventType_where_get, _tv.MouseEventType_where_set)
    def __init__(self, *args):
        _swig_setattr(self, MouseEventType, 'this', _tv.new_MouseEventType(*args))
        _swig_setattr(self, MouseEventType, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_MouseEventType):
        try:
            if self.thisown: destroy(self)
        except: pass

class MouseEventTypePtr(MouseEventType):
    def __init__(self, this):
        _swig_setattr(self, MouseEventType, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, MouseEventType, 'thisown', 0)
        _swig_setattr(self, MouseEventType,self.__class__,MouseEventType)
_tv.MouseEventType_swigregister(MouseEventTypePtr)

class THWMouse(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, THWMouse, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, THWMouse, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<C THWMouse instance at %s>" % (self.this,)
    __swig_getmethods__["forceEvent"] = lambda x: _tv.THWMouse_forceEvent
    if _newclass:forceEvent = staticmethod(_tv.THWMouse_forceEvent)

class THWMousePtr(THWMouse):
    def __init__(self, this):
        _swig_setattr(self, THWMouse, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, THWMouse, 'thisown', 0)
        _swig_setattr(self, THWMouse,self.__class__,THWMouse)
_tv.THWMouse_swigregister(THWMousePtr)

THWMouse_forceEvent = _tv.THWMouse_forceEvent

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
        _swig_setattr(self, TMouse, 'this', _tv.new_TMouse(*args))
        _swig_setattr(self, TMouse, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TMouse):
        try:
            if self.thisown: destroy(self)
        except: pass
    __swig_getmethods__["show"] = lambda x: _tv.TMouse_show
    if _newclass:show = staticmethod(_tv.TMouse_show)
    __swig_getmethods__["hide"] = lambda x: _tv.TMouse_hide
    if _newclass:hide = staticmethod(_tv.TMouse_hide)
    __swig_getmethods__["suspend"] = lambda x: _tv.TMouse_suspend
    if _newclass:suspend = staticmethod(_tv.TMouse_suspend)
    __swig_getmethods__["resume"] = lambda x: _tv.TMouse_resume
    if _newclass:resume = staticmethod(_tv.TMouse_resume)
    __swig_getmethods__["setRange"] = lambda x: _tv.TMouse_setRange
    if _newclass:setRange = staticmethod(_tv.TMouse_setRange)
    __swig_getmethods__["getEvent"] = lambda x: _tv.TMouse_getEvent
    if _newclass:getEvent = staticmethod(_tv.TMouse_getEvent)
    __swig_getmethods__["present"] = lambda x: _tv.TMouse_present
    if _newclass:present = staticmethod(_tv.TMouse_present)
    __swig_getmethods__["resetDrawCounter"] = lambda x: _tv.TMouse_resetDrawCounter
    if _newclass:resetDrawCounter = staticmethod(_tv.TMouse_resetDrawCounter)
    __swig_getmethods__["getDrawCounter"] = lambda x: _tv.TMouse_getDrawCounter
    if _newclass:getDrawCounter = staticmethod(_tv.TMouse_getDrawCounter)

class TMousePtr(TMouse):
    def __init__(self, this):
        _swig_setattr(self, TMouse, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TMouse, 'thisown', 0)
        _swig_setattr(self, TMouse,self.__class__,TMouse)
_tv.TMouse_swigregister(TMousePtr)

TMouse_show = _tv.TMouse_show

TMouse_hide = _tv.TMouse_hide

TMouse_suspend = _tv.TMouse_suspend

TMouse_resume = _tv.TMouse_resume

TMouse_setRange = _tv.TMouse_setRange

TMouse_getEvent = _tv.TMouse_getEvent

TMouse_present = _tv.TMouse_present

TMouse_resetDrawCounter = _tv.TMouse_resetDrawCounter

TMouse_getDrawCounter = _tv.TMouse_getDrawCounter

class CharScanType(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CharScanType, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CharScanType, name)
    def __repr__(self):
        return "<C CharScanType instance at %s>" % (self.this,)
    __swig_setmethods__["charCode"] = _tv.CharScanType_charCode_set
    __swig_getmethods__["charCode"] = _tv.CharScanType_charCode_get
    if _newclass:charCode = property(_tv.CharScanType_charCode_get, _tv.CharScanType_charCode_set)
    __swig_setmethods__["scanCode"] = _tv.CharScanType_scanCode_set
    __swig_getmethods__["scanCode"] = _tv.CharScanType_scanCode_get
    if _newclass:scanCode = property(_tv.CharScanType_scanCode_get, _tv.CharScanType_scanCode_set)
    def __init__(self, *args):
        _swig_setattr(self, CharScanType, 'this', _tv.new_CharScanType(*args))
        _swig_setattr(self, CharScanType, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_CharScanType):
        try:
            if self.thisown: destroy(self)
        except: pass

class CharScanTypePtr(CharScanType):
    def __init__(self, this):
        _swig_setattr(self, CharScanType, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, CharScanType, 'thisown', 0)
        _swig_setattr(self, CharScanType,self.__class__,CharScanType)
_tv.CharScanType_swigregister(CharScanTypePtr)

class KeyDownEvent(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, KeyDownEvent, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, KeyDownEvent, name)
    def __repr__(self):
        return "<C KeyDownEvent instance at %s>" % (self.this,)
    __swig_setmethods__["charScan"] = _tv.KeyDownEvent_charScan_set
    __swig_getmethods__["charScan"] = _tv.KeyDownEvent_charScan_get
    if _newclass:charScan = property(_tv.KeyDownEvent_charScan_get, _tv.KeyDownEvent_charScan_set)
    __swig_setmethods__["keyCode"] = _tv.KeyDownEvent_keyCode_set
    __swig_getmethods__["keyCode"] = _tv.KeyDownEvent_keyCode_get
    if _newclass:keyCode = property(_tv.KeyDownEvent_keyCode_get, _tv.KeyDownEvent_keyCode_set)
    __swig_setmethods__["shiftState"] = _tv.KeyDownEvent_shiftState_set
    __swig_getmethods__["shiftState"] = _tv.KeyDownEvent_shiftState_get
    if _newclass:shiftState = property(_tv.KeyDownEvent_shiftState_get, _tv.KeyDownEvent_shiftState_set)
    __swig_setmethods__["raw_scanCode"] = _tv.KeyDownEvent_raw_scanCode_set
    __swig_getmethods__["raw_scanCode"] = _tv.KeyDownEvent_raw_scanCode_get
    if _newclass:raw_scanCode = property(_tv.KeyDownEvent_raw_scanCode_get, _tv.KeyDownEvent_raw_scanCode_set)
    __swig_setmethods__["charCode"] = _tv.KeyDownEvent_charCode_set
    __swig_getmethods__["charCode"] = _tv.KeyDownEvent_charCode_get
    if _newclass:charCode = property(_tv.KeyDownEvent_charCode_get, _tv.KeyDownEvent_charCode_set)
    def __init__(self, *args):
        _swig_setattr(self, KeyDownEvent, 'this', _tv.new_KeyDownEvent(*args))
        _swig_setattr(self, KeyDownEvent, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_KeyDownEvent):
        try:
            if self.thisown: destroy(self)
        except: pass

class KeyDownEventPtr(KeyDownEvent):
    def __init__(self, this):
        _swig_setattr(self, KeyDownEvent, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, KeyDownEvent, 'thisown', 0)
        _swig_setattr(self, KeyDownEvent,self.__class__,KeyDownEvent)
_tv.KeyDownEvent_swigregister(KeyDownEventPtr)

class MessageEvent(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MessageEvent, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MessageEvent, name)
    def __repr__(self):
        return "<C MessageEvent instance at %s>" % (self.this,)
    __swig_setmethods__["command"] = _tv.MessageEvent_command_set
    __swig_getmethods__["command"] = _tv.MessageEvent_command_get
    if _newclass:command = property(_tv.MessageEvent_command_get, _tv.MessageEvent_command_set)
    __swig_setmethods__["infoPtr"] = _tv.MessageEvent_infoPtr_set
    __swig_getmethods__["infoPtr"] = _tv.MessageEvent_infoPtr_get
    if _newclass:infoPtr = property(_tv.MessageEvent_infoPtr_get, _tv.MessageEvent_infoPtr_set)
    __swig_setmethods__["infoLong"] = _tv.MessageEvent_infoLong_set
    __swig_getmethods__["infoLong"] = _tv.MessageEvent_infoLong_get
    if _newclass:infoLong = property(_tv.MessageEvent_infoLong_get, _tv.MessageEvent_infoLong_set)
    __swig_setmethods__["infoWord"] = _tv.MessageEvent_infoWord_set
    __swig_getmethods__["infoWord"] = _tv.MessageEvent_infoWord_get
    if _newclass:infoWord = property(_tv.MessageEvent_infoWord_get, _tv.MessageEvent_infoWord_set)
    __swig_setmethods__["infoInt"] = _tv.MessageEvent_infoInt_set
    __swig_getmethods__["infoInt"] = _tv.MessageEvent_infoInt_get
    if _newclass:infoInt = property(_tv.MessageEvent_infoInt_get, _tv.MessageEvent_infoInt_set)
    __swig_setmethods__["infoByte"] = _tv.MessageEvent_infoByte_set
    __swig_getmethods__["infoByte"] = _tv.MessageEvent_infoByte_get
    if _newclass:infoByte = property(_tv.MessageEvent_infoByte_get, _tv.MessageEvent_infoByte_set)
    __swig_setmethods__["infoChar"] = _tv.MessageEvent_infoChar_set
    __swig_getmethods__["infoChar"] = _tv.MessageEvent_infoChar_get
    if _newclass:infoChar = property(_tv.MessageEvent_infoChar_get, _tv.MessageEvent_infoChar_set)
    def __init__(self, *args):
        _swig_setattr(self, MessageEvent, 'this', _tv.new_MessageEvent(*args))
        _swig_setattr(self, MessageEvent, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_MessageEvent):
        try:
            if self.thisown: destroy(self)
        except: pass

class MessageEventPtr(MessageEvent):
    def __init__(self, this):
        _swig_setattr(self, MessageEvent, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, MessageEvent, 'thisown', 0)
        _swig_setattr(self, MessageEvent,self.__class__,MessageEvent)
_tv.MessageEvent_swigregister(MessageEventPtr)

class TEvent(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TEvent, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TEvent, name)
    def __repr__(self):
        return "<C TEvent instance at %s>" % (self.this,)
    __swig_setmethods__["what"] = _tv.TEvent_what_set
    __swig_getmethods__["what"] = _tv.TEvent_what_get
    if _newclass:what = property(_tv.TEvent_what_get, _tv.TEvent_what_set)
    __swig_setmethods__["mouse"] = _tv.TEvent_mouse_set
    __swig_getmethods__["mouse"] = _tv.TEvent_mouse_get
    if _newclass:mouse = property(_tv.TEvent_mouse_get, _tv.TEvent_mouse_set)
    __swig_setmethods__["keyDown"] = _tv.TEvent_keyDown_set
    __swig_getmethods__["keyDown"] = _tv.TEvent_keyDown_get
    if _newclass:keyDown = property(_tv.TEvent_keyDown_get, _tv.TEvent_keyDown_set)
    __swig_setmethods__["message"] = _tv.TEvent_message_set
    __swig_getmethods__["message"] = _tv.TEvent_message_get
    if _newclass:message = property(_tv.TEvent_message_get, _tv.TEvent_message_set)
    def __init__(self, *args):
        _swig_setattr(self, TEvent, 'this', _tv.new_TEvent(*args))
        _swig_setattr(self, TEvent, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TEvent):
        try:
            if self.thisown: destroy(self)
        except: pass

class TEventPtr(TEvent):
    def __init__(self, this):
        _swig_setattr(self, TEvent, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TEvent, 'thisown', 0)
        _swig_setattr(self, TEvent,self.__class__,TEvent)
_tv.TEvent_swigregister(TEventPtr)

class TStreamable(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TStreamable, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TStreamable, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<C TStreamable instance at %s>" % (self.this,)
    def __del__(self, destroy=_tv.delete_TStreamable):
        try:
            if self.thisown: destroy(self)
        except: pass

class TStreamablePtr(TStreamable):
    def __init__(self, this):
        _swig_setattr(self, TStreamable, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TStreamable, 'thisown', 0)
        _swig_setattr(self, TStreamable,self.__class__,TStreamable)
_tv.TStreamable_swigregister(TStreamablePtr)

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
        _swig_setattr(self, TNSCollection, 'this', _tv.new_TNSCollection(*args))
        _swig_setattr(self, TNSCollection, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TNSCollection):
        try:
            if self.thisown: destroy(self)
        except: pass
    def shutDown(*args): return _tv.TNSCollection_shutDown(*args)
    def at(*args): return _tv.TNSCollection_at(*args)
    def indexOf(*args): return _tv.TNSCollection_indexOf(*args)
    def atFree(*args): return _tv.TNSCollection_atFree(*args)
    def atRemove(*args): return _tv.TNSCollection_atRemove(*args)
    def remove(*args): return _tv.TNSCollection_remove(*args)
    def removeAll(*args): return _tv.TNSCollection_removeAll(*args)
    def free(*args): return _tv.TNSCollection_free(*args)
    def freeAll(*args): return _tv.TNSCollection_freeAll(*args)
    def atInsert(*args): return _tv.TNSCollection_atInsert(*args)
    def atPut(*args): return _tv.TNSCollection_atPut(*args)
    def atReplace(*args): return _tv.TNSCollection_atReplace(*args)
    def insert(*args): return _tv.TNSCollection_insert(*args)
    def insert(self, p):
        p.thisown = 0
        return _tv.TNSCollection_insert(self, p)

    def error(*args): return _tv.TNSCollection_error(*args)
    def firstThat(*args): return _tv.TNSCollection_firstThat(*args)
    def lastThat(*args): return _tv.TNSCollection_lastThat(*args)
    def forEach(*args): return _tv.TNSCollection_forEach(*args)
    def pack(*args): return _tv.TNSCollection_pack(*args)
    def setLimit(*args): return _tv.TNSCollection_setLimit(*args)
    def getCount(*args): return _tv.TNSCollection_getCount(*args)
    def setOwnerShip(*args): return _tv.TNSCollection_setOwnerShip(*args)

class TNSCollectionPtr(TNSCollection):
    def __init__(self, this):
        _swig_setattr(self, TNSCollection, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TNSCollection, 'thisown', 0)
        _swig_setattr(self, TNSCollection,self.__class__,TNSCollection)
_tv.TNSCollection_swigregister(TNSCollectionPtr)

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
    def search(*args): return _tv.TNSSortedCollection_search(*args)
    def indexOf(*args): return _tv.TNSSortedCollection_indexOf(*args)
    def insert(*args): return _tv.TNSSortedCollection_insert(*args)
    __swig_setmethods__["duplicates"] = _tv.TNSSortedCollection_duplicates_set
    __swig_getmethods__["duplicates"] = _tv.TNSSortedCollection_duplicates_get
    if _newclass:duplicates = property(_tv.TNSSortedCollection_duplicates_get, _tv.TNSSortedCollection_duplicates_set)
    def keyOf(*args): return _tv.TNSSortedCollection_keyOf(*args)
    def __del__(self, destroy=_tv.delete_TNSSortedCollection):
        try:
            if self.thisown: destroy(self)
        except: pass

class TNSSortedCollectionPtr(TNSSortedCollection):
    def __init__(self, this):
        _swig_setattr(self, TNSSortedCollection, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TNSSortedCollection, 'thisown', 0)
        _swig_setattr(self, TNSSortedCollection,self.__class__,TNSSortedCollection)
_tv.TNSSortedCollection_swigregister(TNSSortedCollectionPtr)

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
        _swig_setattr(self, TCollection, 'this', _tv.new_TCollection(*args))
        _swig_setattr(self, TCollection, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TCollection):
        try:
            if self.thisown: destroy(self)
        except: pass

class TCollectionPtr(TCollection):
    def __init__(self, this):
        _swig_setattr(self, TCollection, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TCollection, 'thisown', 0)
        _swig_setattr(self, TCollection,self.__class__,TCollection)
_tv.TCollection_swigregister(TCollectionPtr)

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
    def __del__(self, destroy=_tv.delete_TSortedCollection):
        try:
            if self.thisown: destroy(self)
        except: pass

class TSortedCollectionPtr(TSortedCollection):
    def __init__(self, this):
        _swig_setattr(self, TSortedCollection, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TSortedCollection, 'thisown', 0)
        _swig_setattr(self, TSortedCollection,self.__class__,TSortedCollection)
_tv.TSortedCollection_swigregister(TSortedCollectionPtr)

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
        _swig_setattr(self, TStringCollection, 'this', _tv.new_TStringCollection(*args))
        _swig_setattr(self, TStringCollection, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TStringCollection):
        try:
            if self.thisown: destroy(self)
        except: pass

class TStringCollectionPtr(TStringCollection):
    def __init__(self, this):
        _swig_setattr(self, TStringCollection, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TStringCollection, 'thisown', 0)
        _swig_setattr(self, TStringCollection,self.__class__,TStringCollection)
_tv.TStringCollection_swigregister(TStringCollectionPtr)

class TPoint(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TPoint, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TPoint, name)
    def __repr__(self):
        return "<C TPoint instance at %s>" % (self.this,)
    def __iadd__(*args): return _tv.TPoint___iadd__(*args)
    def __isub__(*args): return _tv.TPoint___isub__(*args)
    __swig_setmethods__["x"] = _tv.TPoint_x_set
    __swig_getmethods__["x"] = _tv.TPoint_x_get
    if _newclass:x = property(_tv.TPoint_x_get, _tv.TPoint_x_set)
    __swig_setmethods__["y"] = _tv.TPoint_y_set
    __swig_getmethods__["y"] = _tv.TPoint_y_get
    if _newclass:y = property(_tv.TPoint_y_get, _tv.TPoint_y_set)
    def __init__(self, *args):
        _swig_setattr(self, TPoint, 'this', _tv.new_TPoint(*args))
        _swig_setattr(self, TPoint, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TPoint):
        try:
            if self.thisown: destroy(self)
        except: pass

class TPointPtr(TPoint):
    def __init__(self, this):
        _swig_setattr(self, TPoint, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TPoint, 'thisown', 0)
        _swig_setattr(self, TPoint,self.__class__,TPoint)
_tv.TPoint_swigregister(TPointPtr)

class TRect(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TRect, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TRect, name)
    def __repr__(self):
        return "<C TRect instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TRect, 'this', _tv.new_TRect(*args))
        _swig_setattr(self, TRect, 'thisown', 1)
    def move(*args): return _tv.TRect_move(*args)
    def grow(*args): return _tv.TRect_grow(*args)
    def intersect(*args): return _tv.TRect_intersect(*args)
    def Union(*args): return _tv.TRect_Union(*args)
    def contains(*args): return _tv.TRect_contains(*args)
    def __eq__(*args): return _tv.TRect___eq__(*args)
    def __ne__(*args): return _tv.TRect___ne__(*args)
    def isEmpty(*args): return _tv.TRect_isEmpty(*args)
    __swig_setmethods__["a"] = _tv.TRect_a_set
    __swig_getmethods__["a"] = _tv.TRect_a_get
    if _newclass:a = property(_tv.TRect_a_get, _tv.TRect_a_set)
    __swig_setmethods__["b"] = _tv.TRect_b_set
    __swig_getmethods__["b"] = _tv.TRect_b_get
    if _newclass:b = property(_tv.TRect_b_get, _tv.TRect_b_set)
    def __del__(self, destroy=_tv.delete_TRect):
        try:
            if self.thisown: destroy(self)
        except: pass

class TRectPtr(TRect):
    def __init__(self, this):
        _swig_setattr(self, TRect, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TRect, 'thisown', 0)
        _swig_setattr(self, TRect,self.__class__,TRect)
_tv.TRect_swigregister(TRectPtr)

class TPalette(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TPalette, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TPalette, name)
    def __repr__(self):
        return "<C TPalette instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TPalette, 'this', _tv.new_TPalette(*args))
        _swig_setattr(self, TPalette, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TPalette):
        try:
            if self.thisown: destroy(self)
        except: pass
    __swig_setmethods__["data"] = _tv.TPalette_data_set
    __swig_getmethods__["data"] = _tv.TPalette_data_get
    if _newclass:data = property(_tv.TPalette_data_get, _tv.TPalette_data_set)

class TPalettePtr(TPalette):
    def __init__(self, this):
        _swig_setattr(self, TPalette, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TPalette, 'thisown', 0)
        _swig_setattr(self, TPalette,self.__class__,TPalette)
_tv.TPalette_swigregister(TPalettePtr)

class TCommandSet(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TCommandSet, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TCommandSet, name)
    def __repr__(self):
        return "<C TCommandSet instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TCommandSet, 'this', _tv.new_TCommandSet(*args))
        _swig_setattr(self, TCommandSet, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TCommandSet):
        try:
            if self.thisown: destroy(self)
        except: pass
    def has(*args): return _tv.TCommandSet_has(*args)
    def disableCmdInt(*args): return _tv.TCommandSet_disableCmdInt(*args)
    def disableCmdRange(*args): return _tv.TCommandSet_disableCmdRange(*args)
    def enableCmdInt(*args): return _tv.TCommandSet_enableCmdInt(*args)
    def enableCmdRange(*args): return _tv.TCommandSet_enableCmdRange(*args)
    def enableAllCommands(*args): return _tv.TCommandSet_enableAllCommands(*args)
    def disableCmd(*args): return _tv.TCommandSet_disableCmd(*args)
    def enableCmd(*args): return _tv.TCommandSet_enableCmd(*args)
    def __iadd__(*args): return _tv.TCommandSet___iadd__(*args)
    def __isub__(*args): return _tv.TCommandSet___isub__(*args)
    def isEmpty(*args): return _tv.TCommandSet_isEmpty(*args)
    def set(*args): return _tv.TCommandSet_set(*args)
    def __iand__(*args): return _tv.TCommandSet___iand__(*args)
    def __ior__(*args): return _tv.TCommandSet___ior__(*args)

class TCommandSetPtr(TCommandSet):
    def __init__(self, this):
        _swig_setattr(self, TCommandSet, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TCommandSet, 'thisown', 0)
        _swig_setattr(self, TCommandSet,self.__class__,TCommandSet)
_tv.TCommandSet_swigregister(TCommandSetPtr)

class write_args(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, write_args, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, write_args, name)
    def __repr__(self):
        return "<C write_args instance at %s>" % (self.this,)
    __swig_setmethods__["self"] = _tv.write_args_self_set
    __swig_getmethods__["self"] = _tv.write_args_self_get
    if _newclass:self = property(_tv.write_args_self_get, _tv.write_args_self_set)
    __swig_setmethods__["target"] = _tv.write_args_target_set
    __swig_getmethods__["target"] = _tv.write_args_target_get
    if _newclass:target = property(_tv.write_args_target_get, _tv.write_args_target_set)
    __swig_setmethods__["buf"] = _tv.write_args_buf_set
    __swig_getmethods__["buf"] = _tv.write_args_buf_get
    if _newclass:buf = property(_tv.write_args_buf_get, _tv.write_args_buf_set)
    __swig_setmethods__["offset"] = _tv.write_args_offset_set
    __swig_getmethods__["offset"] = _tv.write_args_offset_get
    if _newclass:offset = property(_tv.write_args_offset_get, _tv.write_args_offset_set)
    def __init__(self, *args):
        _swig_setattr(self, write_args, 'this', _tv.new_write_args(*args))
        _swig_setattr(self, write_args, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_write_args):
        try:
            if self.thisown: destroy(self)
        except: pass

class write_argsPtr(write_args):
    def __init__(self, this):
        _swig_setattr(self, write_args, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, write_args, 'thisown', 0)
        _swig_setattr(self, write_args,self.__class__,write_args)
_tv.write_args_swigregister(write_argsPtr)

class TView(TObject):
    __swig_setmethods__ = {}
    for _s in [TObject]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TView, name, value)
    __swig_getmethods__ = {}
    for _s in [TObject]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TView, name)
    def __repr__(self):
        return "<C TView instance at %s>" % (self.this,)
    phFocused = _tv.TView_phFocused
    phPreProcess = _tv.TView_phPreProcess
    phPostProcess = _tv.TView_phPostProcess
    normalSelect = _tv.TView_normalSelect
    enterSelect = _tv.TView_enterSelect
    leaveSelect = _tv.TView_leaveSelect
    def __init__(self, *args):
        _swig_setattr(self, TView, 'this', _tv.new_TView(*args))
        _swig_setattr(self, TView, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TView):
        try:
            if self.thisown: destroy(self)
        except: pass
    def sizeLimits(*args): return _tv.TView_sizeLimits(*args)
    def getBounds(*args): return _tv.TView_getBounds(*args)
    def getExtent(*args): return _tv.TView_getExtent(*args)
    def getClipRect(*args): return _tv.TView_getClipRect(*args)
    def mouseInView(*args): return _tv.TView_mouseInView(*args)
    def containsMouse(*args): return _tv.TView_containsMouse(*args)
    def locate(*args): return _tv.TView_locate(*args)
    def dragView(*args): return _tv.TView_dragView(*args)
    def calcBounds(*args): return _tv.TView_calcBounds(*args)
    def changeBounds(*args): return _tv.TView_changeBounds(*args)
    def growTo(*args): return _tv.TView_growTo(*args)
    def moveTo(*args): return _tv.TView_moveTo(*args)
    def setBounds(*args): return _tv.TView_setBounds(*args)
    def getHelpCtx(*args): return _tv.TView_getHelpCtx(*args)
    def valid(*args): return _tv.TView_valid(*args)
    def hide(*args): return _tv.TView_hide(*args)
    def show(*args): return _tv.TView_show(*args)
    def draw(*args): return _tv.TView_draw(*args)
    def drawView(*args): return _tv.TView_drawView(*args)
    def exposed(*args): return _tv.TView_exposed(*args)
    def hideCursor(*args): return _tv.TView_hideCursor(*args)
    def drawHide(*args): return _tv.TView_drawHide(*args)
    def drawShow(*args): return _tv.TView_drawShow(*args)
    def drawUnderRect(*args): return _tv.TView_drawUnderRect(*args)
    def drawUnderView(*args): return _tv.TView_drawUnderView(*args)
    def dataSize(*args): return _tv.TView_dataSize(*args)
    def getData(*args): return _tv.TView_getData(*args)
    def setData(*args): return _tv.TView_setData(*args)
    def blockCursor(*args): return _tv.TView_blockCursor(*args)
    def normalCursor(*args): return _tv.TView_normalCursor(*args)
    def resetCursor(*args): return _tv.TView_resetCursor(*args)
    def setCursor(*args): return _tv.TView_setCursor(*args)
    def showCursor(*args): return _tv.TView_showCursor(*args)
    def drawCursor(*args): return _tv.TView_drawCursor(*args)
    def clearEvent(*args): return _tv.TView_clearEvent(*args)
    def eventAvail(*args): return _tv.TView_eventAvail(*args)
    def getEvent(*args): return _tv.TView_getEvent(*args)
    def handleEvent(*args): return _tv.TView_handleEvent(*args)
    def putEvent(*args): return _tv.TView_putEvent(*args)
    __swig_getmethods__["commandEnabled"] = lambda x: _tv.TView_commandEnabled
    if _newclass:commandEnabled = staticmethod(_tv.TView_commandEnabled)
    __swig_getmethods__["disableCommands"] = lambda x: _tv.TView_disableCommands
    if _newclass:disableCommands = staticmethod(_tv.TView_disableCommands)
    __swig_getmethods__["enableCommands"] = lambda x: _tv.TView_enableCommands
    if _newclass:enableCommands = staticmethod(_tv.TView_enableCommands)
    __swig_getmethods__["disableCommand"] = lambda x: _tv.TView_disableCommand
    if _newclass:disableCommand = staticmethod(_tv.TView_disableCommand)
    __swig_getmethods__["enableCommand"] = lambda x: _tv.TView_enableCommand
    if _newclass:enableCommand = staticmethod(_tv.TView_enableCommand)
    __swig_getmethods__["getCommands"] = lambda x: _tv.TView_getCommands
    if _newclass:getCommands = staticmethod(_tv.TView_getCommands)
    __swig_getmethods__["setCommands"] = lambda x: _tv.TView_setCommands
    if _newclass:setCommands = staticmethod(_tv.TView_setCommands)
    def endModal(*args): return _tv.TView_endModal(*args)
    def execute(*args): return _tv.TView_execute(*args)
    def getColor(*args): return _tv.TView_getColor(*args)
    def getPalette(*args): return _tv.TView_getPalette(*args)
    def mapColor(*args): return _tv.TView_mapColor(*args)
    def getState(*args): return _tv.TView_getState(*args)
    def select(*args): return _tv.TView_select(*args)
    def setState(*args): return _tv.TView_setState(*args)
    def keyEvent(*args): return _tv.TView_keyEvent(*args)
    def mouseEvent(*args): return _tv.TView_mouseEvent(*args)
    def makeGlobal(*args): return _tv.TView_makeGlobal(*args)
    def makeLocal(*args): return _tv.TView_makeLocal(*args)
    def nextView(*args): return _tv.TView_nextView(*args)
    def prevView(*args): return _tv.TView_prevView(*args)
    def prev(*args): return _tv.TView_prev(*args)
    __swig_setmethods__["next"] = _tv.TView_next_set
    __swig_getmethods__["next"] = _tv.TView_next_get
    if _newclass:next = property(_tv.TView_next_get, _tv.TView_next_set)
    def makeFirst(*args): return _tv.TView_makeFirst(*args)
    def putInFrontOf(*args): return _tv.TView_putInFrontOf(*args)
    def TopView(*args): return _tv.TView_TopView(*args)
    def writeBuf(*args): return _tv.TView_writeBuf(*args)
    def writeNativeBuf(*args): return _tv.TView_writeNativeBuf(*args)
    def writeLine(*args): return _tv.TView_writeLine(*args)
    def writeNativeLine(*args): return _tv.TView_writeNativeLine(*args)
    def writeChar(*args): return _tv.TView_writeChar(*args)
    def writeCharU16(*args): return _tv.TView_writeCharU16(*args)
    def writeStr(*args): return _tv.TView_writeStr(*args)
    def writeStrU16(*args): return _tv.TView_writeStrU16(*args)
    __swig_setmethods__["size"] = _tv.TView_size_set
    __swig_getmethods__["size"] = _tv.TView_size_get
    if _newclass:size = property(_tv.TView_size_get, _tv.TView_size_set)
    __swig_setmethods__["options"] = _tv.TView_options_set
    __swig_getmethods__["options"] = _tv.TView_options_get
    if _newclass:options = property(_tv.TView_options_get, _tv.TView_options_set)
    __swig_setmethods__["eventMask"] = _tv.TView_eventMask_set
    __swig_getmethods__["eventMask"] = _tv.TView_eventMask_get
    if _newclass:eventMask = property(_tv.TView_eventMask_get, _tv.TView_eventMask_set)
    __swig_setmethods__["state"] = _tv.TView_state_set
    __swig_getmethods__["state"] = _tv.TView_state_get
    if _newclass:state = property(_tv.TView_state_get, _tv.TView_state_set)
    __swig_setmethods__["origin"] = _tv.TView_origin_set
    __swig_getmethods__["origin"] = _tv.TView_origin_get
    if _newclass:origin = property(_tv.TView_origin_get, _tv.TView_origin_set)
    __swig_setmethods__["cursor"] = _tv.TView_cursor_set
    __swig_getmethods__["cursor"] = _tv.TView_cursor_get
    if _newclass:cursor = property(_tv.TView_cursor_get, _tv.TView_cursor_set)
    __swig_setmethods__["growMode"] = _tv.TView_growMode_set
    __swig_getmethods__["growMode"] = _tv.TView_growMode_get
    if _newclass:growMode = property(_tv.TView_growMode_get, _tv.TView_growMode_set)
    __swig_setmethods__["dragMode"] = _tv.TView_dragMode_set
    __swig_getmethods__["dragMode"] = _tv.TView_dragMode_get
    if _newclass:dragMode = property(_tv.TView_dragMode_get, _tv.TView_dragMode_set)
    __swig_setmethods__["helpCtx"] = _tv.TView_helpCtx_set
    __swig_getmethods__["helpCtx"] = _tv.TView_helpCtx_get
    if _newclass:helpCtx = property(_tv.TView_helpCtx_get, _tv.TView_helpCtx_set)
    __swig_setmethods__["owner"] = _tv.TView_owner_set
    __swig_getmethods__["owner"] = _tv.TView_owner_get
    if _newclass:owner = property(_tv.TView_owner_get, _tv.TView_owner_set)
    def shutDown(*args): return _tv.TView_shutDown(*args)

class TViewPtr(TView):
    def __init__(self, this):
        _swig_setattr(self, TView, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TView, 'thisown', 0)
        _swig_setattr(self, TView,self.__class__,TView)
_tv.TView_swigregister(TViewPtr)

TView_commandEnabled = _tv.TView_commandEnabled

TView_disableCommands = _tv.TView_disableCommands

TView_enableCommands = _tv.TView_enableCommands

TView_disableCommand = _tv.TView_disableCommand

TView_enableCommand = _tv.TView_enableCommand

TView_getCommands = _tv.TView_getCommands

TView_setCommands = _tv.TView_setCommands

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
        _swig_setattr(self, TGroup, 'this', _tv.new_TGroup(*args))
        _swig_setattr(self, TGroup, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TGroup):
        try:
            if self.thisown: destroy(self)
        except: pass
    def shutDown(*args): return _tv.TGroup_shutDown(*args)
    def execView(*args): return _tv.TGroup_execView(*args)
    def execute(*args): return _tv.TGroup_execute(*args)
    def insertView(*args): return _tv.TGroup_insertView(*args)
    def remove(*args): return _tv.TGroup_remove(*args)
    def removeView(*args): return _tv.TGroup_removeView(*args)
    def resetCurrent(*args): return _tv.TGroup_resetCurrent(*args)
    def setCurrent(*args): return _tv.TGroup_setCurrent(*args)
    def selectNext(*args): return _tv.TGroup_selectNext(*args)
    def firstThat(*args): return _tv.TGroup_firstThat(*args)
    def forEach(*args): return _tv.TGroup_forEach(*args)
    def insert(*args): return _tv.TGroup_insert(*args)
    def insert(self, p):
        p.thisown = 0
        return _tv.TGroup_insert(self, p)

    def insertBefore(*args): return _tv.TGroup_insertBefore(*args)
    def insertBefore(self, p):
        p.thisown = 0
        return _tv.TGroup_insertBefore(self, p)

    __swig_setmethods__["current"] = _tv.TGroup_current_set
    __swig_getmethods__["current"] = _tv.TGroup_current_get
    if _newclass:current = property(_tv.TGroup_current_get, _tv.TGroup_current_set)
    def at(*args): return _tv.TGroup_at(*args)
    def firstMatch(*args): return _tv.TGroup_firstMatch(*args)
    def indexOf(*args): return _tv.TGroup_indexOf(*args)
    def first(*args): return _tv.TGroup_first(*args)
    def setState(*args): return _tv.TGroup_setState(*args)
    def handleEvent(*args): return _tv.TGroup_handleEvent(*args)
    def drawSubViews(*args): return _tv.TGroup_drawSubViews(*args)
    def changeBounds(*args): return _tv.TGroup_changeBounds(*args)
    def dataSize(*args): return _tv.TGroup_dataSize(*args)
    def getData(*args): return _tv.TGroup_getData(*args)
    def setData(*args): return _tv.TGroup_setData(*args)
    def draw(*args): return _tv.TGroup_draw(*args)
    def redraw(*args): return _tv.TGroup_redraw(*args)
    def Redraw(*args): return _tv.TGroup_Redraw(*args)
    def lock(*args): return _tv.TGroup_lock(*args)
    def unlock(*args): return _tv.TGroup_unlock(*args)
    def resetCursor(*args): return _tv.TGroup_resetCursor(*args)
    def canShowCursor(*args): return _tv.TGroup_canShowCursor(*args)
    def endModal(*args): return _tv.TGroup_endModal(*args)
    def eventError(*args): return _tv.TGroup_eventError(*args)
    def getHelpCtx(*args): return _tv.TGroup_getHelpCtx(*args)
    def valid(*args): return _tv.TGroup_valid(*args)
    def freeBuffer(*args): return _tv.TGroup_freeBuffer(*args)
    def getBuffer(*args): return _tv.TGroup_getBuffer(*args)
    __swig_setmethods__["last"] = _tv.TGroup_last_set
    __swig_getmethods__["last"] = _tv.TGroup_last_get
    if _newclass:last = property(_tv.TGroup_last_get, _tv.TGroup_last_set)
    __swig_setmethods__["clip"] = _tv.TGroup_clip_set
    __swig_getmethods__["clip"] = _tv.TGroup_clip_get
    if _newclass:clip = property(_tv.TGroup_clip_get, _tv.TGroup_clip_set)
    __swig_setmethods__["phase"] = _tv.TGroup_phase_set
    __swig_getmethods__["phase"] = _tv.TGroup_phase_get
    if _newclass:phase = property(_tv.TGroup_phase_get, _tv.TGroup_phase_set)
    __swig_setmethods__["buffer"] = _tv.TGroup_buffer_set
    __swig_getmethods__["buffer"] = _tv.TGroup_buffer_get
    if _newclass:buffer = property(_tv.TGroup_buffer_get, _tv.TGroup_buffer_set)
    __swig_setmethods__["lockFlag"] = _tv.TGroup_lockFlag_set
    __swig_getmethods__["lockFlag"] = _tv.TGroup_lockFlag_get
    if _newclass:lockFlag = property(_tv.TGroup_lockFlag_get, _tv.TGroup_lockFlag_set)
    __swig_setmethods__["endState"] = _tv.TGroup_endState_set
    __swig_getmethods__["endState"] = _tv.TGroup_endState_get
    if _newclass:endState = property(_tv.TGroup_endState_get, _tv.TGroup_endState_set)

class TGroupPtr(TGroup):
    def __init__(self, this):
        _swig_setattr(self, TGroup, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TGroup, 'thisown', 0)
        _swig_setattr(self, TGroup,self.__class__,TGroup)
_tv.TGroup_swigregister(TGroupPtr)

class TWindowInit(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TWindowInit, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TWindowInit, name)
    def __repr__(self):
        return "<C TWindowInit instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TWindowInit, 'this', _tv.new_TWindowInit(*args))
        _swig_setattr(self, TWindowInit, 'thisown', 1)
    def defaultInitFrame(*args): return _tv.TWindowInit_defaultInitFrame(*args)
    def __del__(self, destroy=_tv.delete_TWindowInit):
        try:
            if self.thisown: destroy(self)
        except: pass

class TWindowInitPtr(TWindowInit):
    def __init__(self, this):
        _swig_setattr(self, TWindowInit, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TWindowInit, 'thisown', 0)
        _swig_setattr(self, TWindowInit,self.__class__,TWindowInit)
_tv.TWindowInit_swigregister(TWindowInitPtr)

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
        if self.__class__ == TWindow:
            args = (None,) + args
        else:
            args = (self,) + args
        _swig_setattr(self, TWindow, 'this', _tv.new_TWindow(*args))
        _swig_setattr(self, TWindow, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TWindow):
        try:
            if self.thisown: destroy(self)
        except: pass
    def close(*args): return _tv.TWindow_close(*args)
    def getPalette(*args): return _tv.TWindow_getPalette(*args)
    def getTitle(*args): return _tv.TWindow_getTitle(*args)
    def handleEvent(*args): return _tv.TWindow_handleEvent(*args)
    __swig_getmethods__["initFrame"] = lambda x: _tv.TWindow_initFrame
    if _newclass:initFrame = staticmethod(_tv.TWindow_initFrame)
    def setState(*args): return _tv.TWindow_setState(*args)
    def sizeLimits(*args): return _tv.TWindow_sizeLimits(*args)
    def standardScrollBar(*args): return _tv.TWindow_standardScrollBar(*args)
    def zoom(*args): return _tv.TWindow_zoom(*args)
    def shutDown(*args): return _tv.TWindow_shutDown(*args)
    __swig_setmethods__["flags"] = _tv.TWindow_flags_set
    __swig_getmethods__["flags"] = _tv.TWindow_flags_get
    if _newclass:flags = property(_tv.TWindow_flags_get, _tv.TWindow_flags_set)
    __swig_setmethods__["zoomRect"] = _tv.TWindow_zoomRect_set
    __swig_getmethods__["zoomRect"] = _tv.TWindow_zoomRect_get
    if _newclass:zoomRect = property(_tv.TWindow_zoomRect_get, _tv.TWindow_zoomRect_set)
    __swig_setmethods__["number"] = _tv.TWindow_number_set
    __swig_getmethods__["number"] = _tv.TWindow_number_get
    if _newclass:number = property(_tv.TWindow_number_get, _tv.TWindow_number_set)
    __swig_setmethods__["palette"] = _tv.TWindow_palette_set
    __swig_getmethods__["palette"] = _tv.TWindow_palette_get
    if _newclass:palette = property(_tv.TWindow_palette_get, _tv.TWindow_palette_set)
    __swig_setmethods__["frame"] = _tv.TWindow_frame_set
    __swig_getmethods__["frame"] = _tv.TWindow_frame_get
    if _newclass:frame = property(_tv.TWindow_frame_get, _tv.TWindow_frame_set)
    __swig_setmethods__["title"] = _tv.TWindow_title_set
    __swig_getmethods__["title"] = _tv.TWindow_title_get
    if _newclass:title = property(_tv.TWindow_title_get, _tv.TWindow_title_set)
    __swig_setmethods__["intlTitle"] = _tv.TWindow_intlTitle_set
    __swig_getmethods__["intlTitle"] = _tv.TWindow_intlTitle_get
    if _newclass:intlTitle = property(_tv.TWindow_intlTitle_get, _tv.TWindow_intlTitle_set)
    def __disown__(self):
        self.thisown = 0
        _tv.disown_TWindow(self)
        return weakref_proxy(self)

class TWindowPtr(TWindow):
    def __init__(self, this):
        _swig_setattr(self, TWindow, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TWindow, 'thisown', 0)
        _swig_setattr(self, TWindow,self.__class__,TWindow)
_tv.TWindow_swigregister(TWindowPtr)

TWindow_initFrame = _tv.TWindow_initFrame

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
        _swig_setattr(self, TScrollBar, 'this', _tv.new_TScrollBar(*args))
        _swig_setattr(self, TScrollBar, 'thisown', 1)
    def draw(*args): return _tv.TScrollBar_draw(*args)
    def getPalette(*args): return _tv.TScrollBar_getPalette(*args)
    def handleEvent(*args): return _tv.TScrollBar_handleEvent(*args)
    def scrollDraw(*args): return _tv.TScrollBar_scrollDraw(*args)
    def scrollStep(*args): return _tv.TScrollBar_scrollStep(*args)
    def setParams(*args): return _tv.TScrollBar_setParams(*args)
    def setRange(*args): return _tv.TScrollBar_setRange(*args)
    def setStep(*args): return _tv.TScrollBar_setStep(*args)
    def setValue(*args): return _tv.TScrollBar_setValue(*args)
    def drawPos(*args): return _tv.TScrollBar_drawPos(*args)
    def getPos(*args): return _tv.TScrollBar_getPos(*args)
    def getSize(*args): return _tv.TScrollBar_getSize(*args)
    __swig_setmethods__["value"] = _tv.TScrollBar_value_set
    __swig_getmethods__["value"] = _tv.TScrollBar_value_get
    if _newclass:value = property(_tv.TScrollBar_value_get, _tv.TScrollBar_value_set)
    __swig_setmethods__["chars"] = _tv.TScrollBar_chars_set
    __swig_getmethods__["chars"] = _tv.TScrollBar_chars_get
    if _newclass:chars = property(_tv.TScrollBar_chars_get, _tv.TScrollBar_chars_set)
    __swig_setmethods__["minVal"] = _tv.TScrollBar_minVal_set
    __swig_getmethods__["minVal"] = _tv.TScrollBar_minVal_get
    if _newclass:minVal = property(_tv.TScrollBar_minVal_get, _tv.TScrollBar_minVal_set)
    __swig_setmethods__["maxVal"] = _tv.TScrollBar_maxVal_set
    __swig_getmethods__["maxVal"] = _tv.TScrollBar_maxVal_get
    if _newclass:maxVal = property(_tv.TScrollBar_maxVal_get, _tv.TScrollBar_maxVal_set)
    __swig_setmethods__["pgStep"] = _tv.TScrollBar_pgStep_set
    __swig_getmethods__["pgStep"] = _tv.TScrollBar_pgStep_get
    if _newclass:pgStep = property(_tv.TScrollBar_pgStep_get, _tv.TScrollBar_pgStep_set)
    __swig_setmethods__["arStep"] = _tv.TScrollBar_arStep_set
    __swig_getmethods__["arStep"] = _tv.TScrollBar_arStep_get
    if _newclass:arStep = property(_tv.TScrollBar_arStep_get, _tv.TScrollBar_arStep_set)
    def __del__(self, destroy=_tv.delete_TScrollBar):
        try:
            if self.thisown: destroy(self)
        except: pass

class TScrollBarPtr(TScrollBar):
    def __init__(self, this):
        _swig_setattr(self, TScrollBar, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TScrollBar, 'thisown', 0)
        _swig_setattr(self, TScrollBar,self.__class__,TScrollBar)
_tv.TScrollBar_swigregister(TScrollBarPtr)

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
        _swig_setattr(self, TScroller, 'this', _tv.new_TScroller(*args))
        _swig_setattr(self, TScroller, 'thisown', 1)
    def changeBounds(*args): return _tv.TScroller_changeBounds(*args)
    def getPalette(*args): return _tv.TScroller_getPalette(*args)
    def handleEvent(*args): return _tv.TScroller_handleEvent(*args)
    def scrollDraw(*args): return _tv.TScroller_scrollDraw(*args)
    def scrollTo(*args): return _tv.TScroller_scrollTo(*args)
    def setLimit(*args): return _tv.TScroller_setLimit(*args)
    def setState(*args): return _tv.TScroller_setState(*args)
    def checkDraw(*args): return _tv.TScroller_checkDraw(*args)
    def shutDown(*args): return _tv.TScroller_shutDown(*args)
    __swig_setmethods__["wheelStep"] = _tv.TScroller_wheelStep_set
    __swig_getmethods__["wheelStep"] = _tv.TScroller_wheelStep_get
    if _newclass:wheelStep = property(_tv.TScroller_wheelStep_get, _tv.TScroller_wheelStep_set)
    def __del__(self, destroy=_tv.delete_TScroller):
        try:
            if self.thisown: destroy(self)
        except: pass

class TScrollerPtr(TScroller):
    def __init__(self, this):
        _swig_setattr(self, TScroller, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TScroller, 'thisown', 0)
        _swig_setattr(self, TScroller,self.__class__,TScroller)
_tv.TScroller_swigregister(TScrollerPtr)

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
        _swig_setattr(self, TButton, 'this', _tv.new_TButton(*args))
        _swig_setattr(self, TButton, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TButton):
        try:
            if self.thisown: destroy(self)
        except: pass
    def draw(*args): return _tv.TButton_draw(*args)
    def drawState(*args): return _tv.TButton_drawState(*args)
    def getPalette(*args): return _tv.TButton_getPalette(*args)
    def handleEvent(*args): return _tv.TButton_handleEvent(*args)
    def makeDefault(*args): return _tv.TButton_makeDefault(*args)
    def press(*args): return _tv.TButton_press(*args)
    def setState(*args): return _tv.TButton_setState(*args)
    def setCallBack(*args): return _tv.TButton_setCallBack(*args)
    def getText(*args): return _tv.TButton_getText(*args)
    __swig_setmethods__["title"] = _tv.TButton_title_set
    __swig_getmethods__["title"] = _tv.TButton_title_get
    if _newclass:title = property(_tv.TButton_title_get, _tv.TButton_title_set)
    __swig_setmethods__["intlTitle"] = _tv.TButton_intlTitle_set
    __swig_getmethods__["intlTitle"] = _tv.TButton_intlTitle_get
    if _newclass:intlTitle = property(_tv.TButton_intlTitle_get, _tv.TButton_intlTitle_set)

class TButtonPtr(TButton):
    def __init__(self, this):
        _swig_setattr(self, TButton, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TButton, 'thisown', 0)
        _swig_setattr(self, TButton,self.__class__,TButton)
_tv.TButton_swigregister(TButtonPtr)
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
    def __del__(self, destroy=_tv.delete_TInputLineBase):
        try:
            if self.thisown: destroy(self)
        except: pass
    def dataSize(*args): return _tv.TInputLineBase_dataSize(*args)
    def getPalette(*args): return _tv.TInputLineBase_getPalette(*args)
    def handleEvent(*args): return _tv.TInputLineBase_handleEvent(*args)
    def selectAll(*args): return _tv.TInputLineBase_selectAll(*args)
    def setState(*args): return _tv.TInputLineBase_setState(*args)
    def SetValidator(*args): return _tv.TInputLineBase_SetValidator(*args)
    def valid(*args): return _tv.TInputLineBase_valid(*args)
    def insertChar(*args): return _tv.TInputLineBase_insertChar(*args)
    def assignPos(*args): return _tv.TInputLineBase_assignPos(*args)
    def pasteFromOSClipboard(*args): return _tv.TInputLineBase_pasteFromOSClipboard(*args)
    def copyToOSClipboard(*args): return _tv.TInputLineBase_copyToOSClipboard(*args)
    def setDataFromStr(*args): return _tv.TInputLineBase_setDataFromStr(*args)
    def getData(*args): return _tv.TInputLineBase_getData(*args)
    __swig_setmethods__["curPos"] = _tv.TInputLineBase_curPos_set
    __swig_getmethods__["curPos"] = _tv.TInputLineBase_curPos_get
    if _newclass:curPos = property(_tv.TInputLineBase_curPos_get, _tv.TInputLineBase_curPos_set)
    __swig_setmethods__["firstPos"] = _tv.TInputLineBase_firstPos_set
    __swig_getmethods__["firstPos"] = _tv.TInputLineBase_firstPos_get
    if _newclass:firstPos = property(_tv.TInputLineBase_firstPos_get, _tv.TInputLineBase_firstPos_set)
    __swig_setmethods__["selStart"] = _tv.TInputLineBase_selStart_set
    __swig_getmethods__["selStart"] = _tv.TInputLineBase_selStart_get
    if _newclass:selStart = property(_tv.TInputLineBase_selStart_get, _tv.TInputLineBase_selStart_set)
    __swig_setmethods__["selEnd"] = _tv.TInputLineBase_selEnd_set
    __swig_getmethods__["selEnd"] = _tv.TInputLineBase_selEnd_get
    if _newclass:selEnd = property(_tv.TInputLineBase_selEnd_get, _tv.TInputLineBase_selEnd_set)

class TInputLineBasePtr(TInputLineBase):
    def __init__(self, this):
        _swig_setattr(self, TInputLineBase, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TInputLineBase, 'thisown', 0)
        _swig_setattr(self, TInputLineBase,self.__class__,TInputLineBase)
_tv.TInputLineBase_swigregister(TInputLineBasePtr)

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
    def setData(*args): return _tv.TInputLineBaseChar_setData(*args)
    def setDataFromStr(*args): return _tv.TInputLineBaseChar_setDataFromStr(*args)
    def assignPos(*args): return _tv.TInputLineBaseChar_assignPos(*args)
    def pasteFromOSClipboard(*args): return _tv.TInputLineBaseChar_pasteFromOSClipboard(*args)
    def copyToOSClipboard(*args): return _tv.TInputLineBaseChar_copyToOSClipboard(*args)
    def draw(*args): return _tv.TInputLineBaseChar_draw(*args)
    def __del__(self, destroy=_tv.delete_TInputLineBaseChar):
        try:
            if self.thisown: destroy(self)
        except: pass

class TInputLineBaseCharPtr(TInputLineBaseChar):
    def __init__(self, this):
        _swig_setattr(self, TInputLineBaseChar, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TInputLineBaseChar, 'thisown', 0)
        _swig_setattr(self, TInputLineBaseChar,self.__class__,TInputLineBaseChar)
_tv.TInputLineBaseChar_swigregister(TInputLineBaseCharPtr)

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
        _swig_setattr(self, TInputLine, 'this', _tv.new_TInputLine(*args))
        _swig_setattr(self, TInputLine, 'thisown', 1)
    def insertChar(*args): return _tv.TInputLine_insertChar(*args)
    def __del__(self, destroy=_tv.delete_TInputLine):
        try:
            if self.thisown: destroy(self)
        except: pass

class TInputLinePtr(TInputLine):
    def __init__(self, this):
        _swig_setattr(self, TInputLine, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TInputLine, 'thisown', 0)
        _swig_setattr(self, TInputLine,self.__class__,TInputLine)
_tv.TInputLine_swigregister(TInputLinePtr)

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
    def setData(*args): return _tv.TInputLineBaseU16_setData(*args)
    def setDataFromStr(*args): return _tv.TInputLineBaseU16_setDataFromStr(*args)
    def assignPos(*args): return _tv.TInputLineBaseU16_assignPos(*args)
    def pasteFromOSClipboard(*args): return _tv.TInputLineBaseU16_pasteFromOSClipboard(*args)
    def copyToOSClipboard(*args): return _tv.TInputLineBaseU16_copyToOSClipboard(*args)
    def draw(*args): return _tv.TInputLineBaseU16_draw(*args)
    def __del__(self, destroy=_tv.delete_TInputLineBaseU16):
        try:
            if self.thisown: destroy(self)
        except: pass

class TInputLineBaseU16Ptr(TInputLineBaseU16):
    def __init__(self, this):
        _swig_setattr(self, TInputLineBaseU16, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TInputLineBaseU16, 'thisown', 0)
        _swig_setattr(self, TInputLineBaseU16,self.__class__,TInputLineBaseU16)
_tv.TInputLineBaseU16_swigregister(TInputLineBaseU16Ptr)

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
        _swig_setattr(self, TInputLineU16, 'this', _tv.new_TInputLineU16(*args))
        _swig_setattr(self, TInputLineU16, 'thisown', 1)
    def insertChar(*args): return _tv.TInputLineU16_insertChar(*args)
    def __del__(self, destroy=_tv.delete_TInputLineU16):
        try:
            if self.thisown: destroy(self)
        except: pass

class TInputLineU16Ptr(TInputLineU16):
    def __init__(self, this):
        _swig_setattr(self, TInputLineU16, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TInputLineU16, 'thisown', 0)
        _swig_setattr(self, TInputLineU16,self.__class__,TInputLineU16)
_tv.TInputLineU16_swigregister(TInputLineU16Ptr)

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
        _swig_setattr(self, TStaticText, 'this', _tv.new_TStaticText(*args))
        _swig_setattr(self, TStaticText, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TStaticText):
        try:
            if self.thisown: destroy(self)
        except: pass
    def draw(*args): return _tv.TStaticText_draw(*args)
    def getPalette(*args): return _tv.TStaticText_getPalette(*args)
    def getText(*args): return _tv.TStaticText_getText(*args)

class TStaticTextPtr(TStaticText):
    def __init__(self, this):
        _swig_setattr(self, TStaticText, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TStaticText, 'thisown', 0)
        _swig_setattr(self, TStaticText,self.__class__,TStaticText)
_tv.TStaticText_swigregister(TStaticTextPtr)

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
        _swig_setattr(self, T1StaticText, 'this', _tv.new_T1StaticText(*args))
        _swig_setattr(self, T1StaticText, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_T1StaticText):
        try:
            if self.thisown: destroy(self)
        except: pass

class T1StaticTextPtr(T1StaticText):
    def __init__(self, this):
        _swig_setattr(self, T1StaticText, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, T1StaticText, 'thisown', 0)
        _swig_setattr(self, T1StaticText,self.__class__,T1StaticText)
_tv.T1StaticText_swigregister(T1StaticTextPtr)

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
        _swig_setattr(self, TLabel, 'this', _tv.new_TLabel(*args))
        _swig_setattr(self, TLabel, 'thisown', 1)
    def draw(*args): return _tv.TLabel_draw(*args)
    def getPalette(*args): return _tv.TLabel_getPalette(*args)
    def handleEvent(*args): return _tv.TLabel_handleEvent(*args)
    def shutDown(*args): return _tv.TLabel_shutDown(*args)
    __swig_setmethods__["link"] = _tv.TLabel_link_set
    __swig_getmethods__["link"] = _tv.TLabel_link_get
    if _newclass:link = property(_tv.TLabel_link_get, _tv.TLabel_link_set)
    def __del__(self, destroy=_tv.delete_TLabel):
        try:
            if self.thisown: destroy(self)
        except: pass

class TLabelPtr(TLabel):
    def __init__(self, this):
        _swig_setattr(self, TLabel, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TLabel, 'thisown', 0)
        _swig_setattr(self, TLabel,self.__class__,TLabel)
_tv.TLabel_swigregister(TLabelPtr)

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
        _swig_setattr(self, T1Label, 'this', _tv.new_T1Label(*args))
        _swig_setattr(self, T1Label, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_T1Label):
        try:
            if self.thisown: destroy(self)
        except: pass

class T1LabelPtr(T1Label):
    def __init__(self, this):
        _swig_setattr(self, T1Label, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, T1Label, 'thisown', 0)
        _swig_setattr(self, T1Label,self.__class__,T1Label)
_tv.T1Label_swigregister(T1LabelPtr)

class TSItem(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TSItem, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TSItem, name)
    def __repr__(self):
        return "<C TSItem instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TSItem, 'this', _tv.new_TSItem(*args))
        _swig_setattr(self, TSItem, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TSItem):
        try:
            if self.thisown: destroy(self)
        except: pass
    def append(*args): return _tv.TSItem_append(*args)
    def __add__(self, b):
        self.append(b)
        return self

    __swig_setmethods__["value"] = _tv.TSItem_value_set
    __swig_getmethods__["value"] = _tv.TSItem_value_get
    if _newclass:value = property(_tv.TSItem_value_get, _tv.TSItem_value_set)
    __swig_setmethods__["next"] = _tv.TSItem_next_set
    __swig_getmethods__["next"] = _tv.TSItem_next_get
    if _newclass:next = property(_tv.TSItem_next_get, _tv.TSItem_next_set)

class TSItemPtr(TSItem):
    def __init__(self, this):
        _swig_setattr(self, TSItem, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TSItem, 'thisown', 0)
        _swig_setattr(self, TSItem,self.__class__,TSItem)
_tv.TSItem_swigregister(TSItemPtr)

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
        _swig_setattr(self, TCluster, 'this', _tv.new_TCluster(*args))
        _swig_setattr(self, TCluster, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TCluster):
        try:
            if self.thisown: destroy(self)
        except: pass
    def dataSize(*args): return _tv.TCluster_dataSize(*args)
    def drawBox(*args): return _tv.TCluster_drawBox(*args)
    def getData(*args): return _tv.TCluster_getData(*args)
    def getHelpCtx(*args): return _tv.TCluster_getHelpCtx(*args)
    def getPalette(*args): return _tv.TCluster_getPalette(*args)
    def handleEvent(*args): return _tv.TCluster_handleEvent(*args)
    def mark(*args): return _tv.TCluster_mark(*args)
    def press(*args): return _tv.TCluster_press(*args)
    def movedTo(*args): return _tv.TCluster_movedTo(*args)
    def setData(*args): return _tv.TCluster_setData(*args)
    def setState(*args): return _tv.TCluster_setState(*args)
    def getExtraOptions(*args): return _tv.TCluster_getExtraOptions(*args)
    def setExtraOptions(*args): return _tv.TCluster_setExtraOptions(*args)
    def getItemText(*args): return _tv.TCluster_getItemText(*args)

class TClusterPtr(TCluster):
    def __init__(self, this):
        _swig_setattr(self, TCluster, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TCluster, 'thisown', 0)
        _swig_setattr(self, TCluster,self.__class__,TCluster)
_tv.TCluster_swigregister(TClusterPtr)

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
        _swig_setattr(self, TRadioButtons, 'this', _tv.new_TRadioButtons(*args))
        _swig_setattr(self, TRadioButtons, 'thisown', 1)
    def draw(*args): return _tv.TRadioButtons_draw(*args)
    def mark(*args): return _tv.TRadioButtons_mark(*args)
    def movedTo(*args): return _tv.TRadioButtons_movedTo(*args)
    def press(*args): return _tv.TRadioButtons_press(*args)
    def setData(*args): return _tv.TRadioButtons_setData(*args)
    def __del__(self, destroy=_tv.delete_TRadioButtons):
        try:
            if self.thisown: destroy(self)
        except: pass

class TRadioButtonsPtr(TRadioButtons):
    def __init__(self, this):
        _swig_setattr(self, TRadioButtons, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TRadioButtons, 'thisown', 0)
        _swig_setattr(self, TRadioButtons,self.__class__,TRadioButtons)
_tv.TRadioButtons_swigregister(TRadioButtonsPtr)

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
        _swig_setattr(self, TRadioButtons32, 'this', _tv.new_TRadioButtons32(*args))
        _swig_setattr(self, TRadioButtons32, 'thisown', 1)
    def dataSize(*args): return _tv.TRadioButtons32_dataSize(*args)
    def __del__(self, destroy=_tv.delete_TRadioButtons32):
        try:
            if self.thisown: destroy(self)
        except: pass

class TRadioButtons32Ptr(TRadioButtons32):
    def __init__(self, this):
        _swig_setattr(self, TRadioButtons32, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TRadioButtons32, 'thisown', 0)
        _swig_setattr(self, TRadioButtons32,self.__class__,TRadioButtons32)
_tv.TRadioButtons32_swigregister(TRadioButtons32Ptr)

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
        _swig_setattr(self, TCheckBoxes, 'this', _tv.new_TCheckBoxes(*args))
        _swig_setattr(self, TCheckBoxes, 'thisown', 1)
    def draw(*args): return _tv.TCheckBoxes_draw(*args)
    def mark(*args): return _tv.TCheckBoxes_mark(*args)
    def press(*args): return _tv.TCheckBoxes_press(*args)
    def __del__(self, destroy=_tv.delete_TCheckBoxes):
        try:
            if self.thisown: destroy(self)
        except: pass

class TCheckBoxesPtr(TCheckBoxes):
    def __init__(self, this):
        _swig_setattr(self, TCheckBoxes, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TCheckBoxes, 'thisown', 0)
        _swig_setattr(self, TCheckBoxes,self.__class__,TCheckBoxes)
_tv.TCheckBoxes_swigregister(TCheckBoxesPtr)

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
        _swig_setattr(self, TCheckBoxes32, 'this', _tv.new_TCheckBoxes32(*args))
        _swig_setattr(self, TCheckBoxes32, 'thisown', 1)
    def dataSize(*args): return _tv.TCheckBoxes32_dataSize(*args)
    def __del__(self, destroy=_tv.delete_TCheckBoxes32):
        try:
            if self.thisown: destroy(self)
        except: pass

class TCheckBoxes32Ptr(TCheckBoxes32):
    def __init__(self, this):
        _swig_setattr(self, TCheckBoxes32, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TCheckBoxes32, 'thisown', 0)
        _swig_setattr(self, TCheckBoxes32,self.__class__,TCheckBoxes32)
_tv.TCheckBoxes32_swigregister(TCheckBoxes32Ptr)

class TMenuItem(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TMenuItem, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TMenuItem, name)
    def __repr__(self):
        return "<C TMenuItem instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TMenuItem, 'this', _tv.new_TMenuItem(*args))
        _swig_setattr(self, TMenuItem, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TMenuItem):
        try:
            if self.thisown: destroy(self)
        except: pass
    def append(*args): return _tv.TMenuItem_append(*args)
    def append(self, p):
        p.thisown = 0
        return _tv.TMenuItem_append(self, p)

    __swig_setmethods__["next"] = _tv.TMenuItem_next_set
    __swig_getmethods__["next"] = _tv.TMenuItem_next_get
    if _newclass:next = property(_tv.TMenuItem_next_get, _tv.TMenuItem_next_set)
    __swig_setmethods__["name"] = _tv.TMenuItem_name_set
    __swig_getmethods__["name"] = _tv.TMenuItem_name_get
    if _newclass:name = property(_tv.TMenuItem_name_get, _tv.TMenuItem_name_set)
    __swig_setmethods__["intlName"] = _tv.TMenuItem_intlName_set
    __swig_getmethods__["intlName"] = _tv.TMenuItem_intlName_get
    if _newclass:intlName = property(_tv.TMenuItem_intlName_get, _tv.TMenuItem_intlName_set)
    __swig_setmethods__["command"] = _tv.TMenuItem_command_set
    __swig_getmethods__["command"] = _tv.TMenuItem_command_get
    if _newclass:command = property(_tv.TMenuItem_command_get, _tv.TMenuItem_command_set)
    __swig_setmethods__["disabled"] = _tv.TMenuItem_disabled_set
    __swig_getmethods__["disabled"] = _tv.TMenuItem_disabled_get
    if _newclass:disabled = property(_tv.TMenuItem_disabled_get, _tv.TMenuItem_disabled_set)
    __swig_setmethods__["keyCode"] = _tv.TMenuItem_keyCode_set
    __swig_getmethods__["keyCode"] = _tv.TMenuItem_keyCode_get
    if _newclass:keyCode = property(_tv.TMenuItem_keyCode_get, _tv.TMenuItem_keyCode_set)
    __swig_setmethods__["helpCtx"] = _tv.TMenuItem_helpCtx_set
    __swig_getmethods__["helpCtx"] = _tv.TMenuItem_helpCtx_get
    if _newclass:helpCtx = property(_tv.TMenuItem_helpCtx_get, _tv.TMenuItem_helpCtx_set)

class TMenuItemPtr(TMenuItem):
    def __init__(self, this):
        _swig_setattr(self, TMenuItem, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TMenuItem, 'thisown', 0)
        _swig_setattr(self, TMenuItem,self.__class__,TMenuItem)
_tv.TMenuItem_swigregister(TMenuItemPtr)

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
        _swig_setattr(self, TSubMenu, 'this', _tv.new_TSubMenu(*args))
        _swig_setattr(self, TSubMenu, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TSubMenu):
        try:
            if self.thisown: destroy(self)
        except: pass

class TSubMenuPtr(TSubMenu):
    def __init__(self, this):
        _swig_setattr(self, TSubMenu, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TSubMenu, 'thisown', 0)
        _swig_setattr(self, TSubMenu,self.__class__,TSubMenu)
_tv.TSubMenu_swigregister(TSubMenuPtr)


makeMenu__ = _tv.makeMenu__

cMakeMenu = _tv.cMakeMenu
class TMenu(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TMenu, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TMenu, name)
    def __repr__(self):
        return "<C TMenu instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TMenu, 'this', _tv.new_TMenu(*args))
        _swig_setattr(self, TMenu, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TMenu):
        try:
            if self.thisown: destroy(self)
        except: pass
    __swig_setmethods__["items"] = _tv.TMenu_items_set
    __swig_getmethods__["items"] = _tv.TMenu_items_get
    if _newclass:items = property(_tv.TMenu_items_get, _tv.TMenu_items_set)
    __swig_setmethods__["deflt"] = _tv.TMenu_deflt_set
    __swig_getmethods__["deflt"] = _tv.TMenu_deflt_get
    if _newclass:deflt = property(_tv.TMenu_deflt_get, _tv.TMenu_deflt_set)

class TMenuPtr(TMenu):
    def __init__(self, this):
        _swig_setattr(self, TMenu, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TMenu, 'thisown', 0)
        _swig_setattr(self, TMenu,self.__class__,TMenu)
_tv.TMenu_swigregister(TMenuPtr)

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
        _swig_setattr(self, TMenuView, 'this', _tv.new_TMenuView(*args))
        _swig_setattr(self, TMenuView, 'thisown', 1)
    def execute(*args): return _tv.TMenuView_execute(*args)
    def findItem(*args): return _tv.TMenuView_findItem(*args)
    def getItemRect(*args): return _tv.TMenuView_getItemRect(*args)
    def getHelpCtx(*args): return _tv.TMenuView_getHelpCtx(*args)
    def getPalette(*args): return _tv.TMenuView_getPalette(*args)
    def handleEvent(*args): return _tv.TMenuView_handleEvent(*args)
    def hotKey(*args): return _tv.TMenuView_hotKey(*args)
    def newSubView(*args): return _tv.TMenuView_newSubView(*args)
    __swig_setmethods__["compactMenu"] = _tv.TMenuView_compactMenu_set
    __swig_getmethods__["compactMenu"] = _tv.TMenuView_compactMenu_get
    if _newclass:compactMenu = property(_tv.TMenuView_compactMenu_get, _tv.TMenuView_compactMenu_set)
    def __del__(self, destroy=_tv.delete_TMenuView):
        try:
            if self.thisown: destroy(self)
        except: pass

class TMenuViewPtr(TMenuView):
    def __init__(self, this):
        _swig_setattr(self, TMenuView, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TMenuView, 'thisown', 0)
        _swig_setattr(self, TMenuView,self.__class__,TMenuView)
_tv.TMenuView_swigregister(TMenuViewPtr)

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
        _swig_setattr(self, TMenuBox, 'this', _tv.new_TMenuBox(*args))
        _swig_setattr(self, TMenuBox, 'thisown', 1)
    def draw(*args): return _tv.TMenuBox_draw(*args)
    def getItemRect(*args): return _tv.TMenuBox_getItemRect(*args)
    def __del__(self, destroy=_tv.delete_TMenuBox):
        try:
            if self.thisown: destroy(self)
        except: pass

class TMenuBoxPtr(TMenuBox):
    def __init__(self, this):
        _swig_setattr(self, TMenuBox, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TMenuBox, 'thisown', 0)
        _swig_setattr(self, TMenuBox,self.__class__,TMenuBox)
_tv.TMenuBox_swigregister(TMenuBoxPtr)

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
        _swig_setattr(self, TMenuBar, 'this', _tv.new_TMenuBar(*args))
        _swig_setattr(self, TMenuBar, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TMenuBar):
        try:
            if self.thisown: destroy(self)
        except: pass
    def computeLength(*args): return _tv.TMenuBar_computeLength(*args)
    def draw(*args): return _tv.TMenuBar_draw(*args)
    def getItemRect(*args): return _tv.TMenuBar_getItemRect(*args)
    def changeBounds(*args): return _tv.TMenuBar_changeBounds(*args)

class TMenuBarPtr(TMenuBar):
    def __init__(self, this):
        _swig_setattr(self, TMenuBar, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TMenuBar, 'thisown', 0)
        _swig_setattr(self, TMenuBar,self.__class__,TMenuBar)
_tv.TMenuBar_swigregister(TMenuBarPtr)

class TStatusItem(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TStatusItem, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TStatusItem, name)
    def __repr__(self):
        return "<C TStatusItem instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TStatusItem, 'this', _tv.new_TStatusItem(*args))
        _swig_setattr(self, TStatusItem, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TStatusItem):
        try:
            if self.thisown: destroy(self)
        except: pass
    __swig_setmethods__["next"] = _tv.TStatusItem_next_set
    __swig_getmethods__["next"] = _tv.TStatusItem_next_get
    if _newclass:next = property(_tv.TStatusItem_next_get, _tv.TStatusItem_next_set)
    __swig_setmethods__["text"] = _tv.TStatusItem_text_set
    __swig_getmethods__["text"] = _tv.TStatusItem_text_get
    if _newclass:text = property(_tv.TStatusItem_text_get, _tv.TStatusItem_text_set)
    __swig_setmethods__["intlText"] = _tv.TStatusItem_intlText_set
    __swig_getmethods__["intlText"] = _tv.TStatusItem_intlText_get
    if _newclass:intlText = property(_tv.TStatusItem_intlText_get, _tv.TStatusItem_intlText_set)
    __swig_setmethods__["keyCode"] = _tv.TStatusItem_keyCode_set
    __swig_getmethods__["keyCode"] = _tv.TStatusItem_keyCode_get
    if _newclass:keyCode = property(_tv.TStatusItem_keyCode_get, _tv.TStatusItem_keyCode_set)
    __swig_setmethods__["command"] = _tv.TStatusItem_command_set
    __swig_getmethods__["command"] = _tv.TStatusItem_command_get
    if _newclass:command = property(_tv.TStatusItem_command_get, _tv.TStatusItem_command_set)

class TStatusItemPtr(TStatusItem):
    def __init__(self, this):
        _swig_setattr(self, TStatusItem, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TStatusItem, 'thisown', 0)
        _swig_setattr(self, TStatusItem,self.__class__,TStatusItem)
_tv.TStatusItem_swigregister(TStatusItemPtr)

class TStatusDef(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TStatusDef, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TStatusDef, name)
    def __repr__(self):
        return "<C TStatusDef instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TStatusDef, 'this', _tv.new_TStatusDef(*args))
        _swig_setattr(self, TStatusDef, 'thisown', 1)
    __swig_setmethods__["next"] = _tv.TStatusDef_next_set
    __swig_getmethods__["next"] = _tv.TStatusDef_next_get
    if _newclass:next = property(_tv.TStatusDef_next_get, _tv.TStatusDef_next_set)
    __swig_setmethods__["min"] = _tv.TStatusDef_min_set
    __swig_getmethods__["min"] = _tv.TStatusDef_min_get
    if _newclass:min = property(_tv.TStatusDef_min_get, _tv.TStatusDef_min_set)
    __swig_setmethods__["max"] = _tv.TStatusDef_max_set
    __swig_getmethods__["max"] = _tv.TStatusDef_max_get
    if _newclass:max = property(_tv.TStatusDef_max_get, _tv.TStatusDef_max_set)
    __swig_setmethods__["items"] = _tv.TStatusDef_items_set
    __swig_getmethods__["items"] = _tv.TStatusDef_items_get
    if _newclass:items = property(_tv.TStatusDef_items_get, _tv.TStatusDef_items_set)
    def __del__(self, destroy=_tv.delete_TStatusDef):
        try:
            if self.thisown: destroy(self)
        except: pass

class TStatusDefPtr(TStatusDef):
    def __init__(self, this):
        _swig_setattr(self, TStatusDef, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TStatusDef, 'thisown', 0)
        _swig_setattr(self, TStatusDef,self.__class__,TStatusDef)
_tv.TStatusDef_swigregister(TStatusDefPtr)

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
        _swig_setattr(self, TStatusLine, 'this', _tv.new_TStatusLine(*args))
        _swig_setattr(self, TStatusLine, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TStatusLine):
        try:
            if self.thisown: destroy(self)
        except: pass
    def draw(*args): return _tv.TStatusLine_draw(*args)
    def getPalette(*args): return _tv.TStatusLine_getPalette(*args)
    def handleEvent(*args): return _tv.TStatusLine_handleEvent(*args)
    def hint(*args): return _tv.TStatusLine_hint(*args)
    def update(*args): return _tv.TStatusLine_update(*args)
    def computeLength(*args): return _tv.TStatusLine_computeLength(*args)
    def changeBounds(*args): return _tv.TStatusLine_changeBounds(*args)
    __swig_setmethods__["compactStatus"] = _tv.TStatusLine_compactStatus_set
    __swig_getmethods__["compactStatus"] = _tv.TStatusLine_compactStatus_get
    if _newclass:compactStatus = property(_tv.TStatusLine_compactStatus_get, _tv.TStatusLine_compactStatus_set)

class TStatusLinePtr(TStatusLine):
    def __init__(self, this):
        _swig_setattr(self, TStatusLine, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TStatusLine, 'thisown', 0)
        _swig_setattr(self, TStatusLine,self.__class__,TStatusLine)
_tv.TStatusLine_swigregister(TStatusLinePtr)

dsktTileVertical = _tv.dsktTileVertical
dsktTileHorizontal = _tv.dsktTileHorizontal
class TDeskInit(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TDeskInit, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TDeskInit, name)
    def __repr__(self):
        return "<C TDeskInit instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TDeskInit, 'this', _tv.new_TDeskInit(*args))
        _swig_setattr(self, TDeskInit, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TDeskInit):
        try:
            if self.thisown: destroy(self)
        except: pass

class TDeskInitPtr(TDeskInit):
    def __init__(self, this):
        _swig_setattr(self, TDeskInit, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TDeskInit, 'thisown', 0)
        _swig_setattr(self, TDeskInit,self.__class__,TDeskInit)
_tv.TDeskInit_swigregister(TDeskInitPtr)

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
        _swig_setattr(self, TDeskTop, 'this', _tv.new_TDeskTop(*args))
        _swig_setattr(self, TDeskTop, 'thisown', 1)
    def cascade(*args): return _tv.TDeskTop_cascade(*args)
    def handleEvent(*args): return _tv.TDeskTop_handleEvent(*args)
    __swig_getmethods__["initBackground"] = lambda x: _tv.TDeskTop_initBackground
    if _newclass:initBackground = staticmethod(_tv.TDeskTop_initBackground)
    def tile(*args): return _tv.TDeskTop_tile(*args)
    def tileError(*args): return _tv.TDeskTop_tileError(*args)
    def shutDown(*args): return _tv.TDeskTop_shutDown(*args)
    def getBackground(*args): return _tv.TDeskTop_getBackground(*args)
    def getOptions(*args): return _tv.TDeskTop_getOptions(*args)
    def setOptions(*args): return _tv.TDeskTop_setOptions(*args)
    def canShowCursor(*args): return _tv.TDeskTop_canShowCursor(*args)
    def execView(*args): return _tv.TDeskTop_execView(*args)
    def __del__(self, destroy=_tv.delete_TDeskTop):
        try:
            if self.thisown: destroy(self)
        except: pass

class TDeskTopPtr(TDeskTop):
    def __init__(self, this):
        _swig_setattr(self, TDeskTop, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TDeskTop, 'thisown', 0)
        _swig_setattr(self, TDeskTop,self.__class__,TDeskTop)
_tv.TDeskTop_swigregister(TDeskTopPtr)

TDeskTop_initBackground = _tv.TDeskTop_initBackground

cpColor = _tv.cpColor
cpBlackWhite = _tv.cpBlackWhite
cpMonochrome = _tv.cpMonochrome
class TProgInit(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TProgInit, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TProgInit, name)
    def __repr__(self):
        return "<C TProgInit instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TProgInit, 'this', _tv.new_TProgInit(*args))
        _swig_setattr(self, TProgInit, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TProgInit):
        try:
            if self.thisown: destroy(self)
        except: pass

class TProgInitPtr(TProgInit):
    def __init__(self, this):
        _swig_setattr(self, TProgInit, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TProgInit, 'thisown', 0)
        _swig_setattr(self, TProgInit,self.__class__,TProgInit)
_tv.TProgInit_swigregister(TProgInitPtr)

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
        if self.__class__ == TProgram:
            args = (None,) + args
        else:
            args = (self,) + args
        _swig_setattr(self, TProgram, 'this', _tv.new_TProgram(*args))
        _swig_setattr(self, TProgram, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TProgram):
        try:
            if self.thisown: destroy(self)
        except: pass
    def getEvent(*args): return _tv.TProgram_getEvent(*args)
    def getPalette(*args): return _tv.TProgram_getPalette(*args)
    def handleEvent(*args): return _tv.TProgram_handleEvent(*args)
    def idle(*args): return _tv.TProgram_idle(*args)
    def initScreen(*args): return _tv.TProgram_initScreen(*args)
    def outOfMemory(*args): return _tv.TProgram_outOfMemory(*args)
    def putEvent(*args): return _tv.TProgram_putEvent(*args)
    def run(*args): return _tv.TProgram_run(*args)
    def setScreenMode(*args): return _tv.TProgram_setScreenMode(*args)
    def setScreenModeExt(*args): return _tv.TProgram_setScreenModeExt(*args)
    def validView(*args): return _tv.TProgram_validView(*args)
    def shutDown(*args): return _tv.TProgram_shutDown(*args)
    def suspend(*args): return _tv.TProgram_suspend(*args)
    def resume(*args): return _tv.TProgram_resume(*args)
    def syncScreenBuffer(*args): return _tv.TProgram_syncScreenBuffer(*args)
    __swig_getmethods__["initStatusLine"] = lambda x: _tv.TProgram_initStatusLine
    if _newclass:initStatusLine = staticmethod(_tv.TProgram_initStatusLine)
    __swig_getmethods__["initMenuBar"] = lambda x: _tv.TProgram_initMenuBar
    if _newclass:initMenuBar = staticmethod(_tv.TProgram_initMenuBar)
    __swig_getmethods__["initDeskTop"] = lambda x: _tv.TProgram_initDeskTop
    if _newclass:initDeskTop = staticmethod(_tv.TProgram_initDeskTop)
    __swig_getmethods__["resetIdleTime"] = lambda x: _tv.TProgram_resetIdleTime
    if _newclass:resetIdleTime = staticmethod(_tv.TProgram_resetIdleTime)
    def __disown__(self):
        self.thisown = 0
        _tv.disown_TProgram(self)
        return weakref_proxy(self)

class TProgramPtr(TProgram):
    def __init__(self, this):
        _swig_setattr(self, TProgram, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TProgram, 'thisown', 0)
        _swig_setattr(self, TProgram,self.__class__,TProgram)
_tv.TProgram_swigregister(TProgramPtr)
apColor = cvar.apColor
apBlackWhite = cvar.apBlackWhite
apMonochrome = cvar.apMonochrome

TProgram_initStatusLine = _tv.TProgram_initStatusLine

TProgram_initMenuBar = _tv.TProgram_initMenuBar

TProgram_initDeskTop = _tv.TProgram_initDeskTop

TProgram_resetIdleTime = _tv.TProgram_resetIdleTime

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
        _swig_setattr(self, TApplication, 'this', _tv.new_TApplication(*args))
        _swig_setattr(self, TApplication, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TApplication):
        try:
            if self.thisown: destroy(self)
        except: pass
    def suspend(*args): return _tv.TApplication_suspend(*args)
    def resume(*args): return _tv.TApplication_resume(*args)
    def __disown__(self):
        self.thisown = 0
        _tv.disown_TApplication(self)
        return weakref_proxy(self)

class TApplicationPtr(TApplication):
    def __init__(self, this):
        _swig_setattr(self, TApplication, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TApplication, 'thisown', 0)
        _swig_setattr(self, TApplication,self.__class__,TApplication)
_tv.TApplication_swigregister(TApplicationPtr)

cmValid = _tv.cmValid
cmQuit = _tv.cmQuit
cmError = _tv.cmError
cmMenu = _tv.cmMenu
cmClose = _tv.cmClose
cmZoom = _tv.cmZoom
cmResize = _tv.cmResize
cmNext = _tv.cmNext
cmPrev = _tv.cmPrev
cmHelp = _tv.cmHelp
cmOK = _tv.cmOK
cmCancel = _tv.cmCancel
cmYes = _tv.cmYes
cmNo = _tv.cmNo
cmDefault = _tv.cmDefault
sfVisible = _tv.sfVisible
sfCursorVis = _tv.sfCursorVis
sfCursorIns = _tv.sfCursorIns
sfShadow = _tv.sfShadow
sfActive = _tv.sfActive
sfSelected = _tv.sfSelected
sfFocused = _tv.sfFocused
sfDragging = _tv.sfDragging
sfDisabled = _tv.sfDisabled
sfModal = _tv.sfModal
sfDefault = _tv.sfDefault
sfExposed = _tv.sfExposed
ofSelectable = _tv.ofSelectable
ofTopSelect = _tv.ofTopSelect
ofFirstClick = _tv.ofFirstClick
ofFramed = _tv.ofFramed
ofPreProcess = _tv.ofPreProcess
ofPostProcess = _tv.ofPostProcess
ofBuffered = _tv.ofBuffered
ofTileable = _tv.ofTileable
ofCenterX = _tv.ofCenterX
ofCenterY = _tv.ofCenterY
ofCentered = _tv.ofCentered
ofBeVerbose = _tv.ofBeVerbose
gfGrowLoX = _tv.gfGrowLoX
gfGrowLoY = _tv.gfGrowLoY
gfGrowHiX = _tv.gfGrowHiX
gfGrowHiY = _tv.gfGrowHiY
gfGrowAll = _tv.gfGrowAll
gfGrowRel = _tv.gfGrowRel
dmDragMove = _tv.dmDragMove
dmDragGrow = _tv.dmDragGrow
dmLimitLoX = _tv.dmLimitLoX
dmLimitLoY = _tv.dmLimitLoY
dmLimitHiX = _tv.dmLimitHiX
dmLimitHiY = _tv.dmLimitHiY
dmLimitAll = _tv.dmLimitAll
hcNoContext = _tv.hcNoContext
hcDragging = _tv.hcDragging
sbLeftArrow = _tv.sbLeftArrow
sbRightArrow = _tv.sbRightArrow
sbPageLeft = _tv.sbPageLeft
sbPageRight = _tv.sbPageRight
sbUpArrow = _tv.sbUpArrow
sbDownArrow = _tv.sbDownArrow
sbPageUp = _tv.sbPageUp
sbPageDown = _tv.sbPageDown
sbIndicator = _tv.sbIndicator
sbHorizontal = _tv.sbHorizontal
sbVertical = _tv.sbVertical
sbHandleKeyboard = _tv.sbHandleKeyboard
wfMove = _tv.wfMove
wfGrow = _tv.wfGrow
wfClose = _tv.wfClose
wfZoom = _tv.wfZoom
noMenuBar = _tv.noMenuBar
noDeskTop = _tv.noDeskTop
noStatusLine = _tv.noStatusLine
noBackground = _tv.noBackground
noFrame = _tv.noFrame
noViewer = _tv.noViewer
noHistory = _tv.noHistory
wnNoNumber = _tv.wnNoNumber
wpBlueWindow = _tv.wpBlueWindow
wpCyanWindow = _tv.wpCyanWindow
wpGrayWindow = _tv.wpGrayWindow
cmCut = _tv.cmCut
cmCopy = _tv.cmCopy
cmPaste = _tv.cmPaste
cmUndo = _tv.cmUndo
cmClear = _tv.cmClear
cmTile = _tv.cmTile
cmCascade = _tv.cmCascade
cmReceivedFocus = _tv.cmReceivedFocus
cmReleasedFocus = _tv.cmReleasedFocus
cmCommandSetChanged = _tv.cmCommandSetChanged
cmScrollBarChanged = _tv.cmScrollBarChanged
cmScrollBarClicked = _tv.cmScrollBarClicked
cmSelectWindowNum = _tv.cmSelectWindowNum
cmListItemSelected = _tv.cmListItemSelected
cmClosingWindow = _tv.cmClosingWindow
cmClusterMovedTo = _tv.cmClusterMovedTo
cmClusterPress = _tv.cmClusterPress
cmRecordHistory = _tv.cmRecordHistory
cmListItemFocused = _tv.cmListItemFocused
cmGrabDefault = _tv.cmGrabDefault
cmReleaseDefault = _tv.cmReleaseDefault
cmUpdateCodePage = _tv.cmUpdateCodePage
cmCallShell = _tv.cmCallShell
positionalEvents = _tv.positionalEvents
focusedEvents = _tv.focusedEvents
kbSpace = _tv.kbSpace
kbCtrlA = _tv.kbCtrlA
kbCtrlB = _tv.kbCtrlB
kbCtrlC = _tv.kbCtrlC
kbCtrlD = _tv.kbCtrlD
kbCtrlE = _tv.kbCtrlE
kbCtrlF = _tv.kbCtrlF
kbCtrlG = _tv.kbCtrlG
kbCtrlH = _tv.kbCtrlH
kbCtrlI = _tv.kbCtrlI
kbCtrlJ = _tv.kbCtrlJ
kbCtrlK = _tv.kbCtrlK
kbCtrlL = _tv.kbCtrlL
kbCtrlM = _tv.kbCtrlM
kbCtrlN = _tv.kbCtrlN
kbCtrlO = _tv.kbCtrlO
kbCtrlP = _tv.kbCtrlP
kbCtrlQ = _tv.kbCtrlQ
kbCtrlR = _tv.kbCtrlR
kbCtrlS = _tv.kbCtrlS
kbCtrlT = _tv.kbCtrlT
kbCtrlU = _tv.kbCtrlU
kbCtrlV = _tv.kbCtrlV
kbCtrlW = _tv.kbCtrlW
kbCtrlX = _tv.kbCtrlX
kbCtrlY = _tv.kbCtrlY
kbCtrlZ = _tv.kbCtrlZ
kbEsc = _tv.kbEsc
kbAltSpace = _tv.kbAltSpace
kbCtrlIns = _tv.kbCtrlIns
kbShiftIns = _tv.kbShiftIns
kbCtrlDel = _tv.kbCtrlDel
kbShiftDel = _tv.kbShiftDel
kbCtrlShiftIns = _tv.kbCtrlShiftIns
kbCtrlShiftDel = _tv.kbCtrlShiftDel
kbBack = _tv.kbBack
kbCtrlBack = _tv.kbCtrlBack
kbShiftTab = _tv.kbShiftTab
kbTab = _tv.kbTab
kbAltA = _tv.kbAltA
kbAltB = _tv.kbAltB
kbAltC = _tv.kbAltC
kbAltD = _tv.kbAltD
kbAltE = _tv.kbAltE
kbAltF = _tv.kbAltF
kbAltG = _tv.kbAltG
kbAltH = _tv.kbAltH
kbAltI = _tv.kbAltI
kbAltJ = _tv.kbAltJ
kbAltK = _tv.kbAltK
kbAltL = _tv.kbAltL
kbAltM = _tv.kbAltM
kbAltN = _tv.kbAltN
kbAltO = _tv.kbAltO
kbAltP = _tv.kbAltP
kbAltQ = _tv.kbAltQ
kbAltR = _tv.kbAltR
kbAltS = _tv.kbAltS
kbAltT = _tv.kbAltT
kbAltU = _tv.kbAltU
kbAltV = _tv.kbAltV
kbAltW = _tv.kbAltW
kbAltX = _tv.kbAltX
kbAltY = _tv.kbAltY
kbAltZ = _tv.kbAltZ
kbCtrlEnter = _tv.kbCtrlEnter
kbEnter = _tv.kbEnter
kbF1 = _tv.kbF1
kbF2 = _tv.kbF2
kbF3 = _tv.kbF3
kbF4 = _tv.kbF4
kbF5 = _tv.kbF5
kbF6 = _tv.kbF6
kbF7 = _tv.kbF7
kbF8 = _tv.kbF8
kbF9 = _tv.kbF9
kbF10 = _tv.kbF10
kbF11 = _tv.kbF11
kbF12 = _tv.kbF12
kbHome = _tv.kbHome
kbUp = _tv.kbUp
kbPgUp = _tv.kbPgUp
kbLeft = _tv.kbLeft
kbRight = _tv.kbRight
kbEnd = _tv.kbEnd
kbDown = _tv.kbDown
kbPgDn = _tv.kbPgDn
kbIns = _tv.kbIns
kbDel = _tv.kbDel
kbGrayMinus = _tv.kbGrayMinus
kbGrayPlus = _tv.kbGrayPlus
kbShiftF1 = _tv.kbShiftF1
kbShiftF2 = _tv.kbShiftF2
kbShiftF3 = _tv.kbShiftF3
kbShiftF4 = _tv.kbShiftF4
kbShiftF5 = _tv.kbShiftF5
kbShiftF6 = _tv.kbShiftF6
kbShiftF7 = _tv.kbShiftF7
kbShiftF8 = _tv.kbShiftF8
kbShiftF9 = _tv.kbShiftF9
kbShiftF10 = _tv.kbShiftF10
kbShiftF11 = _tv.kbShiftF11
kbShiftF12 = _tv.kbShiftF12
kbCtrlF1 = _tv.kbCtrlF1
kbCtrlF2 = _tv.kbCtrlF2
kbCtrlF3 = _tv.kbCtrlF3
kbCtrlF4 = _tv.kbCtrlF4
kbCtrlF5 = _tv.kbCtrlF5
kbCtrlF6 = _tv.kbCtrlF6
kbCtrlF7 = _tv.kbCtrlF7
kbCtrlF8 = _tv.kbCtrlF8
kbCtrlF9 = _tv.kbCtrlF9
kbCtrlF10 = _tv.kbCtrlF10
kbCtrlF11 = _tv.kbCtrlF11
kbCtrlF12 = _tv.kbCtrlF12
kbAltF1 = _tv.kbAltF1
kbAltF2 = _tv.kbAltF2
kbAltF3 = _tv.kbAltF3
kbAltF4 = _tv.kbAltF4
kbAltF5 = _tv.kbAltF5
kbAltF6 = _tv.kbAltF6
kbAltF7 = _tv.kbAltF7
kbAltF8 = _tv.kbAltF8
kbAltF9 = _tv.kbAltF9
kbAltF10 = _tv.kbAltF10
kbAltF11 = _tv.kbAltF11
kbAltF12 = _tv.kbAltF12
kbCtrlPrtSc = _tv.kbCtrlPrtSc
kbCtrlLeft = _tv.kbCtrlLeft
kbCtrlRight = _tv.kbCtrlRight
kbCtrlEnd = _tv.kbCtrlEnd
kbCtrlPgDn = _tv.kbCtrlPgDn
kbCtrlHome = _tv.kbCtrlHome
kbAlt1 = _tv.kbAlt1
kbAlt2 = _tv.kbAlt2
kbAlt3 = _tv.kbAlt3
kbAlt4 = _tv.kbAlt4
kbAlt5 = _tv.kbAlt5
kbAlt6 = _tv.kbAlt6
kbAlt7 = _tv.kbAlt7
kbAlt8 = _tv.kbAlt8
kbAlt9 = _tv.kbAlt9
kbAlt0 = _tv.kbAlt0
kbAltMinus = _tv.kbAltMinus
kbAltEqual = _tv.kbAltEqual
kbCtrlPgUp = _tv.kbCtrlPgUp
kbNoKey = _tv.kbNoKey
kbAltBack = _tv.kbAltBack
kbRightShift = _tv.kbRightShift
kbLeftShift = _tv.kbLeftShift
kbShift = _tv.kbShift
kbLeftCtrl = _tv.kbLeftCtrl
kbRightCtrl = _tv.kbRightCtrl
kbCtrlShift = _tv.kbCtrlShift
kbLeftAlt = _tv.kbLeftAlt
kbRightAlt = _tv.kbRightAlt
kbAltShift = _tv.kbAltShift
kbScrollState = _tv.kbScrollState
kbNumState = _tv.kbNumState
kbCapsState = _tv.kbCapsState
kbInsState = _tv.kbInsState
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
        _swig_setattr(self, TDialog, 'this', _tv.new_TDialog(*args))
        _swig_setattr(self, TDialog, 'thisown', 1)
    def getPalette(*args): return _tv.TDialog_getPalette(*args)
    def handleEvent(*args): return _tv.TDialog_handleEvent(*args)
    def valid(*args): return _tv.TDialog_valid(*args)
    def __del__(self, destroy=_tv.delete_TDialog):
        try:
            if self.thisown: destroy(self)
        except: pass

class TDialogPtr(TDialog):
    def __init__(self, this):
        _swig_setattr(self, TDialog, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TDialog, 'thisown', 0)
        _swig_setattr(self, TDialog,self.__class__,TDialog)
_tv.TDialog_swigregister(TDialogPtr)

fdOKButton = _tv.fdOKButton
fdOpenButton = _tv.fdOpenButton
fdReplaceButton = _tv.fdReplaceButton
fdClearButton = _tv.fdClearButton
fdHelpButton = _tv.fdHelpButton
fdSelectButton = _tv.fdSelectButton
fdDoneButton = _tv.fdDoneButton
fdAddButton = _tv.fdAddButton
fdNoLoadDir = _tv.fdNoLoadDir
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
        _swig_setattr(self, TFileDialog, 'this', _tv.new_TFileDialog(*args))
        _swig_setattr(self, TFileDialog, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TFileDialog):
        try:
            if self.thisown: destroy(self)
        except: pass
    def getData(*args): return _tv.TFileDialog_getData(*args)
    def getFileName(*args): return _tv.TFileDialog_getFileName(*args)
    def handleEvent(*args): return _tv.TFileDialog_handleEvent(*args)
    def setData(*args): return _tv.TFileDialog_setData(*args)
    def valid(*args): return _tv.TFileDialog_valid(*args)
    def shutDown(*args): return _tv.TFileDialog_shutDown(*args)
    def sizeLimits(*args): return _tv.TFileDialog_sizeLimits(*args)
    __swig_setmethods__["fileName"] = _tv.TFileDialog_fileName_set
    __swig_getmethods__["fileName"] = _tv.TFileDialog_fileName_get
    if _newclass:fileName = property(_tv.TFileDialog_fileName_get, _tv.TFileDialog_fileName_set)
    __swig_setmethods__["fileList"] = _tv.TFileDialog_fileList_set
    __swig_getmethods__["fileList"] = _tv.TFileDialog_fileList_get
    if _newclass:fileList = property(_tv.TFileDialog_fileList_get, _tv.TFileDialog_fileList_set)
    __swig_setmethods__["wildCard"] = _tv.TFileDialog_wildCard_set
    __swig_getmethods__["wildCard"] = _tv.TFileDialog_wildCard_get
    if _newclass:wildCard = property(_tv.TFileDialog_wildCard_get, _tv.TFileDialog_wildCard_set)
    __swig_setmethods__["directory"] = _tv.TFileDialog_directory_set
    __swig_getmethods__["directory"] = _tv.TFileDialog_directory_get
    if _newclass:directory = property(_tv.TFileDialog_directory_get, _tv.TFileDialog_directory_set)

class TFileDialogPtr(TFileDialog):
    def __init__(self, this):
        _swig_setattr(self, TFileDialog, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TFileDialog, 'thisown', 0)
        _swig_setattr(self, TFileDialog,self.__class__,TFileDialog)
_tv.TFileDialog_swigregister(TFileDialogPtr)

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
        _swig_setattr(self, TEditorApp, 'this', _tv.new_TEditorApp(*args))
        _swig_setattr(self, TEditorApp, 'thisown', 1)
    def handleEvent(*args): return _tv.TEditorApp_handleEvent(*args)
    __swig_getmethods__["initMenuBar"] = lambda x: _tv.TEditorApp_initMenuBar
    if _newclass:initMenuBar = staticmethod(_tv.TEditorApp_initMenuBar)
    __swig_getmethods__["initStatusLine"] = lambda x: _tv.TEditorApp_initStatusLine
    if _newclass:initStatusLine = staticmethod(_tv.TEditorApp_initStatusLine)
    def outOfMemory(*args): return _tv.TEditorApp_outOfMemory(*args)
    def openEditor(*args): return _tv.TEditorApp_openEditor(*args)
    def __del__(self, destroy=_tv.delete_TEditorApp):
        try:
            if self.thisown: destroy(self)
        except: pass

class TEditorAppPtr(TEditorApp):
    def __init__(self, this):
        _swig_setattr(self, TEditorApp, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TEditorApp, 'thisown', 0)
        _swig_setattr(self, TEditorApp,self.__class__,TEditorApp)
_tv.TEditorApp_swigregister(TEditorAppPtr)

TEditorApp_initMenuBar = _tv.TEditorApp_initMenuBar

TEditorApp_initStatusLine = _tv.TEditorApp_initStatusLine


execDialog = _tv.execDialog

createFindDialog = _tv.createFindDialog

createReplaceDialog = _tv.createReplaceDialog
bfNormal = _tv.bfNormal
bfDefault = _tv.bfDefault
bfLeftJust = _tv.bfLeftJust
bfBroadcast = _tv.bfBroadcast

messageBox = _tv.messageBox

messageBoxRect = _tv.messageBoxRect

inputBox = _tv.inputBox

inputBoxRect = _tv.inputBoxRect
mfWarning = _tv.mfWarning
mfError = _tv.mfError
mfInformation = _tv.mfInformation
mfConfirmation = _tv.mfConfirmation
mfYesButton = _tv.mfYesButton
mfNoButton = _tv.mfNoButton
mfOKButton = _tv.mfOKButton
mfCancelButton = _tv.mfCancelButton
mfDontTranslate = _tv.mfDontTranslate
mfDontShowAgain = _tv.mfDontShowAgain
mfYesNoCancel = _tv.mfYesNoCancel
mfOKCancel = _tv.mfOKCancel
class MsgBoxText(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MsgBoxText, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MsgBoxText, name)
    def __repr__(self):
        return "<C MsgBoxText instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, MsgBoxText, 'this', _tv.new_MsgBoxText(*args))
        _swig_setattr(self, MsgBoxText, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_MsgBoxText):
        try:
            if self.thisown: destroy(self)
        except: pass

class MsgBoxTextPtr(MsgBoxText):
    def __init__(self, this):
        _swig_setattr(self, MsgBoxText, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, MsgBoxText, 'thisown', 0)
        _swig_setattr(self, MsgBoxText,self.__class__,MsgBoxText)
_tv.MsgBoxText_swigregister(MsgBoxTextPtr)

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
        _swig_setattr(self, TListViewer, 'this', _tv.new_TListViewer(*args))
        _swig_setattr(self, TListViewer, 'thisown', 1)
    def changeBounds(*args): return _tv.TListViewer_changeBounds(*args)
    def draw(*args): return _tv.TListViewer_draw(*args)
    def focusItem(*args): return _tv.TListViewer_focusItem(*args)
    def getPalette(*args): return _tv.TListViewer_getPalette(*args)
    def getText(*args): return _tv.TListViewer_getText(*args)
    def isSelected(*args): return _tv.TListViewer_isSelected(*args)
    def handleEvent(*args): return _tv.TListViewer_handleEvent(*args)
    def selectItem(*args): return _tv.TListViewer_selectItem(*args)
    def setRange(*args): return _tv.TListViewer_setRange(*args)
    def setState(*args): return _tv.TListViewer_setState(*args)
    def focusItemNum(*args): return _tv.TListViewer_focusItemNum(*args)
    def shutDown(*args): return _tv.TListViewer_shutDown(*args)
    __swig_setmethods__["hScrollBar"] = _tv.TListViewer_hScrollBar_set
    __swig_getmethods__["hScrollBar"] = _tv.TListViewer_hScrollBar_get
    if _newclass:hScrollBar = property(_tv.TListViewer_hScrollBar_get, _tv.TListViewer_hScrollBar_set)
    __swig_setmethods__["vScrollBar"] = _tv.TListViewer_vScrollBar_set
    __swig_getmethods__["vScrollBar"] = _tv.TListViewer_vScrollBar_get
    if _newclass:vScrollBar = property(_tv.TListViewer_vScrollBar_get, _tv.TListViewer_vScrollBar_set)
    __swig_setmethods__["numCols"] = _tv.TListViewer_numCols_set
    __swig_getmethods__["numCols"] = _tv.TListViewer_numCols_get
    if _newclass:numCols = property(_tv.TListViewer_numCols_get, _tv.TListViewer_numCols_set)
    __swig_setmethods__["topItem"] = _tv.TListViewer_topItem_set
    __swig_getmethods__["topItem"] = _tv.TListViewer_topItem_get
    if _newclass:topItem = property(_tv.TListViewer_topItem_get, _tv.TListViewer_topItem_set)
    __swig_setmethods__["focused"] = _tv.TListViewer_focused_set
    __swig_getmethods__["focused"] = _tv.TListViewer_focused_get
    if _newclass:focused = property(_tv.TListViewer_focused_get, _tv.TListViewer_focused_set)
    __swig_setmethods__["range"] = _tv.TListViewer_range_set
    __swig_getmethods__["range"] = _tv.TListViewer_range_get
    if _newclass:range = property(_tv.TListViewer_range_get, _tv.TListViewer_range_set)
    __swig_setmethods__["handleSpace"] = _tv.TListViewer_handleSpace_set
    __swig_getmethods__["handleSpace"] = _tv.TListViewer_handleSpace_get
    if _newclass:handleSpace = property(_tv.TListViewer_handleSpace_get, _tv.TListViewer_handleSpace_set)
    def getExtraOptions(*args): return _tv.TListViewer_getExtraOptions(*args)
    def setExtraOptions(*args): return _tv.TListViewer_setExtraOptions(*args)
    def __del__(self, destroy=_tv.delete_TListViewer):
        try:
            if self.thisown: destroy(self)
        except: pass

class TListViewerPtr(TListViewer):
    def __init__(self, this):
        _swig_setattr(self, TListViewer, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TListViewer, 'thisown', 0)
        _swig_setattr(self, TListViewer,self.__class__,TListViewer)
_tv.TListViewer_swigregister(TListViewerPtr)

class TListBoxRec(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TListBoxRec, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TListBoxRec, name)
    def __repr__(self):
        return "<C TListBoxRec instance at %s>" % (self.this,)
    __swig_setmethods__["items"] = _tv.TListBoxRec_items_set
    __swig_getmethods__["items"] = _tv.TListBoxRec_items_get
    if _newclass:items = property(_tv.TListBoxRec_items_get, _tv.TListBoxRec_items_set)
    __swig_setmethods__["selection"] = _tv.TListBoxRec_selection_set
    __swig_getmethods__["selection"] = _tv.TListBoxRec_selection_get
    if _newclass:selection = property(_tv.TListBoxRec_selection_get, _tv.TListBoxRec_selection_set)
    def __init__(self, *args):
        _swig_setattr(self, TListBoxRec, 'this', _tv.new_TListBoxRec(*args))
        _swig_setattr(self, TListBoxRec, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TListBoxRec):
        try:
            if self.thisown: destroy(self)
        except: pass

class TListBoxRecPtr(TListBoxRec):
    def __init__(self, this):
        _swig_setattr(self, TListBoxRec, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TListBoxRec, 'thisown', 0)
        _swig_setattr(self, TListBoxRec,self.__class__,TListBoxRec)
_tv.TListBoxRec_swigregister(TListBoxRecPtr)

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
        _swig_setattr(self, TListBox, 'this', _tv.new_TListBox(*args))
        _swig_setattr(self, TListBox, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TListBox):
        try:
            if self.thisown: destroy(self)
        except: pass
    def dataSize(*args): return _tv.TListBox_dataSize(*args)
    def getData(*args): return _tv.TListBox_getData(*args)
    def getText(*args): return _tv.TListBox_getText(*args)
    def newList(*args): return _tv.TListBox_newList(*args)
    def newList(self, p):
        p.thisown = 0
        return _tv.TListBox_newList(self, p)

    def setData(*args): return _tv.TListBox_setData(*args)
    def list(*args): return _tv.TListBox_list(*args)

class TListBoxPtr(TListBox):
    def __init__(self, this):
        _swig_setattr(self, TListBox, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TListBox, 'thisown', 0)
        _swig_setattr(self, TListBox,self.__class__,TListBox)
_tv.TListBox_swigregister(TListBoxPtr)

ufUpdate = _tv.ufUpdate
ufLine = _tv.ufLine
ufView = _tv.ufView
smExtend = _tv.smExtend
smDouble = _tv.smDouble
sfSearchFailed = _tv.sfSearchFailed
cmSave = _tv.cmSave
cmSaveAs = _tv.cmSaveAs
cmFind = _tv.cmFind
cmReplace = _tv.cmReplace
cmSearchAgain = _tv.cmSearchAgain
cmCharLeft = _tv.cmCharLeft
cmCharRight = _tv.cmCharRight
cmWordLeft = _tv.cmWordLeft
cmWordRight = _tv.cmWordRight
cmLineStart = _tv.cmLineStart
cmLineEnd = _tv.cmLineEnd
cmLineUp = _tv.cmLineUp
cmLineDown = _tv.cmLineDown
cmPageUp = _tv.cmPageUp
cmPageDown = _tv.cmPageDown
cmTextStart = _tv.cmTextStart
cmTextEnd = _tv.cmTextEnd
cmNewLine = _tv.cmNewLine
cmBackSpace = _tv.cmBackSpace
cmDelChar = _tv.cmDelChar
cmDelWord = _tv.cmDelWord
cmDelStart = _tv.cmDelStart
cmDelEnd = _tv.cmDelEnd
cmDelLine = _tv.cmDelLine
cmInsMode = _tv.cmInsMode
cmStartSelect = _tv.cmStartSelect
cmHideSelect = _tv.cmHideSelect
cmIndentMode = _tv.cmIndentMode
cmUpdateTitle = _tv.cmUpdateTitle
cmInsertText = _tv.cmInsertText
edOutOfMemory = _tv.edOutOfMemory
edReadError = _tv.edReadError
edWriteError = _tv.edWriteError
edCreateError = _tv.edCreateError
edSaveModify = _tv.edSaveModify
edSaveUntitled = _tv.edSaveUntitled
edSaveAs = _tv.edSaveAs
edFind = _tv.edFind
edSearchFailed = _tv.edSearchFailed
edReplace = _tv.edReplace
edReplacePrompt = _tv.edReplacePrompt
efCaseSensitive = _tv.efCaseSensitive
efWholeWordsOnly = _tv.efWholeWordsOnly
efPromptOnReplace = _tv.efPromptOnReplace
efReplaceAll = _tv.efReplaceAll
efDoReplace = _tv.efDoReplace
efBackupFiles = _tv.efBackupFiles
cmOpen = _tv.cmOpen
cmNew = _tv.cmNew
cmChangeDrct = _tv.cmChangeDrct
cmDosShell = _tv.cmDosShell
cmCalculator = _tv.cmCalculator
cmShowClip = _tv.cmShowClip
cmMacros = _tv.cmMacros

defEditorDialog = _tv.defEditorDialog
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
        _swig_setattr(self, TIndicator, 'this', _tv.new_TIndicator(*args))
        _swig_setattr(self, TIndicator, 'thisown', 1)
    def draw(*args): return _tv.TIndicator_draw(*args)
    def getPalette(*args): return _tv.TIndicator_getPalette(*args)
    def setState(*args): return _tv.TIndicator_setState(*args)
    def setValue(*args): return _tv.TIndicator_setValue(*args)
    def __del__(self, destroy=_tv.delete_TIndicator):
        try:
            if self.thisown: destroy(self)
        except: pass

class TIndicatorPtr(TIndicator):
    def __init__(self, this):
        _swig_setattr(self, TIndicator, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TIndicator, 'thisown', 0)
        _swig_setattr(self, TIndicator,self.__class__,TIndicator)
_tv.TIndicator_swigregister(TIndicatorPtr)
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
        _swig_setattr(self, TEditor, 'this', _tv.new_TEditor(*args))
        _swig_setattr(self, TEditor, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TEditor):
        try:
            if self.thisown: destroy(self)
        except: pass
    def shutDown(*args): return _tv.TEditor_shutDown(*args)
    def bufChar(*args): return _tv.TEditor_bufChar(*args)
    def bufPtr(*args): return _tv.TEditor_bufPtr(*args)
    def changeBounds(*args): return _tv.TEditor_changeBounds(*args)
    def convertEvent(*args): return _tv.TEditor_convertEvent(*args)
    def cursorVisible(*args): return _tv.TEditor_cursorVisible(*args)
    def deleteSelect(*args): return _tv.TEditor_deleteSelect(*args)
    def doneBuffer(*args): return _tv.TEditor_doneBuffer(*args)
    def draw(*args): return _tv.TEditor_draw(*args)
    def getPalette(*args): return _tv.TEditor_getPalette(*args)
    def handleEvent(*args): return _tv.TEditor_handleEvent(*args)
    def initBuffer(*args): return _tv.TEditor_initBuffer(*args)
    def insertBuffer(*args): return _tv.TEditor_insertBuffer(*args)
    def insertFrom(*args): return _tv.TEditor_insertFrom(*args)
    def insertText(*args): return _tv.TEditor_insertText(*args)
    def scrollTo(*args): return _tv.TEditor_scrollTo(*args)
    def search(*args): return _tv.TEditor_search(*args)
    def setBufSize(*args): return _tv.TEditor_setBufSize(*args)
    def setCmdState(*args): return _tv.TEditor_setCmdState(*args)
    def setSelect(*args): return _tv.TEditor_setSelect(*args)
    def setState(*args): return _tv.TEditor_setState(*args)
    def trackCursor(*args): return _tv.TEditor_trackCursor(*args)
    def undo(*args): return _tv.TEditor_undo(*args)
    def updateCommands(*args): return _tv.TEditor_updateCommands(*args)
    def valid(*args): return _tv.TEditor_valid(*args)
    def charPos(*args): return _tv.TEditor_charPos(*args)
    def charPtr(*args): return _tv.TEditor_charPtr(*args)
    def clipCopy(*args): return _tv.TEditor_clipCopy(*args)
    def clipCut(*args): return _tv.TEditor_clipCut(*args)
    def clipPaste(*args): return _tv.TEditor_clipPaste(*args)
    def deleteRange(*args): return _tv.TEditor_deleteRange(*args)
    def doUpdate(*args): return _tv.TEditor_doUpdate(*args)
    def doSearchReplace(*args): return _tv.TEditor_doSearchReplace(*args)
    def drawLines(*args): return _tv.TEditor_drawLines(*args)
    def formatLine(*args): return _tv.TEditor_formatLine(*args)
    def find(*args): return _tv.TEditor_find(*args)
    def getMousePtr(*args): return _tv.TEditor_getMousePtr(*args)
    def hasSelection(*args): return _tv.TEditor_hasSelection(*args)
    def hideSelect(*args): return _tv.TEditor_hideSelect(*args)
    def isClipboard(*args): return _tv.TEditor_isClipboard(*args)
    def lineEnd(*args): return _tv.TEditor_lineEnd(*args)
    def lineMove(*args): return _tv.TEditor_lineMove(*args)
    def lineStart(*args): return _tv.TEditor_lineStart(*args)
    def lock(*args): return _tv.TEditor_lock(*args)
    def newLine(*args): return _tv.TEditor_newLine(*args)
    def nextChar(*args): return _tv.TEditor_nextChar(*args)
    def nextLine(*args): return _tv.TEditor_nextLine(*args)
    def nextWord(*args): return _tv.TEditor_nextWord(*args)
    def prevChar(*args): return _tv.TEditor_prevChar(*args)
    def prevLine(*args): return _tv.TEditor_prevLine(*args)
    def prevWord(*args): return _tv.TEditor_prevWord(*args)
    def replace(*args): return _tv.TEditor_replace(*args)
    def setBufLen(*args): return _tv.TEditor_setBufLen(*args)
    def setCurPtr(*args): return _tv.TEditor_setCurPtr(*args)
    def startSelect(*args): return _tv.TEditor_startSelect(*args)
    def toggleInsMode(*args): return _tv.TEditor_toggleInsMode(*args)
    def unlock(*args): return _tv.TEditor_unlock(*args)
    def update(*args): return _tv.TEditor_update(*args)
    def checkScrollBar(*args): return _tv.TEditor_checkScrollBar(*args)
    __swig_setmethods__["hScrollBar"] = _tv.TEditor_hScrollBar_set
    __swig_getmethods__["hScrollBar"] = _tv.TEditor_hScrollBar_get
    if _newclass:hScrollBar = property(_tv.TEditor_hScrollBar_get, _tv.TEditor_hScrollBar_set)
    __swig_setmethods__["vScrollBar"] = _tv.TEditor_vScrollBar_set
    __swig_getmethods__["vScrollBar"] = _tv.TEditor_vScrollBar_get
    if _newclass:vScrollBar = property(_tv.TEditor_vScrollBar_get, _tv.TEditor_vScrollBar_set)
    __swig_setmethods__["indicator"] = _tv.TEditor_indicator_set
    __swig_getmethods__["indicator"] = _tv.TEditor_indicator_get
    if _newclass:indicator = property(_tv.TEditor_indicator_get, _tv.TEditor_indicator_set)
    __swig_setmethods__["buffer"] = _tv.TEditor_buffer_set
    __swig_getmethods__["buffer"] = _tv.TEditor_buffer_get
    if _newclass:buffer = property(_tv.TEditor_buffer_get, _tv.TEditor_buffer_set)
    __swig_setmethods__["bufSize"] = _tv.TEditor_bufSize_set
    __swig_getmethods__["bufSize"] = _tv.TEditor_bufSize_get
    if _newclass:bufSize = property(_tv.TEditor_bufSize_get, _tv.TEditor_bufSize_set)
    __swig_setmethods__["bufLen"] = _tv.TEditor_bufLen_set
    __swig_getmethods__["bufLen"] = _tv.TEditor_bufLen_get
    if _newclass:bufLen = property(_tv.TEditor_bufLen_get, _tv.TEditor_bufLen_set)
    __swig_setmethods__["gapLen"] = _tv.TEditor_gapLen_set
    __swig_getmethods__["gapLen"] = _tv.TEditor_gapLen_get
    if _newclass:gapLen = property(_tv.TEditor_gapLen_get, _tv.TEditor_gapLen_set)
    __swig_setmethods__["selStart"] = _tv.TEditor_selStart_set
    __swig_getmethods__["selStart"] = _tv.TEditor_selStart_get
    if _newclass:selStart = property(_tv.TEditor_selStart_get, _tv.TEditor_selStart_set)
    __swig_setmethods__["selEnd"] = _tv.TEditor_selEnd_set
    __swig_getmethods__["selEnd"] = _tv.TEditor_selEnd_get
    if _newclass:selEnd = property(_tv.TEditor_selEnd_get, _tv.TEditor_selEnd_set)
    __swig_setmethods__["curPtr"] = _tv.TEditor_curPtr_set
    __swig_getmethods__["curPtr"] = _tv.TEditor_curPtr_get
    if _newclass:curPtr = property(_tv.TEditor_curPtr_get, _tv.TEditor_curPtr_set)
    __swig_setmethods__["curPos"] = _tv.TEditor_curPos_set
    __swig_getmethods__["curPos"] = _tv.TEditor_curPos_get
    if _newclass:curPos = property(_tv.TEditor_curPos_get, _tv.TEditor_curPos_set)
    __swig_setmethods__["delta"] = _tv.TEditor_delta_set
    __swig_getmethods__["delta"] = _tv.TEditor_delta_get
    if _newclass:delta = property(_tv.TEditor_delta_get, _tv.TEditor_delta_set)
    __swig_setmethods__["limit"] = _tv.TEditor_limit_set
    __swig_getmethods__["limit"] = _tv.TEditor_limit_get
    if _newclass:limit = property(_tv.TEditor_limit_get, _tv.TEditor_limit_set)
    __swig_setmethods__["drawLine"] = _tv.TEditor_drawLine_set
    __swig_getmethods__["drawLine"] = _tv.TEditor_drawLine_get
    if _newclass:drawLine = property(_tv.TEditor_drawLine_get, _tv.TEditor_drawLine_set)
    __swig_setmethods__["drawPtr"] = _tv.TEditor_drawPtr_set
    __swig_getmethods__["drawPtr"] = _tv.TEditor_drawPtr_get
    if _newclass:drawPtr = property(_tv.TEditor_drawPtr_get, _tv.TEditor_drawPtr_set)
    __swig_setmethods__["delCount"] = _tv.TEditor_delCount_set
    __swig_getmethods__["delCount"] = _tv.TEditor_delCount_get
    if _newclass:delCount = property(_tv.TEditor_delCount_get, _tv.TEditor_delCount_set)
    __swig_setmethods__["insCount"] = _tv.TEditor_insCount_set
    __swig_getmethods__["insCount"] = _tv.TEditor_insCount_get
    if _newclass:insCount = property(_tv.TEditor_insCount_get, _tv.TEditor_insCount_set)
    __swig_setmethods__["isValid"] = _tv.TEditor_isValid_set
    __swig_getmethods__["isValid"] = _tv.TEditor_isValid_get
    if _newclass:isValid = property(_tv.TEditor_isValid_get, _tv.TEditor_isValid_set)
    __swig_setmethods__["canUndo"] = _tv.TEditor_canUndo_set
    __swig_getmethods__["canUndo"] = _tv.TEditor_canUndo_get
    if _newclass:canUndo = property(_tv.TEditor_canUndo_get, _tv.TEditor_canUndo_set)
    __swig_setmethods__["modified"] = _tv.TEditor_modified_set
    __swig_getmethods__["modified"] = _tv.TEditor_modified_get
    if _newclass:modified = property(_tv.TEditor_modified_get, _tv.TEditor_modified_set)
    __swig_setmethods__["selecting"] = _tv.TEditor_selecting_set
    __swig_getmethods__["selecting"] = _tv.TEditor_selecting_get
    if _newclass:selecting = property(_tv.TEditor_selecting_get, _tv.TEditor_selecting_set)
    __swig_setmethods__["overwrite"] = _tv.TEditor_overwrite_set
    __swig_getmethods__["overwrite"] = _tv.TEditor_overwrite_get
    if _newclass:overwrite = property(_tv.TEditor_overwrite_get, _tv.TEditor_overwrite_set)
    __swig_setmethods__["autoIndent"] = _tv.TEditor_autoIndent_set
    __swig_getmethods__["autoIndent"] = _tv.TEditor_autoIndent_get
    if _newclass:autoIndent = property(_tv.TEditor_autoIndent_get, _tv.TEditor_autoIndent_set)
    __swig_setmethods__["lockCount"] = _tv.TEditor_lockCount_set
    __swig_getmethods__["lockCount"] = _tv.TEditor_lockCount_get
    if _newclass:lockCount = property(_tv.TEditor_lockCount_get, _tv.TEditor_lockCount_set)
    __swig_setmethods__["updateFlags"] = _tv.TEditor_updateFlags_set
    __swig_getmethods__["updateFlags"] = _tv.TEditor_updateFlags_get
    if _newclass:updateFlags = property(_tv.TEditor_updateFlags_get, _tv.TEditor_updateFlags_set)
    __swig_setmethods__["keyState"] = _tv.TEditor_keyState_set
    __swig_getmethods__["keyState"] = _tv.TEditor_keyState_get
    if _newclass:keyState = property(_tv.TEditor_keyState_get, _tv.TEditor_keyState_set)

class TEditorPtr(TEditor):
    def __init__(self, this):
        _swig_setattr(self, TEditor, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TEditor, 'thisown', 0)
        _swig_setattr(self, TEditor,self.__class__,TEditor)
_tv.TEditor_swigregister(TEditorPtr)

class TMemoData(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TMemoData, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TMemoData, name)
    def __repr__(self):
        return "<C TMemoData instance at %s>" % (self.this,)
    __swig_setmethods__["length"] = _tv.TMemoData_length_set
    __swig_getmethods__["length"] = _tv.TMemoData_length_get
    if _newclass:length = property(_tv.TMemoData_length_get, _tv.TMemoData_length_set)
    __swig_setmethods__["buffer"] = _tv.TMemoData_buffer_set
    __swig_getmethods__["buffer"] = _tv.TMemoData_buffer_get
    if _newclass:buffer = property(_tv.TMemoData_buffer_get, _tv.TMemoData_buffer_set)
    def __init__(self, *args):
        _swig_setattr(self, TMemoData, 'this', _tv.new_TMemoData(*args))
        _swig_setattr(self, TMemoData, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TMemoData):
        try:
            if self.thisown: destroy(self)
        except: pass

class TMemoDataPtr(TMemoData):
    def __init__(self, this):
        _swig_setattr(self, TMemoData, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TMemoData, 'thisown', 0)
        _swig_setattr(self, TMemoData,self.__class__,TMemoData)
_tv.TMemoData_swigregister(TMemoDataPtr)

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
        _swig_setattr(self, TMemo, 'this', _tv.new_TMemo(*args))
        _swig_setattr(self, TMemo, 'thisown', 1)
    def getData(*args): return _tv.TMemo_getData(*args)
    def setData(*args): return _tv.TMemo_setData(*args)
    def dataSize(*args): return _tv.TMemo_dataSize(*args)
    def getPalette(*args): return _tv.TMemo_getPalette(*args)
    def handleEvent(*args): return _tv.TMemo_handleEvent(*args)
    def __del__(self, destroy=_tv.delete_TMemo):
        try:
            if self.thisown: destroy(self)
        except: pass

class TMemoPtr(TMemo):
    def __init__(self, this):
        _swig_setattr(self, TMemo, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TMemo, 'thisown', 0)
        _swig_setattr(self, TMemo,self.__class__,TMemo)
_tv.TMemo_swigregister(TMemoPtr)

class TFileEditor(TEditor):
    __swig_setmethods__ = {}
    for _s in [TEditor]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TFileEditor, name, value)
    __swig_getmethods__ = {}
    for _s in [TEditor]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TFileEditor, name)
    def __repr__(self):
        return "<C TFileEditor instance at %s>" % (self.this,)
    __swig_setmethods__["fileName"] = _tv.TFileEditor_fileName_set
    __swig_getmethods__["fileName"] = _tv.TFileEditor_fileName_get
    if _newclass:fileName = property(_tv.TFileEditor_fileName_get, _tv.TFileEditor_fileName_set)
    def __init__(self, *args):
        _swig_setattr(self, TFileEditor, 'this', _tv.new_TFileEditor(*args))
        _swig_setattr(self, TFileEditor, 'thisown', 1)
    def doneBuffer(*args): return _tv.TFileEditor_doneBuffer(*args)
    def handleEvent(*args): return _tv.TFileEditor_handleEvent(*args)
    def initBuffer(*args): return _tv.TFileEditor_initBuffer(*args)
    def loadFile(*args): return _tv.TFileEditor_loadFile(*args)
    def save(*args): return _tv.TFileEditor_save(*args)
    def saveAs(*args): return _tv.TFileEditor_saveAs(*args)
    def saveFile(*args): return _tv.TFileEditor_saveFile(*args)
    def setBufSize(*args): return _tv.TFileEditor_setBufSize(*args)
    def shutDown(*args): return _tv.TFileEditor_shutDown(*args)
    def updateCommands(*args): return _tv.TFileEditor_updateCommands(*args)
    def valid(*args): return _tv.TFileEditor_valid(*args)
    def __del__(self, destroy=_tv.delete_TFileEditor):
        try:
            if self.thisown: destroy(self)
        except: pass

class TFileEditorPtr(TFileEditor):
    def __init__(self, this):
        _swig_setattr(self, TFileEditor, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TFileEditor, 'thisown', 0)
        _swig_setattr(self, TFileEditor,self.__class__,TFileEditor)
_tv.TFileEditor_swigregister(TFileEditorPtr)

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
        _swig_setattr(self, TEditWindow, 'this', _tv.new_TEditWindow(*args))
        _swig_setattr(self, TEditWindow, 'thisown', 1)
    def close(*args): return _tv.TEditWindow_close(*args)
    def getTitle(*args): return _tv.TEditWindow_getTitle(*args)
    def handleEvent(*args): return _tv.TEditWindow_handleEvent(*args)
    def sizeLimits(*args): return _tv.TEditWindow_sizeLimits(*args)
    __swig_setmethods__["editor"] = _tv.TEditWindow_editor_set
    __swig_getmethods__["editor"] = _tv.TEditWindow_editor_get
    if _newclass:editor = property(_tv.TEditWindow_editor_get, _tv.TEditWindow_editor_set)
    def __del__(self, destroy=_tv.delete_TEditWindow):
        try:
            if self.thisown: destroy(self)
        except: pass

class TEditWindowPtr(TEditWindow):
    def __init__(self, this):
        _swig_setattr(self, TEditWindow, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TEditWindow, 'thisown', 0)
        _swig_setattr(self, TEditWindow,self.__class__,TEditWindow)
_tv.TEditWindow_swigregister(TEditWindowPtr)

class TFindDialogRec(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TFindDialogRec, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TFindDialogRec, name)
    def __repr__(self):
        return "<C TFindDialogRec instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TFindDialogRec, 'this', _tv.new_TFindDialogRec(*args))
        _swig_setattr(self, TFindDialogRec, 'thisown', 1)
    __swig_setmethods__["find"] = _tv.TFindDialogRec_find_set
    __swig_getmethods__["find"] = _tv.TFindDialogRec_find_get
    if _newclass:find = property(_tv.TFindDialogRec_find_get, _tv.TFindDialogRec_find_set)
    __swig_setmethods__["options"] = _tv.TFindDialogRec_options_set
    __swig_getmethods__["options"] = _tv.TFindDialogRec_options_get
    if _newclass:options = property(_tv.TFindDialogRec_options_get, _tv.TFindDialogRec_options_set)
    def __del__(self, destroy=_tv.delete_TFindDialogRec):
        try:
            if self.thisown: destroy(self)
        except: pass

class TFindDialogRecPtr(TFindDialogRec):
    def __init__(self, this):
        _swig_setattr(self, TFindDialogRec, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TFindDialogRec, 'thisown', 0)
        _swig_setattr(self, TFindDialogRec,self.__class__,TFindDialogRec)
_tv.TFindDialogRec_swigregister(TFindDialogRecPtr)

class TReplaceDialogRec(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TReplaceDialogRec, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TReplaceDialogRec, name)
    def __repr__(self):
        return "<C TReplaceDialogRec instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TReplaceDialogRec, 'this', _tv.new_TReplaceDialogRec(*args))
        _swig_setattr(self, TReplaceDialogRec, 'thisown', 1)
    __swig_setmethods__["find"] = _tv.TReplaceDialogRec_find_set
    __swig_getmethods__["find"] = _tv.TReplaceDialogRec_find_get
    if _newclass:find = property(_tv.TReplaceDialogRec_find_get, _tv.TReplaceDialogRec_find_set)
    __swig_setmethods__["replace"] = _tv.TReplaceDialogRec_replace_set
    __swig_getmethods__["replace"] = _tv.TReplaceDialogRec_replace_get
    if _newclass:replace = property(_tv.TReplaceDialogRec_replace_get, _tv.TReplaceDialogRec_replace_set)
    __swig_setmethods__["options"] = _tv.TReplaceDialogRec_options_set
    __swig_getmethods__["options"] = _tv.TReplaceDialogRec_options_get
    if _newclass:options = property(_tv.TReplaceDialogRec_options_get, _tv.TReplaceDialogRec_options_set)
    def __del__(self, destroy=_tv.delete_TReplaceDialogRec):
        try:
            if self.thisown: destroy(self)
        except: pass

class TReplaceDialogRecPtr(TReplaceDialogRec):
    def __init__(self, this):
        _swig_setattr(self, TReplaceDialogRec, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TReplaceDialogRec, 'thisown', 0)
        _swig_setattr(self, TReplaceDialogRec,self.__class__,TReplaceDialogRec)
_tv.TReplaceDialogRec_swigregister(TReplaceDialogRecPtr)

cmFileOpen = _tv.cmFileOpen
cmFileReplace = _tv.cmFileReplace
cmFileClear = _tv.cmFileClear
cmFileInit = _tv.cmFileInit
cmChangeDir = _tv.cmChangeDir
cmRevert = _tv.cmRevert
cmFileSelect = _tv.cmFileSelect
cmDirSelection = _tv.cmDirSelection
cmFileFocused = _tv.cmFileFocused
cmFileDoubleClicked = _tv.cmFileDoubleClicked
class TMethodHolder(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TMethodHolder, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TMethodHolder, name)
    def __repr__(self):
        return "<C TMethodHolder instance at %s>" % (self.this,)
    def initStatusLine(*args): return _tv.TMethodHolder_initStatusLine(*args)
    def initMenuBar(*args): return _tv.TMethodHolder_initMenuBar(*args)
    def initDeskTop(*args): return _tv.TMethodHolder_initDeskTop(*args)
    def __del__(self, destroy=_tv.delete_TMethodHolder):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __init__(self, *args):
        if self.__class__ == TMethodHolder:
            args = (None,) + args
        else:
            args = (self,) + args
        _swig_setattr(self, TMethodHolder, 'this', _tv.new_TMethodHolder(*args))
        _swig_setattr(self, TMethodHolder, 'thisown', 1)
    def __disown__(self):
        self.thisown = 0
        _tv.disown_TMethodHolder(self)
        return weakref_proxy(self)

class TMethodHolderPtr(TMethodHolder):
    def __init__(self, this):
        _swig_setattr(self, TMethodHolder, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TMethodHolder, 'thisown', 0)
        _swig_setattr(self, TMethodHolder,self.__class__,TMethodHolder)
_tv.TMethodHolder_swigregister(TMethodHolderPtr)

class TAppWrapper(TApplication):
    __swig_setmethods__ = {}
    for _s in [TApplication]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TAppWrapper, name, value)
    __swig_getmethods__ = {}
    for _s in [TApplication]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TAppWrapper, name)
    def __repr__(self):
        return "<C TAppWrapper instance at %s>" % (self.this,)
    __swig_getmethods__["_sInitStatusLine"] = lambda x: _tv.TAppWrapper__sInitStatusLine
    if _newclass:_sInitStatusLine = staticmethod(_tv.TAppWrapper__sInitStatusLine)
    __swig_getmethods__["_sInitMenuBar"] = lambda x: _tv.TAppWrapper__sInitMenuBar
    if _newclass:_sInitMenuBar = staticmethod(_tv.TAppWrapper__sInitMenuBar)
    __swig_getmethods__["_sInitDeskTop"] = lambda x: _tv.TAppWrapper__sInitDeskTop
    if _newclass:_sInitDeskTop = staticmethod(_tv.TAppWrapper__sInitDeskTop)
    def __init__(self, *args):
        if self.__class__ == TAppWrapper:
            args = (None,) + args
        else:
            args = (self,) + args
        _swig_setattr(self, TAppWrapper, 'this', _tv.new_TAppWrapper(*args))
        _swig_setattr(self, TAppWrapper, 'thisown', 1)
    def __del__(self, destroy=_tv.delete_TAppWrapper):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __disown__(self):
        self.thisown = 0
        _tv.disown_TAppWrapper(self)
        return weakref_proxy(self)

class TAppWrapperPtr(TAppWrapper):
    def __init__(self, this):
        _swig_setattr(self, TAppWrapper, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TAppWrapper, 'thisown', 0)
        _swig_setattr(self, TAppWrapper,self.__class__,TAppWrapper)
_tv.TAppWrapper_swigregister(TAppWrapperPtr)

TAppWrapper__sInitStatusLine = _tv.TAppWrapper__sInitStatusLine

TAppWrapper__sInitMenuBar = _tv.TAppWrapper__sInitMenuBar

TAppWrapper__sInitDeskTop = _tv.TAppWrapper__sInitDeskTop


