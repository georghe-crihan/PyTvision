%{
#define Uses_TSItem
#include <tv.h>
%}


class TSItem
{

public:

    TSItem( const char *aValue, TSItem *aNext )
        { value = newStr(aValue); next = aNext; }
    ~TSItem() { DeleteArray((char *)value); }
    void append( TSItem *aNext ); // SET: I put it in the same source as TCluster
%pythoncode
%{
def __add__(self, b):
    self.append(b)
    return self
%}
    const char *value;
    TSItem *next;
};

