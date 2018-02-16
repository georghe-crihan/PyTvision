%module object

%{
#include <stddef.h>
#define Uses_TObject
#include <tv.h>
%}

class TObject {
public:
    virtual ~TObject();
    static void CLY_destroy( TObject * );
    virtual void shutDown();
private:
};


