%{
#define Uses_TPalette
#include <tv.h>
%}

class TPalette
{

public:

    TPalette( const char *, ushort );
    TPalette( const TPalette& );
    ~TPalette();

    TPalette& operator = ( const TPalette& );

    uchar& operator[]( int index) const
    {
        return data[index];
    }

    uchar *data;

};

