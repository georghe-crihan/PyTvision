%module statsdef
%{
#define Uses_TStatusDef
#include <tv.h>
%}

class TStatusDef
{

public:

    TStatusDef( ushort aMin,
                ushort aMax,
                TStatusItem *someItems = 0,
                TStatusDef *aNext = 0
              );

    TStatusDef *next;
    ushort min;
    ushort max;
    TStatusItem *items;
};



