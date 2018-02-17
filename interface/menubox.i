/* ---------------------------------------------------------------------- */
/*      class TMenuBox                                                    */
/*                                                                        */
/*      Palette layout                                                    */
/*        1 = Normal text                                                 */
/*        2 = Disabled text                                               */
/*        3 = Shortcut text                                               */
/*        4 = Normal selection                                            */
/*        5 = Disabled selection                                          */
/*        6 = Shortcut selection                                          */
/* ---------------------------------------------------------------------- */

%{
#define Uses_TMenuBox
#include <tv.h>
%}


class TRect;
class TMenu;
class TMenuView;
class TDrawBuffer;

class TMenuBox : public TMenuView
{

public:

    TMenuBox( const TRect& bounds, TMenu *aMenu, TMenuView *aParentMenu);

    virtual void draw();
    virtual TRect getItemRect( TMenuItem *item );

    static char frameChars[20];
    static char oframeChars[20];
    static char rightArrow;
    static char orightArrow;

private:

    void frameLine( TDrawBuffer&, short n );
    void drawLine( TDrawBuffer& );

#if !defined( NO_STREAM )
    virtual const char *streamableName() const
        { return name; }

protected:

    TMenuBox( StreamableInit );

public:

    static const char * const name;
    static TStreamable *build();
#endif // NO_STREAM
};
