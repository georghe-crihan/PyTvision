# This file was created automatically by SWIG.
import objectc
class TObject:
    __setmethods__ = {}
    for _s in []: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TObject):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TObject.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in []: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TObject.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TObject(self)
    def shutDown(*args): return apply(objectc.TObject_shutDown,args)
    def __init__(self,*args):
        self.this = apply(objectc.new_TObject,args)
        self.thisown = 1
    def __repr__(self):
        return "<C TObject instance at %s>" % (self.this,)

class TObjectPtr(TObject):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TObject
objectc.TObject_swigregister(TObjectPtr)
class MouseEventType:
    __setmethods__ = {}
    for _s in []: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,MouseEventType):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = MouseEventType.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in []: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = MouseEventType.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    __setmethods__["buttons"] = objectc.MouseEventType_buttons_set
    __getmethods__["buttons"] = objectc.MouseEventType_buttons_get
    __setmethods__["doubleClick"] = objectc.MouseEventType_doubleClick_set
    __getmethods__["doubleClick"] = objectc.MouseEventType_doubleClick_get
    __setmethods__["where"] = objectc.MouseEventType_where_set
    __getmethods__["where"] = objectc.MouseEventType_where_get
    def __init__(self,*args):
        self.this = apply(objectc.new_MouseEventType,args)
        self.thisown = 1
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_MouseEventType(self)
    def __repr__(self):
        return "<C MouseEventType instance at %s>" % (self.this,)

class MouseEventTypePtr(MouseEventType):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = MouseEventType
objectc.MouseEventType_swigregister(MouseEventTypePtr)
class THWMouse:
    __setmethods__ = {}
    for _s in []: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,THWMouse):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = THWMouse.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in []: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = THWMouse.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<C THWMouse instance at %s>" % (self.this,)

class THWMousePtr(THWMouse):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = THWMouse
objectc.THWMouse_swigregister(THWMousePtr)
class TMouse(THWMouse):
    __setmethods__ = {}
    for _s in [THWMouse]: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TMouse):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TMouse.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in [THWMouse]: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TMouse.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __init__(self,*args):
        self.this = apply(objectc.new_TMouse,args)
        self.thisown = 1
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TMouse(self)
    def __repr__(self):
        return "<C TMouse instance at %s>" % (self.this,)

class TMousePtr(TMouse):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TMouse
objectc.TMouse_swigregister(TMousePtr)
class CharScanType:
    __setmethods__ = {}
    for _s in []: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,CharScanType):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = CharScanType.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in []: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = CharScanType.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    __setmethods__["charCode"] = objectc.CharScanType_charCode_set
    __getmethods__["charCode"] = objectc.CharScanType_charCode_get
    __setmethods__["scanCode"] = objectc.CharScanType_scanCode_set
    __getmethods__["scanCode"] = objectc.CharScanType_scanCode_get
    def __init__(self,*args):
        self.this = apply(objectc.new_CharScanType,args)
        self.thisown = 1
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_CharScanType(self)
    def __repr__(self):
        return "<C CharScanType instance at %s>" % (self.this,)

class CharScanTypePtr(CharScanType):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = CharScanType
objectc.CharScanType_swigregister(CharScanTypePtr)
class KeyDownEvent:
    __setmethods__ = {}
    for _s in []: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,KeyDownEvent):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = KeyDownEvent.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in []: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = KeyDownEvent.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    __setmethods__["charScan"] = objectc.KeyDownEvent_charScan_set
    __getmethods__["charScan"] = objectc.KeyDownEvent_charScan_get
    __setmethods__["keyCode"] = objectc.KeyDownEvent_keyCode_set
    __getmethods__["keyCode"] = objectc.KeyDownEvent_keyCode_get
    __setmethods__["shiftState"] = objectc.KeyDownEvent_shiftState_set
    __getmethods__["shiftState"] = objectc.KeyDownEvent_shiftState_get
    __setmethods__["raw_scanCode"] = objectc.KeyDownEvent_raw_scanCode_set
    __getmethods__["raw_scanCode"] = objectc.KeyDownEvent_raw_scanCode_get
    __setmethods__["charCode"] = objectc.KeyDownEvent_charCode_set
    __getmethods__["charCode"] = objectc.KeyDownEvent_charCode_get
    def __init__(self,*args):
        self.this = apply(objectc.new_KeyDownEvent,args)
        self.thisown = 1
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_KeyDownEvent(self)
    def __repr__(self):
        return "<C KeyDownEvent instance at %s>" % (self.this,)

class KeyDownEventPtr(KeyDownEvent):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = KeyDownEvent
objectc.KeyDownEvent_swigregister(KeyDownEventPtr)
class MessageEvent:
    __setmethods__ = {}
    for _s in []: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,MessageEvent):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = MessageEvent.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in []: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = MessageEvent.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    __setmethods__["command"] = objectc.MessageEvent_command_set
    __getmethods__["command"] = objectc.MessageEvent_command_get
    def __init__(self,*args):
        self.this = apply(objectc.new_MessageEvent,args)
        self.thisown = 1
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_MessageEvent(self)
    def __repr__(self):
        return "<C MessageEvent instance at %s>" % (self.this,)

class MessageEventPtr(MessageEvent):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = MessageEvent
objectc.MessageEvent_swigregister(MessageEventPtr)
class TEvent:
    __setmethods__ = {}
    for _s in []: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TEvent):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TEvent.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in []: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TEvent.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    __setmethods__["what"] = objectc.TEvent_what_set
    __getmethods__["what"] = objectc.TEvent_what_get
    def __init__(self,*args):
        self.this = apply(objectc.new_TEvent,args)
        self.thisown = 1
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TEvent(self)
    def __repr__(self):
        return "<C TEvent instance at %s>" % (self.this,)

class TEventPtr(TEvent):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TEvent
objectc.TEvent_swigregister(TEventPtr)
class TStreamable:
    __setmethods__ = {}
    for _s in []: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TStreamable):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TStreamable.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in []: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TStreamable.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TStreamable(self)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<C TStreamable instance at %s>" % (self.this,)

class TStreamablePtr(TStreamable):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TStreamable
objectc.TStreamable_swigregister(TStreamablePtr)
class TNSCollection(TObject):
    __setmethods__ = {}
    for _s in [TObject]: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TNSCollection):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TNSCollection.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in [TObject]: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TNSCollection.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __init__(self,*args):
        self.this = apply(objectc.new_TNSCollection,args)
        self.thisown = 1
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TNSCollection(self)
    def shutDown(*args): return apply(objectc.TNSCollection_shutDown,args)
    def at(*args): return apply(objectc.TNSCollection_at,args)
    def indexOf(*args): return apply(objectc.TNSCollection_indexOf,args)
    def atFree(*args): return apply(objectc.TNSCollection_atFree,args)
    def atRemove(*args): return apply(objectc.TNSCollection_atRemove,args)
    def remove(*args): return apply(objectc.TNSCollection_remove,args)
    def removeAll(*args): return apply(objectc.TNSCollection_removeAll,args)
    def free(*args): return apply(objectc.TNSCollection_free,args)
    def freeAll(*args): return apply(objectc.TNSCollection_freeAll,args)
    def atInsert(*args): return apply(objectc.TNSCollection_atInsert,args)
    def atPut(*args): return apply(objectc.TNSCollection_atPut,args)
    def atReplace(*args): return apply(objectc.TNSCollection_atReplace,args)
    def insert(*args): return apply(objectc.TNSCollection_insert,args)
    def error(*args): return apply(objectc.TNSCollection_error,args)
    def firstThat(*args): return apply(objectc.TNSCollection_firstThat,args)
    def lastThat(*args): return apply(objectc.TNSCollection_lastThat,args)
    def forEach(*args): return apply(objectc.TNSCollection_forEach,args)
    def pack(*args): return apply(objectc.TNSCollection_pack,args)
    def setLimit(*args): return apply(objectc.TNSCollection_setLimit,args)
    def getCount(*args): return apply(objectc.TNSCollection_getCount,args)
    def setOwnerShip(*args): return apply(objectc.TNSCollection_setOwnerShip,args)
    def __repr__(self):
        return "<C TNSCollection instance at %s>" % (self.this,)

