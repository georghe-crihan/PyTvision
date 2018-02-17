/* ---------------------------------------------------------------------- */
/*      class TMenuBar                                                    */
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
#define Uses_TMenuBar
#include <tv.h>
%}

class TRect;
class TMenu;

class TMenuBar : public TMenuView
{

public:

    TMenuBar( const TRect& bounds, TMenu *aMenu );
    TMenuBar( const TRect& bounds, TSubMenu &aMenu );
    ~TMenuBar();

    void computeLength();
    virtual void draw();
    virtual TRect getItemRect( TMenuItem *item );
    virtual void changeBounds(const TRect& bounds);
    
#if !defined( NO_STREAM )
private:

    virtual const char *streamableName() const
        { return name; }

protected:

    TMenuBar( StreamableInit );

public:

    static const char * const name;
    static TStreamable *build();
#endif // NO_STREAM
};

