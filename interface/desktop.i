%module desktop
%{
#define Uses_TDeskTop
#include <tv.h>
%}

// SET: To set the tile partition priority
enum { dsktTileVertical=1, dsktTileHorizontal=0 };

class TBackground;
class TRect;
struct TEvent;

class TDeskInit
{
public:
    TDeskInit( TBackground *(*cBackground)( TRect ) );

protected:
    TBackground *(*createBackground)( TRect );
};

class TDeskTop : public TGroup, public virtual TDeskInit
{

public:

    TDeskTop( const TRect& );

    void cascade( const TRect& );
    virtual void handleEvent( TEvent& );
    static TBackground *initBackground( TRect );
    void tile( const TRect& );
    virtual void tileError();
    virtual void shutDown();
    TBackground *getBackground(void) { return background; }
    // SET: Added to setup the tileable options
    unsigned getOptions() { return flagsOptions; }
    void setOptions(unsigned aFlags) { flagsOptions=aFlags; }
    virtual Boolean canShowCursor();
    // SET: Added to help Braille Terminals
    virtual ushort execView( TView *p );

    // SET: Made non-constant and added original
    static char defaultBkgrnd;
    static char odefaultBkgrnd;

protected:

    TBackground *background;
    unsigned flagsOptions;

private:

#if !defined( NO_STREAM )
    virtual const char *streamableName() const
        { return name; }

protected:

    TDeskTop( StreamableInit );

public:

    static const char * const name;
    static TStreamable *build();
#endif // NO_STREAM
};