class TNSCollectionPtr(TNSCollection):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TNSCollection
objectc.TNSCollection_swigregister(TNSCollectionPtr)
class TNSSortedCollection(TNSCollection):
    __setmethods__ = {}
    for _s in [TNSCollection]: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TNSSortedCollection):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TNSSortedCollection.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in [TNSCollection]: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TNSSortedCollection.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def search(*args): return apply(objectc.TNSSortedCollection_search,args)
    def indexOf(*args): return apply(objectc.TNSSortedCollection_indexOf,args)
    def insert(*args): return apply(objectc.TNSSortedCollection_insert,args)
    __setmethods__["duplicates"] = objectc.TNSSortedCollection_duplicates_set
    __getmethods__["duplicates"] = objectc.TNSSortedCollection_duplicates_get
    def keyOf(*args): return apply(objectc.TNSSortedCollection_keyOf,args)
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TNSSortedCollection(self)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<C TNSSortedCollection instance at %s>" % (self.this,)

class TNSSortedCollectionPtr(TNSSortedCollection):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TNSSortedCollection
objectc.TNSSortedCollection_swigregister(TNSSortedCollectionPtr)
class TCollection(TNSCollection,TStreamable):
    __setmethods__ = {}
    for _s in [TNSCollection,TStreamable]: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TCollection):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TCollection.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in [TNSCollection,TStreamable]: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TCollection.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TCollection(self)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<C TCollection instance at %s>" % (self.this,)

class TCollectionPtr(TCollection):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TCollection
objectc.TCollection_swigregister(TCollectionPtr)
class TSortedCollection(TNSSortedCollection,TCollection):
    __setmethods__ = {}
    for _s in [TNSSortedCollection,TCollection]: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TSortedCollection):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TSortedCollection.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in [TNSSortedCollection,TCollection]: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TSortedCollection.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TSortedCollection(self)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<C TSortedCollection instance at %s>" % (self.this,)

class TSortedCollectionPtr(TSortedCollection):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TSortedCollection
objectc.TSortedCollection_swigregister(TSortedCollectionPtr)
class TStringCollection(TSortedCollection):
    __setmethods__ = {}
    for _s in [TSortedCollection]: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TStringCollection):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TStringCollection.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in [TSortedCollection]: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TStringCollection.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __init__(self,*args):
        self.this = apply(objectc.new_TStringCollection,args)
        self.thisown = 1
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TStringCollection(self)
    def __repr__(self):
        return "<C TStringCollection instance at %s>" % (self.this,)

class TStringCollectionPtr(TStringCollection):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TStringCollection
objectc.TStringCollection_swigregister(TStringCollectionPtr)
class TPoint:
    __setmethods__ = {}
    for _s in []: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TPoint):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TPoint.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in []: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TPoint.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __iadd__(*args): return apply(objectc.TPoint___iadd__,args)
    def __isub__(*args): return apply(objectc.TPoint___isub__,args)
    __setmethods__["x"] = objectc.TPoint_x_set
    __getmethods__["x"] = objectc.TPoint_x_get
    __setmethods__["y"] = objectc.TPoint_y_set
    __getmethods__["y"] = objectc.TPoint_y_get
    def __init__(self,*args):
        self.this = apply(objectc.new_TPoint,args)
        self.thisown = 1
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TPoint(self)
    def __repr__(self):
        return "<C TPoint instance at %s>" % (self.this,)

class TPointPtr(TPoint):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TPoint
objectc.TPoint_swigregister(TPointPtr)
class TRect:
    __setmethods__ = {}
    for _s in []: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TRect):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TRect.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in []: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TRect.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __init__(self,*args):
        self.this = apply(objectc.new_TRect,args)
        self.thisown = 1
    def move(*args): return apply(objectc.TRect_move,args)
    def grow(*args): return apply(objectc.TRect_grow,args)
    def intersect(*args): return apply(objectc.TRect_intersect,args)
    def Union(*args): return apply(objectc.TRect_Union,args)
    def contains(*args): return apply(objectc.TRect_contains,args)
    def __eq__(*args): return apply(objectc.TRect___eq__,args)
    def __ne__(*args): return apply(objectc.TRect___ne__,args)
    def isEmpty(*args): return apply(objectc.TRect_isEmpty,args)
    __setmethods__["a"] = objectc.TRect_a_set
    __getmethods__["a"] = objectc.TRect_a_get
    __setmethods__["b"] = objectc.TRect_b_set
    __getmethods__["b"] = objectc.TRect_b_get
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TRect(self)
    def __repr__(self):
        return "<C TRect instance at %s>" % (self.this,)

class TRectPtr(TRect):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TRect
objectc.TRect_swigregister(TRectPtr)
class TCommandSet:
    __setmethods__ = {}
    for _s in []: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TCommandSet):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TCommandSet.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in []: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TCommandSet.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __init__(self,*args):
        self.this = apply(objectc.new_TCommandSet,args)
        self.thisown = 1
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TCommandSet(self)
    def has(*args): return apply(objectc.TCommandSet_has,args)
    def disableCmdInt(*args): return apply(objectc.TCommandSet_disableCmdInt,args)
    def disableCmdRange(*args): return apply(objectc.TCommandSet_disableCmdRange,args)
    def enableCmdInt(*args): return apply(objectc.TCommandSet_enableCmdInt,args)
    def enableCmdRange(*args): return apply(objectc.TCommandSet_enableCmdRange,args)
    def enableAllCommands(*args): return apply(objectc.TCommandSet_enableAllCommands,args)
    def disableCmd(*args): return apply(objectc.TCommandSet_disableCmd,args)
    def enableCmd(*args): return apply(objectc.TCommandSet_enableCmd,args)
    def __iadd__(*args): return apply(objectc.TCommandSet___iadd__,args)
    def __isub__(*args): return apply(objectc.TCommandSet___isub__,args)
    def isEmpty(*args): return apply(objectc.TCommandSet_isEmpty,args)
    def set(*args): return apply(objectc.TCommandSet_set,args)
    def __iand__(*args): return apply(objectc.TCommandSet___iand__,args)
    def __ior__(*args): return apply(objectc.TCommandSet___ior__,args)
    def __repr__(self):
        return "<C TCommandSet instance at %s>" % (self.this,)

class TCommandSetPtr(TCommandSet):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TCommandSet
objectc.TCommandSet_swigregister(TCommandSetPtr)
class write_args:
    __setmethods__ = {}
    for _s in []: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,write_args):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = write_args.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in []: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = write_args.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    __setmethods__["self"] = objectc.write_args_self_set
    __getmethods__["self"] = objectc.write_args_self_get
    __setmethods__["target"] = objectc.write_args_target_set
    __getmethods__["target"] = objectc.write_args_target_get
    __setmethods__["buf"] = objectc.write_args_buf_set
    __getmethods__["buf"] = objectc.write_args_buf_get
    __setmethods__["offset"] = objectc.write_args_offset_set
    __getmethods__["offset"] = objectc.write_args_offset_get
    def __init__(self,*args):
        self.this = apply(objectc.new_write_args,args)
        self.thisown = 1
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_write_args(self)
    def __repr__(self):
        return "<C write_args instance at %s>" % (self.this,)

