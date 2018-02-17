%module listbox
%{
#define Uses_TListViewer
#include <tv.h>
%}


class TRect;
class TScrollBar;
struct TEvent;

class TListViewer : public TView
{

public:

    TListViewer( const TRect& bounds,
		 ushort aNumCols,
		 TScrollBar *aHScrollBar,
		 TScrollBar *aVScrollBar
	       );

    virtual void changeBounds( const TRect& bounds );
    virtual void draw();
    virtual void focusItem( ccIndex item );
    virtual TPalette& getPalette() const;
    virtual void getText( char *dest, ccIndex item, short maxLen );
    virtual Boolean isSelected( ccIndex item );
    virtual void handleEvent( TEvent& event );
    virtual void selectItem( ccIndex item );
    void setRange( ccIndex aRange );
    virtual void setState( ushort aState, Boolean enable );

    virtual void focusItemNum( ccIndex item );
    virtual void shutDown();

    TScrollBar *hScrollBar;
    TScrollBar *vScrollBar;
    short numCols;
    ccIndex topItem;
    ccIndex focused;
    ccIndex range;
    Boolean handleSpace;

    static uchar columnSeparator;
    static uchar ocolumnSeparator;

    // SET: see tlistvie.cc for more information
    unsigned getExtraOptions() { return extraOptions; }
    void setExtraOptions(unsigned ops) { extraOptions=ops; }

protected:
    // SET: extra options ored by default to all objects of this class.
    static unsigned extraOptions;
    // SET: neede to change the scroll bars too.
    void setNumCols(int aNumCols);

#if !defined( NO_STREAM )
private:

    virtual const char *streamableName() const
	{ return name; }

protected:

    TListViewer( StreamableInit );
    virtual void write( opstream& );
    virtual void *read( ipstream& );

public:

    static const char * const name;
    static TStreamable *build();
#endif // NO_STREAM
};


