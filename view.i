%module view
%{
#define Uses_TView
#include <tv.h>
%}

struct write_args
{
    void *self;
    void *target;
    void *buf;
    ushort offset;
};

class TRect;
struct TEvent;
class TGroup;
class TPalette;
class TCommandSet;

class TView : public TObject
#if !defined ( NO_STREAM )
                             , public TStreamable
#endif // NO_STREAM
{

public:

    friend void genRefs();

    enum phaseType { phFocused, phPreProcess, phPostProcess };
    enum selectMode{ normalSelect, enterSelect, leaveSelect };

    TView( const TRect& bounds );
    ~TView();

    virtual void sizeLimits( TPoint& min, TPoint& max );
    TRect getBounds();
    TRect getExtent();
    TRect getClipRect();
    Boolean mouseInView( TPoint mouse );
    Boolean containsMouse( TEvent& event );

    void locate( TRect& bounds );
    virtual void dragView( TEvent& event, uchar mode,   //  temporary fix
      TRect& limits, TPoint minSize, TPoint maxSize ); //  for Miller's stuff
    virtual void calcBounds( TRect& bounds, TPoint delta );
    virtual void changeBounds( const TRect& bounds );
    void growTo( int x, int y );
    void moveTo( int x, int y );
    void setBounds( const TRect& bounds );

    virtual ushort getHelpCtx();

    virtual Boolean valid( ushort command );

    void hide();
    void show();
    virtual void draw();
    void drawView();
    Boolean exposed();
    void hideCursor();
    void drawHide( TView *lastView );
    void drawShow( TView *lastView );
    void drawUnderRect( TRect& r, TView *lastView );
    void drawUnderView( Boolean doShadow, TView *lastView );

    virtual uint32 dataSize();
    virtual void getData( void *rec );
    virtual void setData( void *rec );

    void blockCursor();
    void normalCursor();
    virtual void resetCursor();
    void setCursor( int x, int y );
    void showCursor();
    void drawCursor();

    void clearEvent( TEvent& event );
    Boolean eventAvail();
    virtual void getEvent( TEvent& event );
    virtual void handleEvent( TEvent& event );
    virtual void putEvent( TEvent& event );

    static Boolean commandEnabled( ushort command );
    static void disableCommands( TCommandSet& commands );
    static void enableCommands( TCommandSet& commands );
    static void disableCommand( ushort command );
    static void enableCommand( ushort command );
    static void getCommands( TCommandSet& commands );
    static void setCommands( TCommandSet& commands );

    virtual void endModal( ushort command );
    virtual ushort execute();

    ushort getColor( ushort color );
    virtual TPalette& getPalette() const;
    uchar mapColor( uchar );

    Boolean getState( ushort aState );
    void select();
    virtual void setState( ushort aState, Boolean enable );

    void keyEvent( TEvent& event );
    Boolean mouseEvent( TEvent& event, ushort mask );


    TPoint makeGlobal( TPoint source );
    TPoint makeLocal( TPoint source );

    TView *nextView();
    TView *prevView();
    TView *prev();
    TView *next;

    void makeFirst();
    void putInFrontOf( TView *Target );
    TView *TopView();

    // For old code bypassing TDrawBuffer and encoding using 8 bit chars
    void writeBuf(int x, int y, int w, int h, const void *b);
    // Best choice because the TDrawBuffer says which format is used
    void writeBuf(int x, int y, int w, int h, TDrawBufferBase& b);
    // For new code that want to bypass TDrawBuffer and knows the screen format
    void writeNativeBuf(int x, int y, int w, int h, const void *Buffer);

    void writeLine(int x, int y, int w, int h, const void *b);
    void writeLine(int x, int y, int w, int h, TDrawBufferBase& b);
    void writeNativeLine(int x, int y, int w, int h, const void *b);

    void writeChar(int x, int y, char c, uchar color, int count);
    void writeCharU16(int x, int y, unsigned c, unsigned color, int count);

    void writeStr(int x, int y, const char *str, uchar color);
    void writeStrU16(int x, int y, const uint16 *str, unsigned color);

    TPoint size;
    ushort options;
    ushort eventMask;
    ushort state;
    TPoint origin;
    TPoint cursor;
    uchar growMode;
    uchar dragMode;
    ushort helpCtx;
    static Boolean commandSetChanged;
    static TCommandSet curCommandSet;
    TGroup *owner;

    static Boolean showMarkers;
    static uchar errorAttr;

    virtual void shutDown();

    // SET: These are shared by various TView members.
    // I moved it to a class because I think is better to enclose them.
//    static uchar specialChars[];
//    static uchar ospecialChars[];

private:

    void moveGrow( TPoint p,
                   TPoint s,
                   TRect& limits,
                   TPoint minSize,
                   TPoint maxSize,
                   uchar mode
                 );
    void change( uchar, TPoint delta, TPoint& p, TPoint& s, int grow=0 );
    static void writeView( write_args );

#if !defined( NO_STREAM )
    virtual const char *streamableName() const
        { return name; }

protected:

    TView( StreamableInit );

public:

    static const char * const name;
    static TStreamable *build();

protected:

    virtual void write( opstream& );
    virtual void *read( ipstream& );
#endif // NO_STREAM
};