class write_argsPtr(write_args):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = write_args
objectc.write_args_swigregister(write_argsPtr)
class TView(TObject,TStreamable):
    __setmethods__ = {}
    for _s in [TObject,TStreamable]: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TView):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TView.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in [TObject,TStreamable]: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TView.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    phFocused = objectc.TView_phFocused
    phPreProcess = objectc.TView_phPreProcess
    phPostProcess = objectc.TView_phPostProcess
    normalSelect = objectc.TView_normalSelect
    enterSelect = objectc.TView_enterSelect
    leaveSelect = objectc.TView_leaveSelect
    def __init__(self,*args):
        self.this = apply(objectc.new_TView,args)
        self.thisown = 1
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TView(self)
    def sizeLimits(*args): return apply(objectc.TView_sizeLimits,args)
    def getBounds(*args): return apply(objectc.TView_getBounds,args)
    def getExtent(*args): return apply(objectc.TView_getExtent,args)
    def getClipRect(*args): return apply(objectc.TView_getClipRect,args)
    def mouseInView(*args): return apply(objectc.TView_mouseInView,args)
    def containsMouse(*args): return apply(objectc.TView_containsMouse,args)
    def locate(*args): return apply(objectc.TView_locate,args)
    def dragView(*args): return apply(objectc.TView_dragView,args)
    def calcBounds(*args): return apply(objectc.TView_calcBounds,args)
    def changeBounds(*args): return apply(objectc.TView_changeBounds,args)
    def growTo(*args): return apply(objectc.TView_growTo,args)
    def moveTo(*args): return apply(objectc.TView_moveTo,args)
    def setBounds(*args): return apply(objectc.TView_setBounds,args)
    def getHelpCtx(*args): return apply(objectc.TView_getHelpCtx,args)
    def valid(*args): return apply(objectc.TView_valid,args)
    def hide(*args): return apply(objectc.TView_hide,args)
    def show(*args): return apply(objectc.TView_show,args)
    def draw(*args): return apply(objectc.TView_draw,args)
    def drawView(*args): return apply(objectc.TView_drawView,args)
    def exposed(*args): return apply(objectc.TView_exposed,args)
    def hideCursor(*args): return apply(objectc.TView_hideCursor,args)
    def drawHide(*args): return apply(objectc.TView_drawHide,args)
    def drawShow(*args): return apply(objectc.TView_drawShow,args)
    def drawUnderRect(*args): return apply(objectc.TView_drawUnderRect,args)
    def drawUnderView(*args): return apply(objectc.TView_drawUnderView,args)
    def dataSize(*args): return apply(objectc.TView_dataSize,args)
    def getData(*args): return apply(objectc.TView_getData,args)
    def setData(*args): return apply(objectc.TView_setData,args)
    def blockCursor(*args): return apply(objectc.TView_blockCursor,args)
    def normalCursor(*args): return apply(objectc.TView_normalCursor,args)
    def resetCursor(*args): return apply(objectc.TView_resetCursor,args)
    def setCursor(*args): return apply(objectc.TView_setCursor,args)
    def showCursor(*args): return apply(objectc.TView_showCursor,args)
    def drawCursor(*args): return apply(objectc.TView_drawCursor,args)
    def clearEvent(*args): return apply(objectc.TView_clearEvent,args)
    def eventAvail(*args): return apply(objectc.TView_eventAvail,args)
    def getEvent(*args): return apply(objectc.TView_getEvent,args)
    def handleEvent(*args): return apply(objectc.TView_handleEvent,args)
    def putEvent(*args): return apply(objectc.TView_putEvent,args)
    def endModal(*args): return apply(objectc.TView_endModal,args)
    def execute(*args): return apply(objectc.TView_execute,args)
    def getColor(*args): return apply(objectc.TView_getColor,args)
    def getPalette(*args): return apply(objectc.TView_getPalette,args)
    def mapColor(*args): return apply(objectc.TView_mapColor,args)
    def getState(*args): return apply(objectc.TView_getState,args)
    def select(*args): return apply(objectc.TView_select,args)
    def setState(*args): return apply(objectc.TView_setState,args)
    def keyEvent(*args): return apply(objectc.TView_keyEvent,args)
    def mouseEvent(*args): return apply(objectc.TView_mouseEvent,args)
    def makeGlobal(*args): return apply(objectc.TView_makeGlobal,args)
    def makeLocal(*args): return apply(objectc.TView_makeLocal,args)
    def nextView(*args): return apply(objectc.TView_nextView,args)
    def prevView(*args): return apply(objectc.TView_prevView,args)
    def prev(*args): return apply(objectc.TView_prev,args)
    __setmethods__["next"] = objectc.TView_next_set
    __getmethods__["next"] = objectc.TView_next_get
    def makeFirst(*args): return apply(objectc.TView_makeFirst,args)
    def putInFrontOf(*args): return apply(objectc.TView_putInFrontOf,args)
    def TopView(*args): return apply(objectc.TView_TopView,args)
    def writeBuf(*args): return apply(objectc.TView_writeBuf,args)
    def writeNativeBuf(*args): return apply(objectc.TView_writeNativeBuf,args)
    def writeLine(*args): return apply(objectc.TView_writeLine,args)
    def writeNativeLine(*args): return apply(objectc.TView_writeNativeLine,args)
    def writeChar(*args): return apply(objectc.TView_writeChar,args)
    def writeCharU16(*args): return apply(objectc.TView_writeCharU16,args)
    def writeStr(*args): return apply(objectc.TView_writeStr,args)
    def writeStrU16(*args): return apply(objectc.TView_writeStrU16,args)
    __setmethods__["size"] = objectc.TView_size_set
    __getmethods__["size"] = objectc.TView_size_get
    __setmethods__["options"] = objectc.TView_options_set
    __getmethods__["options"] = objectc.TView_options_get
    __setmethods__["eventMask"] = objectc.TView_eventMask_set
    __getmethods__["eventMask"] = objectc.TView_eventMask_get
    __setmethods__["state"] = objectc.TView_state_set
    __getmethods__["state"] = objectc.TView_state_get
    __setmethods__["origin"] = objectc.TView_origin_set
    __getmethods__["origin"] = objectc.TView_origin_get
    __setmethods__["cursor"] = objectc.TView_cursor_set
    __getmethods__["cursor"] = objectc.TView_cursor_get
    __setmethods__["growMode"] = objectc.TView_growMode_set
    __getmethods__["growMode"] = objectc.TView_growMode_get
    __setmethods__["dragMode"] = objectc.TView_dragMode_set
    __getmethods__["dragMode"] = objectc.TView_dragMode_get
    __setmethods__["helpCtx"] = objectc.TView_helpCtx_set
    __getmethods__["helpCtx"] = objectc.TView_helpCtx_get
    __setmethods__["owner"] = objectc.TView_owner_set
    __getmethods__["owner"] = objectc.TView_owner_get
    def shutDown(*args): return apply(objectc.TView_shutDown,args)
    def __repr__(self):
        return "<C TView instance at %s>" % (self.this,)

class TViewPtr(TView):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TView
objectc.TView_swigregister(TViewPtr)
class TGroup(TView):
    __setmethods__ = {}
    for _s in [TView]: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TGroup):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TGroup.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in [TView]: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TGroup.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __init__(self,*args):
        self.this = apply(objectc.new_TGroup,args)
        self.thisown = 1
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TGroup(self)
    def shutDown(*args): return apply(objectc.TGroup_shutDown,args)
    def execView(*args): return apply(objectc.TGroup_execView,args)
    def execute(*args): return apply(objectc.TGroup_execute,args)
    def insertView(*args): return apply(objectc.TGroup_insertView,args)
    def remove(*args): return apply(objectc.TGroup_remove,args)
    def removeView(*args): return apply(objectc.TGroup_removeView,args)
    def resetCurrent(*args): return apply(objectc.TGroup_resetCurrent,args)
    def setCurrent(*args): return apply(objectc.TGroup_setCurrent,args)
    def selectNext(*args): return apply(objectc.TGroup_selectNext,args)
    def firstThat(*args): return apply(objectc.TGroup_firstThat,args)
    def forEach(*args): return apply(objectc.TGroup_forEach,args)
    def insert(*args): return apply(objectc.TGroup_insert,args)
    def at(*args): return apply(objectc.TGroup_at,args)
    def firstMatch(*args): return apply(objectc.TGroup_firstMatch,args)
    def indexOf(*args): return apply(objectc.TGroup_indexOf,args)
    def first(*args): return apply(objectc.TGroup_first,args)
    def setState(*args): return apply(objectc.TGroup_setState,args)
    def handleEvent(*args): return apply(objectc.TGroup_handleEvent,args)
    def drawSubViews(*args): return apply(objectc.TGroup_drawSubViews,args)
    def changeBounds(*args): return apply(objectc.TGroup_changeBounds,args)
    def dataSize(*args): return apply(objectc.TGroup_dataSize,args)
    def getData(*args): return apply(objectc.TGroup_getData,args)
    def setData(*args): return apply(objectc.TGroup_setData,args)
    def draw(*args): return apply(objectc.TGroup_draw,args)
    def redraw(*args): return apply(objectc.TGroup_redraw,args)
    def Redraw(*args): return apply(objectc.TGroup_Redraw,args)
    def lock(*args): return apply(objectc.TGroup_lock,args)
    def unlock(*args): return apply(objectc.TGroup_unlock,args)
    def resetCursor(*args): return apply(objectc.TGroup_resetCursor,args)
    def canShowCursor(*args): return apply(objectc.TGroup_canShowCursor,args)
    def endModal(*args): return apply(objectc.TGroup_endModal,args)
    def eventError(*args): return apply(objectc.TGroup_eventError,args)
    def getHelpCtx(*args): return apply(objectc.TGroup_getHelpCtx,args)
    def valid(*args): return apply(objectc.TGroup_valid,args)
    def freeBuffer(*args): return apply(objectc.TGroup_freeBuffer,args)
    def getBuffer(*args): return apply(objectc.TGroup_getBuffer,args)
    __setmethods__["last"] = objectc.TGroup_last_set
    __getmethods__["last"] = objectc.TGroup_last_get
    __setmethods__["clip"] = objectc.TGroup_clip_set
    __getmethods__["clip"] = objectc.TGroup_clip_get
    __setmethods__["phase"] = objectc.TGroup_phase_set
    __getmethods__["phase"] = objectc.TGroup_phase_get
    __setmethods__["buffer"] = objectc.TGroup_buffer_set
    __getmethods__["buffer"] = objectc.TGroup_buffer_get
    __setmethods__["lockFlag"] = objectc.TGroup_lockFlag_set
    __getmethods__["lockFlag"] = objectc.TGroup_lockFlag_get
    __setmethods__["endState"] = objectc.TGroup_endState_set
    __getmethods__["endState"] = objectc.TGroup_endState_get
    def __repr__(self):
        return "<C TGroup instance at %s>" % (self.this,)

