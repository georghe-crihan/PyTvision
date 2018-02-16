%module group
%{
#define Uses_TGroup
#include <tv.h>
%}

class TGroup : public TView
{

public:

//    friend void genRefs();

    TGroup( const TRect& bounds );
    ~TGroup();

    virtual void shutDown();

    ushort execView( TView *p );
    virtual ushort execute();

    void insertView( TView *p, TView *Target );
    void remove( TView *p );
    void removeView( TView *p );
    void resetCurrent();
    void setCurrent( TView *p, TView::selectMode mode );
    void selectNext( Boolean forwards );
    TView *firstThat( Boolean (*func)( TView *, void * ), void *args );
    void forEach( void (*func)( TView *, void * ), void *args );
    void insert( TView *p );
%pythoncode
%{
def insert(self, p):
    p.thisown = 0
    return _tv.TGroup_insert(self, p)
%}
    void insertBefore( TView *p, TView *Target );
%pythoncode
%{
def insertBefore(self, p):
    p.thisown = 0
    return _tv.TGroup_insertBefore(self, p)
%}
    TView *current;
    TView *at( short index );
    TView *firstMatch( ushort aState, ushort aOptions );
    short indexOf( TView *p );
// !!! link error
//    Boolean matches( TView *p );
    TView *first();

    virtual void setState( ushort aState, Boolean enable );

    virtual void handleEvent( TEvent& event );

    void drawSubViews( TView *p, TView *bottom );

    virtual void changeBounds( const TRect& bounds );

    virtual uint32 dataSize();
    virtual void getData( void *rec );
    virtual void setData( void *rec );

    virtual void draw();
    void redraw();
    void Redraw();
    void lock();
    void unlock();
    virtual void resetCursor();
    // SET: A view should ask your owner (a group) if that's right
    // time to show the cursor or we are locked.
    virtual Boolean canShowCursor();

    virtual void endModal( ushort command );

    virtual void eventError( TEvent& event );

    virtual ushort getHelpCtx();

    virtual Boolean valid( ushort command );

    void freeBuffer();
    void getBuffer();

    TView *last;

    TRect clip;
    phaseType phase;

    ushort *buffer;
    uchar lockFlag;
    ushort endState;

private:

    Boolean invalid( TView *p, ushort command );
    void focusView( TView *p, Boolean enable );
    void selectView( TView *p, Boolean enable );
#if !defined( NO_STREAM )
    virtual const char *streamableName() const
	{ return name; }

protected:

    TGroup( StreamableInit );
    virtual void write( opstream& );
    virtual void *read( ipstream& );

public:

    static const char * const name;
    static TStreamable *build();
#endif // NO_STREAM


};


