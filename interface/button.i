/* ---------------------------------------------------------------------- */
/*      TButton object                                                    */
/*                                                                        */
/*      Palette layout                                                    */
/*        1 = Normal text                                                 */
/*        2 = Default text                                                */
/*        3 = Selected text                                               */
/*        4 = Disabled text                                               */
/*        5 = Normal shortcut                                             */
/*        6 = Default shortcut                                            */
/*        7 = Selected shortcut                                           */
/*        8 = Shadow                                                      */
/* ---------------------------------------------------------------------- */

%{
#define Uses_TButton
#include <tv.h>
%}

class TRect;
struct TEvent;
class TDrawBuffer;

// SET: callback function and return values
typedef int (*TButtonCallBack)(unsigned command, void *data);
const int btcbGoOn=0, btcbEndModal=1;

class TButton : public TView
{

public:

    TButton( const TRect& bounds,
             const char *aTitle,
             ushort aCommand,
             ushort aFlags
           );
    ~TButton();

    virtual void draw();
    void drawState( Boolean down );
    virtual TPalette& getPalette() const;
    virtual void handleEvent( TEvent& event );
    void makeDefault( Boolean enable );
    virtual void press();
    virtual void setState( ushort aState, Boolean enable );
    void setCallBack(TButtonCallBack cb) { callBack=cb; };
    const char *getText() { return TVIntl::getText(title,intlTitle); };

    const char *title;
    stTVIntl   *intlTitle;
//    static char shadows[];
//    static char markers[];
//    static char oshadows[];
//    static char omarkers[];

protected:

    ushort command;
    uchar flags;
    Boolean amDefault;
    TButtonCallBack callBack;

private:

    void drawTitle( TDrawBuffer&, int, int, ushort, Boolean );
    void pressButton( TEvent& );
    TRect getActiveRect();

#if !defined( NO_STREAM )
    virtual const char *streamableName() const
        { return name; }

protected:

    TButton( StreamableInit ): TView( streamableInit ) {};
    virtual void write( opstream& );
    virtual void *read( ipstream& );

public:

    static const char * const name;
    static TStreamable *build();
#endif // NO_STREAM
};

/*
// Note: you can't stream this class. Wait until I create relative code page
// TViews for international buttons.
class TButtonRef : public TButton
{
public:
    TButtonRef( const TRect& bounds,
                const char *aTitle,
                ushort aCommand,
                ushort aFlags
              );
    ~TButtonRef();
};

*/