class TGroupPtr(TGroup):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TGroup
objectc.TGroup_swigregister(TGroupPtr)
class TWindowInit:
    __setmethods__ = {}
    for _s in []: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TWindowInit):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TWindowInit.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in []: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TWindowInit.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __init__(self,*args):
        self.this = apply(objectc.new_TWindowInit,args)
        self.thisown = 1
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TWindowInit(self)
    def __repr__(self):
        return "<C TWindowInit instance at %s>" % (self.this,)

class TWindowInitPtr(TWindowInit):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TWindowInit
objectc.TWindowInit_swigregister(TWindowInitPtr)
class TWindow(TGroup,TWindowInit):
    __setmethods__ = {}
    for _s in [TGroup,TWindowInit]: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TWindow):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TWindow.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in [TGroup,TWindowInit]: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TWindow.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __init__(self,*args):
        self.this = apply(objectc.new_TWindow,args)
        self.thisown = 1
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TWindow(self)
    def close(*args): return apply(objectc.TWindow_close,args)
    def getPalette(*args): return apply(objectc.TWindow_getPalette,args)
    def getTitle(*args): return apply(objectc.TWindow_getTitle,args)
    def handleEvent(*args): return apply(objectc.TWindow_handleEvent,args)
    def setState(*args): return apply(objectc.TWindow_setState,args)
    def sizeLimits(*args): return apply(objectc.TWindow_sizeLimits,args)
    def standardScrollBar(*args): return apply(objectc.TWindow_standardScrollBar,args)
    def zoom(*args): return apply(objectc.TWindow_zoom,args)
    def shutDown(*args): return apply(objectc.TWindow_shutDown,args)
    __setmethods__["flags"] = objectc.TWindow_flags_set
    __getmethods__["flags"] = objectc.TWindow_flags_get
    __setmethods__["zoomRect"] = objectc.TWindow_zoomRect_set
    __getmethods__["zoomRect"] = objectc.TWindow_zoomRect_get
    __setmethods__["number"] = objectc.TWindow_number_set
    __getmethods__["number"] = objectc.TWindow_number_get
    __setmethods__["palette"] = objectc.TWindow_palette_set
    __getmethods__["palette"] = objectc.TWindow_palette_get
    __setmethods__["frame"] = objectc.TWindow_frame_set
    __getmethods__["frame"] = objectc.TWindow_frame_get
    __setmethods__["title"] = objectc.TWindow_title_set
    __getmethods__["title"] = objectc.TWindow_title_get
    __setmethods__["intlTitle"] = objectc.TWindow_intlTitle_set
    __getmethods__["intlTitle"] = objectc.TWindow_intlTitle_get
    def __repr__(self):
        return "<C TWindow instance at %s>" % (self.this,)

class TWindowPtr(TWindow):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TWindow
objectc.TWindow_swigregister(TWindowPtr)
class TButton(TView):
    __setmethods__ = {}
    for _s in [TView]: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TButton):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TButton.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in [TView]: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TButton.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __init__(self,*args):
        self.this = apply(objectc.new_TButton,args)
        self.thisown = 1
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TButton(self)
    def draw(*args): return apply(objectc.TButton_draw,args)
    def drawState(*args): return apply(objectc.TButton_drawState,args)
    def getPalette(*args): return apply(objectc.TButton_getPalette,args)
    def handleEvent(*args): return apply(objectc.TButton_handleEvent,args)
    def makeDefault(*args): return apply(objectc.TButton_makeDefault,args)
    def press(*args): return apply(objectc.TButton_press,args)
    def setState(*args): return apply(objectc.TButton_setState,args)
    def setCallBack(*args): return apply(objectc.TButton_setCallBack,args)
    def getText(*args): return apply(objectc.TButton_getText,args)
    __setmethods__["title"] = objectc.TButton_title_set
    __getmethods__["title"] = objectc.TButton_title_get
    __setmethods__["intlTitle"] = objectc.TButton_intlTitle_set
    __getmethods__["intlTitle"] = objectc.TButton_intlTitle_get
    def __repr__(self):
        return "<C TButton instance at %s>" % (self.this,)

class TButtonPtr(TButton):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TButton
objectc.TButton_swigregister(TButtonPtr)
class TButtonRef(TButton):
    __setmethods__ = {}
    for _s in [TButton]: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TButtonRef):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TButtonRef.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in [TButton]: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TButtonRef.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __init__(self,*args):
        self.this = apply(objectc.new_TButtonRef,args)
        self.thisown = 1
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TButtonRef(self)
    def __repr__(self):
        return "<C TButtonRef instance at %s>" % (self.this,)

class TButtonRefPtr(TButtonRef):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TButtonRef
objectc.TButtonRef_swigregister(TButtonRefPtr)
class TInputLineBase(TView):
    __setmethods__ = {}
    for _s in [TView]: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TInputLineBase):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TInputLineBase.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in [TView]: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TInputLineBase.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TInputLineBase(self)
    def dataSize(*args): return apply(objectc.TInputLineBase_dataSize,args)
    def getPalette(*args): return apply(objectc.TInputLineBase_getPalette,args)
    def handleEvent(*args): return apply(objectc.TInputLineBase_handleEvent,args)
    def selectAll(*args): return apply(objectc.TInputLineBase_selectAll,args)
    def setState(*args): return apply(objectc.TInputLineBase_setState,args)
    def SetValidator(*args): return apply(objectc.TInputLineBase_SetValidator,args)
    def valid(*args): return apply(objectc.TInputLineBase_valid,args)
    def insertChar(*args): return apply(objectc.TInputLineBase_insertChar,args)
    def assignPos(*args): return apply(objectc.TInputLineBase_assignPos,args)
    def pasteFromOSClipboard(*args): return apply(objectc.TInputLineBase_pasteFromOSClipboard,args)
    def copyToOSClipboard(*args): return apply(objectc.TInputLineBase_copyToOSClipboard,args)
    def setDataFromStr(*args): return apply(objectc.TInputLineBase_setDataFromStr,args)
    def getData(*args): return apply(objectc.TInputLineBase_getData,args)
    __setmethods__["curPos"] = objectc.TInputLineBase_curPos_set
    __getmethods__["curPos"] = objectc.TInputLineBase_curPos_get
    __setmethods__["firstPos"] = objectc.TInputLineBase_firstPos_set
    __getmethods__["firstPos"] = objectc.TInputLineBase_firstPos_get
    __setmethods__["selStart"] = objectc.TInputLineBase_selStart_set
    __getmethods__["selStart"] = objectc.TInputLineBase_selStart_get
    __setmethods__["selEnd"] = objectc.TInputLineBase_selEnd_set
    __getmethods__["selEnd"] = objectc.TInputLineBase_selEnd_get
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<C TInputLineBase instance at %s>" % (self.this,)

class TInputLineBasePtr(TInputLineBase):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TInputLineBase
objectc.TInputLineBase_swigregister(TInputLineBasePtr)
class TInputLineBaseChar(TInputLineBase):
    __setmethods__ = {}
    for _s in [TInputLineBase]: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TInputLineBaseChar):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TInputLineBaseChar.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in [TInputLineBase]: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TInputLineBaseChar.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __init__(self,*args):
        self.this = apply(objectc.new_TInputLineBaseChar,args)
        self.thisown = 1
    def setData(*args): return apply(objectc.TInputLineBaseChar_setData,args)
    def setDataFromStr(*args): return apply(objectc.TInputLineBaseChar_setDataFromStr,args)
    def assignPos(*args): return apply(objectc.TInputLineBaseChar_assignPos,args)
    def pasteFromOSClipboard(*args): return apply(objectc.TInputLineBaseChar_pasteFromOSClipboard,args)
    def copyToOSClipboard(*args): return apply(objectc.TInputLineBaseChar_copyToOSClipboard,args)
    def draw(*args): return apply(objectc.TInputLineBaseChar_draw,args)
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TInputLineBaseChar(self)
    def __repr__(self):
        return "<C TInputLineBaseChar instance at %s>" % (self.this,)

