/* ---------------------------------------------------------------------- */
/*      class TLabel                                                      */
/*                                                                        */
/*      Palette layout                                                    */
/*        1 = Normal text                                                 */
/*        2 = Selected text                                               */
/*        3 = Normal shortcut                                             */
/*        4 = Selected shortcut                                           */
/* ---------------------------------------------------------------------- */

%{
#define Uses_TLabel
#define Uses_T1Label
#include <tv.h>
%}


class TRect;
struct TEvent;
class TView;

class TLabel : public TStaticText
{

public:

    TLabel( const TRect& bounds, const char *aText, TView *aLink );
    TLabel( const TRect& bounds, const char *aText, TView *aLink, stTVIntl *aIntlText );

    virtual void draw();
    virtual TPalette& getPalette() const;
    virtual void handleEvent( TEvent& event );
    virtual void shutDown();

    TView *link;

protected:

    Boolean light;
    void init( TView *aLink );

#if !defined( NO_STREAM )
private:

    virtual const char *streamableName() const
        { return name; }

protected:

    TLabel( StreamableInit );
    virtual void write( opstream& );
    virtual void *read( ipstream& );

public:

    static const char * const name;
    static TStreamable *build();
#endif // NO_STREAM
};

class T1Label : public TLabel
{
public:
 T1Label(int x, int y, const char *aText, TView *aLink) :
   TLabel(TRect(x,y,x,y),aText,aLink)
   { growTo(cstrlen(TVIntl::getText(aText,intlText))+1,1); };
};


