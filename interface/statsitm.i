%module statsitm
%{
#define Uses_TStatusItem
#include <tv.h>
%}

class TStatusItem
{

public:

    TStatusItem( const char *aText,
                 ushort key,
                 ushort cmd,
                 TStatusItem *aNext = 0
                );
    ~TStatusItem() { DeleteArray(text); TVIntl::freeSt(intlText); };

    TStatusItem *next;
    const char *text;
    stTVIntl *intlText;
    ushort keyCode;
    ushort command;

};