class TInputLineBaseCharPtr(TInputLineBaseChar):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TInputLineBaseChar
objectc.TInputLineBaseChar_swigregister(TInputLineBaseCharPtr)
class TInputLine(TInputLineBaseChar):
    __setmethods__ = {}
    for _s in [TInputLineBaseChar]: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TInputLine):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TInputLine.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in [TInputLineBaseChar]: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TInputLine.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __init__(self,*args):
        self.this = apply(objectc.new_TInputLine,args)
        self.thisown = 1
    def insertChar(*args): return apply(objectc.TInputLine_insertChar,args)
    def streamableName(*args): return apply(objectc.TInputLine_streamableName,args)
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TInputLine(self)
    def __repr__(self):
        return "<C TInputLine instance at %s>" % (self.this,)

class TInputLinePtr(TInputLine):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TInputLine
objectc.TInputLine_swigregister(TInputLinePtr)
class TInputLineBaseU16(TInputLineBase):
    __setmethods__ = {}
    for _s in [TInputLineBase]: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TInputLineBaseU16):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TInputLineBaseU16.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in [TInputLineBase]: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TInputLineBaseU16.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __init__(self,*args):
        self.this = apply(objectc.new_TInputLineBaseU16,args)
        self.thisown = 1
    def setData(*args): return apply(objectc.TInputLineBaseU16_setData,args)
    def setDataFromStr(*args): return apply(objectc.TInputLineBaseU16_setDataFromStr,args)
    def assignPos(*args): return apply(objectc.TInputLineBaseU16_assignPos,args)
    def pasteFromOSClipboard(*args): return apply(objectc.TInputLineBaseU16_pasteFromOSClipboard,args)
    def copyToOSClipboard(*args): return apply(objectc.TInputLineBaseU16_copyToOSClipboard,args)
    def draw(*args): return apply(objectc.TInputLineBaseU16_draw,args)
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TInputLineBaseU16(self)
    def __repr__(self):
        return "<C TInputLineBaseU16 instance at %s>" % (self.this,)

class TInputLineBaseU16Ptr(TInputLineBaseU16):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TInputLineBaseU16
objectc.TInputLineBaseU16_swigregister(TInputLineBaseU16Ptr)
class TInputLineU16(TInputLineBaseU16):
    __setmethods__ = {}
    for _s in [TInputLineBaseU16]: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TInputLineU16):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TInputLineU16.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in [TInputLineBaseU16]: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TInputLineU16.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __init__(self,*args):
        self.this = apply(objectc.new_TInputLineU16,args)
        self.thisown = 1
    def insertChar(*args): return apply(objectc.TInputLineU16_insertChar,args)
    def streamableName(*args): return apply(objectc.TInputLineU16_streamableName,args)
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TInputLineU16(self)
    def __repr__(self):
        return "<C TInputLineU16 instance at %s>" % (self.this,)

class TInputLineU16Ptr(TInputLineU16):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TInputLineU16
objectc.TInputLineU16_swigregister(TInputLineU16Ptr)
class TStatusItem:
    __setmethods__ = {}
    for _s in []: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TStatusItem):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TStatusItem.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in []: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TStatusItem.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __init__(self,*args):
        self.this = apply(objectc.new_TStatusItem,args)
        self.thisown = 1
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TStatusItem(self)
    __setmethods__["next"] = objectc.TStatusItem_next_set
    __getmethods__["next"] = objectc.TStatusItem_next_get
    __setmethods__["text"] = objectc.TStatusItem_text_set
    __getmethods__["text"] = objectc.TStatusItem_text_get
    __setmethods__["intlText"] = objectc.TStatusItem_intlText_set
    __getmethods__["intlText"] = objectc.TStatusItem_intlText_get
    __setmethods__["keyCode"] = objectc.TStatusItem_keyCode_set
    __getmethods__["keyCode"] = objectc.TStatusItem_keyCode_get
    __setmethods__["command"] = objectc.TStatusItem_command_set
    __getmethods__["command"] = objectc.TStatusItem_command_get
    def __repr__(self):
        return "<C TStatusItem instance at %s>" % (self.this,)

class TStatusItemPtr(TStatusItem):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TStatusItem
objectc.TStatusItem_swigregister(TStatusItemPtr)
class TStatusDef:
    __setmethods__ = {}
    for _s in []: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TStatusDef):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TStatusDef.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in []: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TStatusDef.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __init__(self,*args):
        self.this = apply(objectc.new_TStatusDef,args)
        self.thisown = 1
    __setmethods__["next"] = objectc.TStatusDef_next_set
    __getmethods__["next"] = objectc.TStatusDef_next_get
    __setmethods__["min"] = objectc.TStatusDef_min_set
    __getmethods__["min"] = objectc.TStatusDef_min_get
    __setmethods__["max"] = objectc.TStatusDef_max_set
    __getmethods__["max"] = objectc.TStatusDef_max_get
    __setmethods__["items"] = objectc.TStatusDef_items_set
    __getmethods__["items"] = objectc.TStatusDef_items_get
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TStatusDef(self)
    def __repr__(self):
        return "<C TStatusDef instance at %s>" % (self.this,)

class TStatusDefPtr(TStatusDef):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TStatusDef
objectc.TStatusDef_swigregister(TStatusDefPtr)
class TStatusLine(TView):
    __setmethods__ = {}
    for _s in [TView]: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TStatusLine):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TStatusLine.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in [TView]: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TStatusLine.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __init__(self,*args):
        self.this = apply(objectc.new_TStatusLine,args)
        self.thisown = 1
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TStatusLine(self)
    def draw(*args): return apply(objectc.TStatusLine_draw,args)
    def getPalette(*args): return apply(objectc.TStatusLine_getPalette,args)
    def handleEvent(*args): return apply(objectc.TStatusLine_handleEvent,args)
    def hint(*args): return apply(objectc.TStatusLine_hint,args)
    def update(*args): return apply(objectc.TStatusLine_update,args)
    def computeLength(*args): return apply(objectc.TStatusLine_computeLength,args)
    def changeBounds(*args): return apply(objectc.TStatusLine_changeBounds,args)
    __setmethods__["compactStatus"] = objectc.TStatusLine_compactStatus_set
    __getmethods__["compactStatus"] = objectc.TStatusLine_compactStatus_get
    def __repr__(self):
        return "<C TStatusLine instance at %s>" % (self.this,)

class TStatusLinePtr(TStatusLine):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TStatusLine
objectc.TStatusLine_swigregister(TStatusLinePtr)
class TDeskInit:
    __setmethods__ = {}
    for _s in []: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TDeskInit):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TDeskInit.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in []: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TDeskInit.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __init__(self,*args):
        self.this = apply(objectc.new_TDeskInit,args)
        self.thisown = 1
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TDeskInit(self)
    def __repr__(self):
        return "<C TDeskInit instance at %s>" % (self.this,)

class TDeskInitPtr(TDeskInit):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TDeskInit
objectc.TDeskInit_swigregister(TDeskInitPtr)
class TDeskTop(TGroup,TDeskInit):
    __setmethods__ = {}
    for _s in [TGroup,TDeskInit]: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TDeskTop):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TDeskTop.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in [TGroup,TDeskInit]: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TDeskTop.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __init__(self,*args):
        self.this = apply(objectc.new_TDeskTop,args)
        self.thisown = 1
    def cascade(*args): return apply(objectc.TDeskTop_cascade,args)
    def handleEvent(*args): return apply(objectc.TDeskTop_handleEvent,args)
    def tile(*args): return apply(objectc.TDeskTop_tile,args)
    def tileError(*args): return apply(objectc.TDeskTop_tileError,args)
    def shutDown(*args): return apply(objectc.TDeskTop_shutDown,args)
    def getBackground(*args): return apply(objectc.TDeskTop_getBackground,args)
    def getOptions(*args): return apply(objectc.TDeskTop_getOptions,args)
    def setOptions(*args): return apply(objectc.TDeskTop_setOptions,args)
    def canShowCursor(*args): return apply(objectc.TDeskTop_canShowCursor,args)
    def execView(*args): return apply(objectc.TDeskTop_execView,args)
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TDeskTop(self)
    def __repr__(self):
        return "<C TDeskTop instance at %s>" % (self.this,)

class TDeskTopPtr(TDeskTop):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TDeskTop
objectc.TDeskTop_swigregister(TDeskTopPtr)
class TProgInit:
    __setmethods__ = {}
    for _s in []: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TProgInit):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TProgInit.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in []: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TProgInit.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __init__(self,*args):
        self.this = apply(objectc.new_TProgInit,args)
        self.thisown = 1
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TProgInit(self)
    def __repr__(self):
        return "<C TProgInit instance at %s>" % (self.this,)

