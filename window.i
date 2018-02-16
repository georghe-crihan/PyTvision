%module window
%{
#define Uses_TWindow
#include <tv.h>
%}

class TFrame;
class TRect;
class TPoint;
struct TEvent;
class TFrame;
class TScrollBar;

class TWindowInit
{

public:

    TWindowInit( TFrame *(*cFrame)( TRect ) );
    virtual TFrame *defaultInitFrame( TRect& rect);

protected:

    TFrame *(*createFrame)( TRect );

};

/* ---------------------------------------------------------------------- */
/*      class TWindow                                                     */
/*                                                                        */
/*      Palette layout                                                    */
/*        1 = Frame passive                                               */
/*        2 = Frame active                                                */
/*        3 = Frame icon                                                  */
/*        4 = ScrollBar page area                                         */
/*        5 = ScrollBar controls                                          */
/*        6 = Scroller normal text                                        */
/*        7 = Scroller selected text                                      */
/*        8 = Reserved                                                    */
/* ---------------------------------------------------------------------- */

%feature("director") TWindow;

class TRect;

class TWindow: public TGroup, public virtual TWindowInit
{

public:

    TWindow( const TRect& bounds,
	     const char *aTitle,
	     short aNumber
	   );
    ~TWindow();

    virtual void close();
    virtual TPalette& getPalette() const;
    virtual const char *getTitle( short maxSize );
    virtual void handleEvent( TEvent& event );
    static TFrame *initFrame( TRect );
    virtual void setState( ushort aState, Boolean enable );
    virtual void sizeLimits( TPoint& min, TPoint& max );
    TScrollBar *standardScrollBar( ushort aOptions );
    virtual void zoom();
    virtual void shutDown();

    uchar flags;
    TRect zoomRect;
    short number;
    short palette;
    TFrame *frame;
    const char *title;
    stTVIntl   *intlTitle;
#if !defined( NO_STREAM )
private:

    virtual const char *streamableName() const
	{ return name; }

protected:

    TWindow( StreamableInit );
    virtual void write( opstream& );
    virtual void *read( ipstream& );

public:

    static const char * const name;
    static TStreamable *build();
#endif // NO_STREAM
};

