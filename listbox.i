%module listbox
%{
#define Uses_TListBox )
#include <tv.h>
%}


class TRect;
class TScrollBar;
class TCollection;

struct TListBoxRec
{
    TCollection *items;
    ccIndex selection;
};

class TListBox : public TListViewer
{

public:

    TListBox( const TRect& bounds, ushort aNumCols, TScrollBar *aScrollBar );
    TListBox( const TRect& bounds, ushort aNumCols, TScrollBar *aHScrollBar,
              TScrollBar *aVScrollBar );
    ~TListBox();

    virtual uint32 dataSize();
    virtual void getData( void *rec );
    virtual void getText( char *dest, ccIndex item, short maxLen );
    virtual void newList( TCollection *aList );
%pythoncode
%{
def newList(self, p):
    p.thisown = 0
    return _tv.TListBox_newList(self, p)
%}
    virtual void setData( void *rec );
    // SET: You not always want to destroy the items.
//    virtual void newList( TCollection *aList, Boolean destroyItems );
//    virtual void setData( void *rec, Boolean destroyItems );

    TCollection *list();

protected:
    TCollection *items;

private:

#if !defined( NO_STREAM )
    virtual const char *streamableName() const
	{ return name; }

protected:

    TListBox( StreamableInit );
    virtual void write( opstream& );
    virtual void *read( ipstream& );

public:

    static const char * const name;
    static TStreamable *build();
#endif // NO_STREAM
};