class TProgInitPtr(TProgInit):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TProgInit
objectc.TProgInit_swigregister(TProgInitPtr)
class TProgram(TGroup,TProgInit):
    __setmethods__ = {}
    for _s in [TGroup,TProgInit]: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TProgram):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TProgram.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in [TGroup,TProgInit]: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TProgram.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __init__(self,*args):
        self.this = apply(objectc.new_TProgram,args)
        self.thisown = 1
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TProgram(self)
    def getEvent(*args): return apply(objectc.TProgram_getEvent,args)
    def getPalette(*args): return apply(objectc.TProgram_getPalette,args)
    def handleEvent(*args): return apply(objectc.TProgram_handleEvent,args)
    def idle(*args): return apply(objectc.TProgram_idle,args)
    def initScreen(*args): return apply(objectc.TProgram_initScreen,args)
    def outOfMemory(*args): return apply(objectc.TProgram_outOfMemory,args)
    def putEvent(*args): return apply(objectc.TProgram_putEvent,args)
    def run(*args): return apply(objectc.TProgram_run,args)
    def setScreenMode(*args): return apply(objectc.TProgram_setScreenMode,args)
    def setScreenModeExt(*args): return apply(objectc.TProgram_setScreenModeExt,args)
    def validView(*args): return apply(objectc.TProgram_validView,args)
    def shutDown(*args): return apply(objectc.TProgram_shutDown,args)
    def suspend(*args): return apply(objectc.TProgram_suspend,args)
    def resume(*args): return apply(objectc.TProgram_resume,args)
    def syncScreenBuffer(*args): return apply(objectc.TProgram_syncScreenBuffer,args)
    def __repr__(self):
        return "<C TProgram instance at %s>" % (self.this,)

class TProgramPtr(TProgram):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TProgram
objectc.TProgram_swigregister(TProgramPtr)
class TApplication(TProgram):
    __setmethods__ = {}
    for _s in [TProgram]: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TApplication):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TApplication.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in [TProgram]: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TApplication.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<C TApplication instance at %s>" % (self.this,)

class TApplicationPtr(TApplication):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TApplication
objectc.TApplication_swigregister(TApplicationPtr)
class TDialog(TWindow):
    __setmethods__ = {}
    for _s in [TWindow]: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TDialog):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TDialog.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in [TWindow]: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TDialog.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __init__(self,*args):
        self.this = apply(objectc.new_TDialog,args)
        self.thisown = 1
    def getPalette(*args): return apply(objectc.TDialog_getPalette,args)
    def handleEvent(*args): return apply(objectc.TDialog_handleEvent,args)
    def valid(*args): return apply(objectc.TDialog_valid,args)
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TDialog(self)
    def __repr__(self):
        return "<C TDialog instance at %s>" % (self.this,)

class TDialogPtr(TDialog):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TDialog
objectc.TDialog_swigregister(TDialogPtr)
class TEditorApp(TApplication):
    __setmethods__ = {}
    for _s in [TApplication]: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TEditorApp):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TEditorApp.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in [TApplication]: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TEditorApp.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __init__(self,*args):
        self.this = apply(objectc.new_TEditorApp,args)
        self.thisown = 1
    def handleEvent(*args): return apply(objectc.TEditorApp_handleEvent,args)
    def outOfMemory(*args): return apply(objectc.TEditorApp_outOfMemory,args)
    def openEditor(*args): return apply(objectc.TEditorApp_openEditor,args)
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TEditorApp(self)
    def __repr__(self):
        return "<C TEditorApp instance at %s>" % (self.this,)

class TEditorAppPtr(TEditorApp):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TEditorApp
objectc.TEditorApp_swigregister(TEditorAppPtr)
class MsgBoxText:
    __setmethods__ = {}
    for _s in []: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,MsgBoxText):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = MsgBoxText.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in []: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = MsgBoxText.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __init__(self,*args):
        self.this = apply(objectc.new_MsgBoxText,args)
        self.thisown = 1
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_MsgBoxText(self)
    def __repr__(self):
        return "<C MsgBoxText instance at %s>" % (self.this,)

class MsgBoxTextPtr(MsgBoxText):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = MsgBoxText
objectc.MsgBoxText_swigregister(MsgBoxTextPtr)
class TListViewer(TView):
    __setmethods__ = {}
    for _s in [TView]: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TListViewer):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TListViewer.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in [TView]: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TListViewer.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __init__(self,*args):
        self.this = apply(objectc.new_TListViewer,args)
        self.thisown = 1
    def changeBounds(*args): return apply(objectc.TListViewer_changeBounds,args)
    def draw(*args): return apply(objectc.TListViewer_draw,args)
    def focusItem(*args): return apply(objectc.TListViewer_focusItem,args)
    def getPalette(*args): return apply(objectc.TListViewer_getPalette,args)
    def getText(*args): return apply(objectc.TListViewer_getText,args)
    def isSelected(*args): return apply(objectc.TListViewer_isSelected,args)
    def handleEvent(*args): return apply(objectc.TListViewer_handleEvent,args)
    def selectItem(*args): return apply(objectc.TListViewer_selectItem,args)
    def setRange(*args): return apply(objectc.TListViewer_setRange,args)
    def setState(*args): return apply(objectc.TListViewer_setState,args)
    def focusItemNum(*args): return apply(objectc.TListViewer_focusItemNum,args)
    def shutDown(*args): return apply(objectc.TListViewer_shutDown,args)
    __setmethods__["hScrollBar"] = objectc.TListViewer_hScrollBar_set
    __getmethods__["hScrollBar"] = objectc.TListViewer_hScrollBar_get
    __setmethods__["vScrollBar"] = objectc.TListViewer_vScrollBar_set
    __getmethods__["vScrollBar"] = objectc.TListViewer_vScrollBar_get
    __setmethods__["numCols"] = objectc.TListViewer_numCols_set
    __getmethods__["numCols"] = objectc.TListViewer_numCols_get
    __setmethods__["topItem"] = objectc.TListViewer_topItem_set
    __getmethods__["topItem"] = objectc.TListViewer_topItem_get
    __setmethods__["focused"] = objectc.TListViewer_focused_set
    __getmethods__["focused"] = objectc.TListViewer_focused_get
    __setmethods__["range"] = objectc.TListViewer_range_set
    __getmethods__["range"] = objectc.TListViewer_range_get
    __setmethods__["handleSpace"] = objectc.TListViewer_handleSpace_set
    __getmethods__["handleSpace"] = objectc.TListViewer_handleSpace_get
    def getExtraOptions(*args): return apply(objectc.TListViewer_getExtraOptions,args)
    def setExtraOptions(*args): return apply(objectc.TListViewer_setExtraOptions,args)
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TListViewer(self)
    def __repr__(self):
        return "<C TListViewer instance at %s>" % (self.this,)

class TListViewerPtr(TListViewer):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TListViewer
objectc.TListViewer_swigregister(TListViewerPtr)
class TListBoxRec:
    __setmethods__ = {}
    for _s in []: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TListBoxRec):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TListBoxRec.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in []: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TListBoxRec.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    __setmethods__["items"] = objectc.TListBoxRec_items_set
    __getmethods__["items"] = objectc.TListBoxRec_items_get
    __setmethods__["selection"] = objectc.TListBoxRec_selection_set
    __getmethods__["selection"] = objectc.TListBoxRec_selection_get
    def __init__(self,*args):
        self.this = apply(objectc.new_TListBoxRec,args)
        self.thisown = 1
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TListBoxRec(self)
    def __repr__(self):
        return "<C TListBoxRec instance at %s>" % (self.this,)

class TListBoxRecPtr(TListBoxRec):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TListBoxRec
objectc.TListBoxRec_swigregister(TListBoxRecPtr)
class TListBox(TListViewer):
    __setmethods__ = {}
    for _s in [TListViewer]: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TListBox):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TListBox.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in [TListViewer]: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TListBox.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __init__(self,*args):
        self.this = apply(objectc.new_TListBox,args)
        self.thisown = 1
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TListBox(self)
    def dataSize(*args): return apply(objectc.TListBox_dataSize,args)
    def getData(*args): return apply(objectc.TListBox_getData,args)
    def getText(*args): return apply(objectc.TListBox_getText,args)
    def newList(*args): return apply(objectc.TListBox_newList,args)
    def setData(*args): return apply(objectc.TListBox_setData,args)
    def list(*args): return apply(objectc.TListBox_list,args)
    def __repr__(self):
        return "<C TListBox instance at %s>" % (self.this,)

