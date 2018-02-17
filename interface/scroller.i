/* ---------------------------------------------------------------------- */
/*      class TScroller                                                   */
/*                                                                        */
/*      Palette layout                                                    */
/*      1 = Normal text                                                   */
/*      2 = Selected text                                                 */
/* ---------------------------------------------------------------------- */

%{
#define Uses_TScroller
#include <tv.h>
%}


class TRect;
class TScrollBar;
struct TEvent;

class TScroller : public TView
{

public:

    TScroller( const TRect& bounds,
               TScrollBar *aHScrollBar,
               TScrollBar *aVScrollBar
             );

    virtual void changeBounds( const TRect& bounds );
    virtual TPalette& getPalette() const;
    virtual void handleEvent( TEvent& event );
    virtual void scrollDraw();
    void scrollTo( int32 x, int32 y );
    void setLimit( int32 x, int32 y );
    virtual void setState( ushort aState, Boolean enable );
    void checkDraw();
    virtual void shutDown();

    // How many lines we will scroll when the mouse wheel is used.
    static int defaultWheelStep;
    int wheelStep;

protected:

    uchar drawLock;
    Boolean drawFlag;
    TScrollBar *hScrollBar;
    TScrollBar *vScrollBar;
    TPoint delta;
    TPoint limit;

private:

    void showSBar( TScrollBar *sBar );
#if !defined( NO_STREAM )
    virtual const char *streamableName() const
	{ return name; }

protected:

    TScroller( StreamableInit );
    virtual void write( opstream& );
    virtual void *read( ipstream& );

public:

    static const char * const name;
    static TStreamable *build();
#endif // NO_STREAM
};

