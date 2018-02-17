%module rect
%{
#define Uses_TRect
#include <tv.h>
%}

class TRect
{

public:

    TRect( int ax, int ay, int bx, int by );
    TRect( TPoint p1, TPoint p2 );
    TRect();

    void move( int aDX, int aDY );
    void grow( int aDX, int aDY );
    void intersect( const TRect& r );
    void Union( const TRect& r );
    Boolean contains( const TPoint& p ) const;
    Boolean operator == ( const TRect& r ) const;
    Boolean operator != ( const TRect& r ) const;
    Boolean isEmpty();

    TPoint a, b;

};