class TListBoxPtr(TListBox):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TListBox
objectc.TListBox_swigregister(TListBoxPtr)
class TMethodHolder:
    __setmethods__ = {}
    for _s in []: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TMethodHolder):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TMethodHolder.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in []: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TMethodHolder.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def initStatusLine(*args): return apply(objectc.TMethodHolder_initStatusLine,args)
    def initMenuBar(*args): return apply(objectc.TMethodHolder_initMenuBar,args)
    def initDeskTop(*args): return apply(objectc.TMethodHolder_initDeskTop,args)
    def __init__(self,*args):
        self.this = apply(objectc.new_TMethodHolder,args)
        self.thisown = 1
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TMethodHolder(self)
    def __repr__(self):
        return "<C TMethodHolder instance at %s>" % (self.this,)

class TMethodHolderPtr(TMethodHolder):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TMethodHolder
objectc.TMethodHolder_swigregister(TMethodHolderPtr)
class TAppWrapper(TApplication):
    __setmethods__ = {}
    for _s in [TApplication]: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,TAppWrapper):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = TAppWrapper.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in [TApplication]: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = TAppWrapper.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    def __init__(self,*args):
        self.this = apply(objectc.new_TAppWrapper,args)
        self.thisown = 1
    def __del__(self,objectc=objectc):
        if getattr(self,'thisown',0):
            objectc.delete_TAppWrapper(self)
    def __repr__(self):
        return "<C TAppWrapper instance at %s>" % (self.this,)

class TAppWrapperPtr(TAppWrapper):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = TAppWrapper
objectc.TAppWrapper_swigregister(TAppWrapperPtr)
cvar = objectc.cvar
streamableInit = objectc.streamableInit
TObject_destroy = objectc.TObject_destroy

THWMouse_forceEvent = objectc.THWMouse_forceEvent

TMouse_show = objectc.TMouse_show

TMouse_hide = objectc.TMouse_hide

TMouse_suspend = objectc.TMouse_suspend

TMouse_resume = objectc.TMouse_resume

TMouse_setRange = objectc.TMouse_setRange

TMouse_getEvent = objectc.TMouse_getEvent

TMouse_present = objectc.TMouse_present

TMouse_resetDrawCounter = objectc.TMouse_resetDrawCounter

TMouse_getDrawCounter = objectc.TMouse_getDrawCounter

TStringCollection_build = objectc.TStringCollection_build

TView_commandEnabled = objectc.TView_commandEnabled

TView_disableCommands = objectc.TView_disableCommands

TView_enableCommands = objectc.TView_enableCommands

TView_disableCommand = objectc.TView_disableCommand

TView_enableCommand = objectc.TView_enableCommand

TView_getCommands = objectc.TView_getCommands

TView_setCommands = objectc.TView_setCommands

TView_build = objectc.TView_build

TGroup_build = objectc.TGroup_build

TWindow_initFrame = objectc.TWindow_initFrame

TWindow_build = objectc.TWindow_build

TButton_build = objectc.TButton_build

TStatusLine_build = objectc.TStatusLine_build

dsktTileVertical = objectc.dsktTileVertical
dsktTileHorizontal = objectc.dsktTileHorizontal
TDeskTop_initBackground = objectc.TDeskTop_initBackground

TDeskTop_build = objectc.TDeskTop_build

cpColor = objectc.cpColor
cpBlackWhite = objectc.cpBlackWhite
cpMonochrome = objectc.cpMonochrome
TProgram_initStatusLine = objectc.TProgram_initStatusLine

TProgram_initMenuBar = objectc.TProgram_initMenuBar

TProgram_initDeskTop = objectc.TProgram_initDeskTop

TProgram_resetIdleTime = objectc.TProgram_resetIdleTime

