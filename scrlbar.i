/* ---------------------------------------------------------------------- */
/*      class TScrollBar                                                  */
/*                                                                        */
/*      Palette layout                                                    */
/*        1 = Page areas                                                  */
/*        2 = Arrows                                                      */
/*        3 = Indicator                                                   */
/* ---------------------------------------------------------------------- */

%{
#define Uses_TScrollBar
#include <tv.h>
%}

class TRect;
struct TEvent;

typedef char TScrollChars[5];

class TScrollBar : public TView
{

public:

    TScrollBar( const TRect& bounds );

    virtual void draw();
    virtual TPalette& getPalette() const;
    virtual void handleEvent( TEvent& event );
    virtual void scrollDraw();
    virtual int scrollStep( int part );
    void setParams( int32 aValue, int32 aMin, int32 aMax,
                    int aPgStep, int aArStep );
    void setRange( int32 aMin, int32 aMax );
    void setStep( int aPgStep, int aArStep );
    void setValue( int32 aValue );

    void drawPos( int pos );
    int32 getPos();
    int getSize();

    int32 value;

    TScrollChars chars;
    int32 minVal;
    int32 maxVal;
    int pgStep;
    int arStep;

    static TScrollChars vChars;
    static TScrollChars hChars;
    static TScrollChars ovChars;
    static TScrollChars ohChars;

private:

    int getPartCode(void);

#if !defined( NO_STREAM )
    virtual const char *streamableName() const
     { return name; }

protected:

    TScrollBar( StreamableInit );
    virtual void write( opstream& );
    virtual void *read( ipstream& );

public:

    static const char * const name;
    static TStreamable *build();
#endif // NO_STREAM
};
