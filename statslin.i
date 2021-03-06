/* ---------------------------------------------------------------------- */
/*      class TStatusLine                                                 */
/*                                                                        */
/*      Palette layout                                                    */
/*        1 = Normal text                                                 */
/*        2 = Disabled text                                               */
/*        3 = Shortcut text                                               */
/*        4 = Normal selection                                            */
/*        5 = Disabled selection                                          */
/*        6 = Shortcut selection                                          */
/* ---------------------------------------------------------------------- */

%module statslin
%{
#define Uses_TStatusLine
#include <tv.h>
%}

class TRect;
struct TEvent;
class TPoint;

class TStatusLine : public TView
{

public:

    TStatusLine( const TRect& bounds, TStatusDef& aDefs );
    ~TStatusLine();

    virtual void draw();
    virtual TPalette& getPalette() const;
    virtual void handleEvent( TEvent& event );
    virtual const char* hint( ushort aHelpCtx );
    void update();
    void computeLength(); // SET: see compactStatus
    virtual void changeBounds(const TRect& bounds);

//    static char hintSeparator[];
//    static char ohintSeparator[];

    // SET: Look the comments in TMenuView, same purpose
    int compactStatus;

protected:

    TStatusItem *items;
    TStatusDef *defs;

private:

    void drawSelect( TStatusItem *selected );
    void findItems();
    TStatusItem *itemMouseIsIn( TPoint );
    void disposeItems( TStatusItem *item );

#if !defined( NO_STREAM )
    virtual const char *streamableName() const
        { return name; }

    static void writeItems( opstream&, TStatusItem * );
    static void writeDefs( opstream&, TStatusDef * );
    static TStatusItem *readItems( ipstream& );
    static TStatusDef *readDefs( ipstream& );


protected:

    TStatusLine( StreamableInit );
    virtual void write( opstream& );
    virtual void *read( ipstream& );
 
public:

    static const char * const name;
    static TStreamable *build();
#endif // NO_STREAM
};