cmValid = objectc.cmValid
cmQuit = objectc.cmQuit
cmError = objectc.cmError
cmMenu = objectc.cmMenu
cmClose = objectc.cmClose
cmZoom = objectc.cmZoom
cmResize = objectc.cmResize
cmNext = objectc.cmNext
cmPrev = objectc.cmPrev
cmHelp = objectc.cmHelp
cmOK = objectc.cmOK
cmCancel = objectc.cmCancel
cmYes = objectc.cmYes
cmNo = objectc.cmNo
cmDefault = objectc.cmDefault
sfVisible = objectc.sfVisible
sfCursorVis = objectc.sfCursorVis
sfCursorIns = objectc.sfCursorIns
sfShadow = objectc.sfShadow
sfActive = objectc.sfActive
sfSelected = objectc.sfSelected
sfFocused = objectc.sfFocused
sfDragging = objectc.sfDragging
sfDisabled = objectc.sfDisabled
sfModal = objectc.sfModal
sfDefault = objectc.sfDefault
sfExposed = objectc.sfExposed
ofSelectable = objectc.ofSelectable
ofTopSelect = objectc.ofTopSelect
ofFirstClick = objectc.ofFirstClick
ofFramed = objectc.ofFramed
ofPreProcess = objectc.ofPreProcess
ofPostProcess = objectc.ofPostProcess
ofBuffered = objectc.ofBuffered
ofTileable = objectc.ofTileable
ofCenterX = objectc.ofCenterX
ofCenterY = objectc.ofCenterY
ofCentered = objectc.ofCentered
ofBeVerbose = objectc.ofBeVerbose
gfGrowLoX = objectc.gfGrowLoX
gfGrowLoY = objectc.gfGrowLoY
gfGrowHiX = objectc.gfGrowHiX
gfGrowHiY = objectc.gfGrowHiY
gfGrowAll = objectc.gfGrowAll
gfGrowRel = objectc.gfGrowRel
dmDragMove = objectc.dmDragMove
dmDragGrow = objectc.dmDragGrow
dmLimitLoX = objectc.dmLimitLoX
dmLimitLoY = objectc.dmLimitLoY
dmLimitHiX = objectc.dmLimitHiX
dmLimitHiY = objectc.dmLimitHiY
dmLimitAll = objectc.dmLimitAll
hcNoContext = objectc.hcNoContext
hcDragging = objectc.hcDragging
sbLeftArrow = objectc.sbLeftArrow
sbRightArrow = objectc.sbRightArrow
sbPageLeft = objectc.sbPageLeft
sbPageRight = objectc.sbPageRight
sbUpArrow = objectc.sbUpArrow
sbDownArrow = objectc.sbDownArrow
sbPageUp = objectc.sbPageUp
sbPageDown = objectc.sbPageDown
sbIndicator = objectc.sbIndicator
sbHorizontal = objectc.sbHorizontal
sbVertical = objectc.sbVertical
sbHandleKeyboard = objectc.sbHandleKeyboard
wfMove = objectc.wfMove
wfGrow = objectc.wfGrow
wfClose = objectc.wfClose
wfZoom = objectc.wfZoom
noMenuBar = objectc.noMenuBar
noDeskTop = objectc.noDeskTop
noStatusLine = objectc.noStatusLine
noBackground = objectc.noBackground
noFrame = objectc.noFrame
noViewer = objectc.noViewer
noHistory = objectc.noHistory
wnNoNumber = objectc.wnNoNumber
wpBlueWindow = objectc.wpBlueWindow
wpCyanWindow = objectc.wpCyanWindow
wpGrayWindow = objectc.wpGrayWindow
cmCut = objectc.cmCut
cmCopy = objectc.cmCopy
cmPaste = objectc.cmPaste
cmUndo = objectc.cmUndo
cmClear = objectc.cmClear
cmTile = objectc.cmTile
cmCascade = objectc.cmCascade
cmReceivedFocus = objectc.cmReceivedFocus
cmReleasedFocus = objectc.cmReleasedFocus
cmCommandSetChanged = objectc.cmCommandSetChanged
cmScrollBarChanged = objectc.cmScrollBarChanged
cmScrollBarClicked = objectc.cmScrollBarClicked
cmSelectWindowNum = objectc.cmSelectWindowNum
cmListItemSelected = objectc.cmListItemSelected
cmClosingWindow = objectc.cmClosingWindow
cmClusterMovedTo = objectc.cmClusterMovedTo
cmClusterPress = objectc.cmClusterPress
cmRecordHistory = objectc.cmRecordHistory
cmListItemFocused = objectc.cmListItemFocused
cmGrabDefault = objectc.cmGrabDefault
cmReleaseDefault = objectc.cmReleaseDefault
cmUpdateCodePage = objectc.cmUpdateCodePage
cmCallShell = objectc.cmCallShell
positionalEvents = objectc.positionalEvents
focusedEvents = objectc.focusedEvents
kbSpace = objectc.kbSpace
kbCtrlA = objectc.kbCtrlA
kbCtrlB = objectc.kbCtrlB
kbCtrlC = objectc.kbCtrlC
kbCtrlD = objectc.kbCtrlD
kbCtrlE = objectc.kbCtrlE
kbCtrlF = objectc.kbCtrlF
kbCtrlG = objectc.kbCtrlG
kbCtrlH = objectc.kbCtrlH
kbCtrlI = objectc.kbCtrlI
kbCtrlJ = objectc.kbCtrlJ
kbCtrlK = objectc.kbCtrlK
kbCtrlL = objectc.kbCtrlL
kbCtrlM = objectc.kbCtrlM
kbCtrlN = objectc.kbCtrlN
kbCtrlO = objectc.kbCtrlO
kbCtrlP = objectc.kbCtrlP
kbCtrlQ = objectc.kbCtrlQ
kbCtrlR = objectc.kbCtrlR
kbCtrlS = objectc.kbCtrlS
kbCtrlT = objectc.kbCtrlT
kbCtrlU = objectc.kbCtrlU
kbCtrlV = objectc.kbCtrlV
kbCtrlW = objectc.kbCtrlW
kbCtrlX = objectc.kbCtrlX
kbCtrlY = objectc.kbCtrlY
kbCtrlZ = objectc.kbCtrlZ
kbEsc = objectc.kbEsc
kbAltSpace = objectc.kbAltSpace
kbCtrlIns = objectc.kbCtrlIns
kbShiftIns = objectc.kbShiftIns
kbCtrlDel = objectc.kbCtrlDel
kbShiftDel = objectc.kbShiftDel
kbCtrlShiftIns = objectc.kbCtrlShiftIns
kbCtrlShiftDel = objectc.kbCtrlShiftDel
kbBack = objectc.kbBack
kbCtrlBack = objectc.kbCtrlBack
kbShiftTab = objectc.kbShiftTab
kbTab = objectc.kbTab
kbAltA = objectc.kbAltA
kbAltB = objectc.kbAltB
kbAltC = objectc.kbAltC
kbAltD = objectc.kbAltD
kbAltE = objectc.kbAltE
kbAltF = objectc.kbAltF
kbAltG = objectc.kbAltG
kbAltH = objectc.kbAltH
kbAltI = objectc.kbAltI
kbAltJ = objectc.kbAltJ
kbAltK = objectc.kbAltK
kbAltL = objectc.kbAltL
kbAltM = objectc.kbAltM
kbAltN = objectc.kbAltN
kbAltO = objectc.kbAltO
kbAltP = objectc.kbAltP
kbAltQ = objectc.kbAltQ
kbAltR = objectc.kbAltR
kbAltS = objectc.kbAltS
kbAltT = objectc.kbAltT
kbAltU = objectc.kbAltU
kbAltV = objectc.kbAltV
kbAltW = objectc.kbAltW
kbAltX = objectc.kbAltX
kbAltY = objectc.kbAltY
kbAltZ = objectc.kbAltZ
kbCtrlEnter = objectc.kbCtrlEnter
kbEnter = objectc.kbEnter
kbF1 = objectc.kbF1
kbF2 = objectc.kbF2
kbF3 = objectc.kbF3
kbF4 = objectc.kbF4
kbF5 = objectc.kbF5
kbF6 = objectc.kbF6
kbF7 = objectc.kbF7
kbF8 = objectc.kbF8
kbF9 = objectc.kbF9
kbF10 = objectc.kbF10
kbF11 = objectc.kbF11
kbF12 = objectc.kbF12
kbHome = objectc.kbHome
kbUp = objectc.kbUp
kbPgUp = objectc.kbPgUp
kbLeft = objectc.kbLeft
kbRight = objectc.kbRight
kbEnd = objectc.kbEnd
kbDown = objectc.kbDown
kbPgDn = objectc.kbPgDn
kbIns = objectc.kbIns
kbDel = objectc.kbDel
kbGrayMinus = objectc.kbGrayMinus
kbGrayPlus = objectc.kbGrayPlus
kbShiftF1 = objectc.kbShiftF1
kbShiftF2 = objectc.kbShiftF2
kbShiftF3 = objectc.kbShiftF3
kbShiftF4 = objectc.kbShiftF4
kbShiftF5 = objectc.kbShiftF5
kbShiftF6 = objectc.kbShiftF6
kbShiftF7 = objectc.kbShiftF7
kbShiftF8 = objectc.kbShiftF8
kbShiftF9 = objectc.kbShiftF9
kbShiftF10 = objectc.kbShiftF10
kbShiftF11 = objectc.kbShiftF11
kbShiftF12 = objectc.kbShiftF12
kbCtrlF1 = objectc.kbCtrlF1
kbCtrlF2 = objectc.kbCtrlF2
kbCtrlF3 = objectc.kbCtrlF3
kbCtrlF4 = objectc.kbCtrlF4
kbCtrlF5 = objectc.kbCtrlF5
kbCtrlF6 = objectc.kbCtrlF6
kbCtrlF7 = objectc.kbCtrlF7
kbCtrlF8 = objectc.kbCtrlF8
kbCtrlF9 = objectc.kbCtrlF9
kbCtrlF10 = objectc.kbCtrlF10
kbCtrlF11 = objectc.kbCtrlF11
kbCtrlF12 = objectc.kbCtrlF12
kbAltF1 = objectc.kbAltF1
kbAltF2 = objectc.kbAltF2
kbAltF3 = objectc.kbAltF3
kbAltF4 = objectc.kbAltF4
kbAltF5 = objectc.kbAltF5
kbAltF6 = objectc.kbAltF6
kbAltF7 = objectc.kbAltF7
kbAltF8 = objectc.kbAltF8
kbAltF9 = objectc.kbAltF9
kbAltF10 = objectc.kbAltF10
kbAltF11 = objectc.kbAltF11
kbAltF12 = objectc.kbAltF12
kbCtrlPrtSc = objectc.kbCtrlPrtSc
kbCtrlLeft = objectc.kbCtrlLeft
kbCtrlRight = objectc.kbCtrlRight
kbCtrlEnd = objectc.kbCtrlEnd
kbCtrlPgDn = objectc.kbCtrlPgDn
kbCtrlHome = objectc.kbCtrlHome
kbAlt1 = objectc.kbAlt1
kbAlt2 = objectc.kbAlt2
kbAlt3 = objectc.kbAlt3
kbAlt4 = objectc.kbAlt4
kbAlt5 = objectc.kbAlt5
kbAlt6 = objectc.kbAlt6
kbAlt7 = objectc.kbAlt7
kbAlt8 = objectc.kbAlt8
kbAlt9 = objectc.kbAlt9
kbAlt0 = objectc.kbAlt0
kbAltMinus = objectc.kbAltMinus
kbAltEqual = objectc.kbAltEqual
kbCtrlPgUp = objectc.kbCtrlPgUp
kbNoKey = objectc.kbNoKey
kbAltBack = objectc.kbAltBack
kbRightShift = objectc.kbRightShift
kbLeftShift = objectc.kbLeftShift
kbShift = objectc.kbShift
kbLeftCtrl = objectc.kbLeftCtrl
kbRightCtrl = objectc.kbRightCtrl
kbCtrlShift = objectc.kbCtrlShift
kbLeftAlt = objectc.kbLeftAlt
kbRightAlt = objectc.kbRightAlt
kbAltShift = objectc.kbAltShift
kbScrollState = objectc.kbScrollState
kbNumState = objectc.kbNumState
kbCapsState = objectc.kbCapsState
kbInsState = objectc.kbInsState
TDialog_build = objectc.TDialog_build

TEditorApp_initMenuBar = objectc.TEditorApp_initMenuBar

TEditorApp_initStatusLine = objectc.TEditorApp_initStatusLine

execDialog = objectc.execDialog

createFindDialog = objectc.createFindDialog

createReplaceDialog = objectc.createReplaceDialog

bfNormal = objectc.bfNormal
bfDefault = objectc.bfDefault
bfLeftJust = objectc.bfLeftJust
bfBroadcast = objectc.bfBroadcast
messageBox = objectc.messageBox

messageBoxRect = objectc.messageBoxRect

inputBox = objectc.inputBox

inputBoxRect = objectc.inputBoxRect

mfWarning = objectc.mfWarning
mfError = objectc.mfError
mfInformation = objectc.mfInformation
mfConfirmation = objectc.mfConfirmation
mfYesButton = objectc.mfYesButton
mfNoButton = objectc.mfNoButton
mfOKButton = objectc.mfOKButton
mfCancelButton = objectc.mfCancelButton
mfDontTranslate = objectc.mfDontTranslate
mfDontShowAgain = objectc.mfDontShowAgain
mfYesNoCancel = objectc.mfYesNoCancel
mfOKCancel = objectc.mfOKCancel
TListViewer_build = objectc.TListViewer_build

TListBox_build = objectc.TListBox_build


