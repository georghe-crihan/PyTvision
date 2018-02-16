%{
#define Uses_TMenuItem
#include <tv.h>
%}

class TMenu;

class TMenuItem
{

public:

    TMenuItem( const char *aName,
               ushort aCommand,
               ushort aKeyCode,
               ushort aHelpCtx = hcNoContext,
               char *p = 0,
               TMenuItem *aNext = 0
             );
    TMenuItem( const char *aName,
               ushort aKeyCode,
               TMenu *aSubMenu,
               ushort aHelpCtx = hcNoContext,
               TMenuItem *aNext = 0
             );

    ~TMenuItem();

    void append( TMenuItem *aNext );
%pythoncode
%{
def append(self, p):
    p.thisown = 0
    return _tv.TMenuItem_append(self, p)
%}

    TMenuItem *next;
    const char *name;
    stTVIntl *intlName;
    ushort command;
    Boolean disabled;
    ushort keyCode;
    ushort helpCtx;
    union
        {
        const char *param;
        TMenu *subMenu;
        };

};

