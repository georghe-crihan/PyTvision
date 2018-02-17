%module point
%{
#define Uses_TPoint
#include <tv.h>
%}

class TPoint
{

public:

    TPoint& operator+=( const TPoint& adder );
    TPoint& operator-=( const TPoint& subber );
/*
    friend TPoint operator - ( const TPoint& one, const TPoint& two);
    friend TPoint operator + ( const TPoint& one, const TPoint& two);
    friend int operator == ( const TPoint& one, const TPoint& two);
    friend int operator != ( const TPoint& one, const TPoint& two);
*/

    int x,y;

};

