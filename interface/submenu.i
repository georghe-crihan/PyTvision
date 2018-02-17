%{
#define Uses_TSubMenu
#include <tv.h>
%}

class TSubMenu : public TMenuItem
{

public:

    TSubMenu( const char *, ushort, ushort = hcNoContext );

};
