# This file was created automatically by SWIG.
import tobjectc
class TObjectPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self,tobjectc=tobjectc):
        if self.thisown == 1 :
            tobjectc.delete_TObject(self)
    def shutDown(self, *_args, **_kwargs):
        val = apply(tobjectc.TObject_shutDown,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C TObject instance at %s>" % (self.this,)
class TObject(TObjectPtr):
    def __init__(self,this):
        self.this = this






#-------------- FUNCTION WRAPPERS ------------------

TObject_CLY_destroy = tobjectc.TObject_CLY_destroy



#-------------- VARIABLE WRAPPERS ------------------

