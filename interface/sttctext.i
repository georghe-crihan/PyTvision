/* ---------------------------------------------------------------------- */
/*      class TStaticText                                                 */
/*                                                                        */
/*      Palette layout                                                    */
/*        1 = Text                                                        */
/* ---------------------------------------------------------------------- */

%{
#define Uses_TStaticText
#define Uses_T1StaticText
#include <tv.h>
;
%}

class TRect;

class TStaticText : public TView
{

public:

    TStaticText( const TRect& bounds, const char *aText );
    TStaticText( const TRect& bounds, const char *aText, stTVIntl *aIntlText );
    ~TStaticText();

    virtual void draw();
    virtual TPalette& getPalette() const;
    virtual void getText( char *buf, int maxLen );
    const char *getText();

protected:

    const char *text;
    stTVIntl   *intlText;
    char        noIntl;
#if !defined( NO_STREAM )
private:

    virtual const char *streamableName() const
        { return name; }

protected:

    TStaticText( StreamableInit );
    virtual void write( opstream& );
    virtual void *read( ipstream& );

public:

    static const char * const name;
    static TStreamable *build();
#endif // NO_STREAM
};


class T1StaticText : public TStaticText
{
public:
 T1StaticText(int x, int y, const char *aText);

};


