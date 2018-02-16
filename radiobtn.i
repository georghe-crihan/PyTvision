/* ---------------------------------------------------------------------- */
/*      class TRadioButtons                                               */
/*                                                                        */
/*      Palette layout                                                    */
/*        1 = Normal text                                                 */
/*        2 = Selected text                                               */
/*        3 = Normal shortcut                                             */
/*        4 = Selected shortcut                                           */
/* ---------------------------------------------------------------------- */


%{
#define Uses_TRadioButtons
#include <tv.h>
%}


class TRect;
class TSItem;

class TRadioButtons : public TCluster
{

public:

    TRadioButtons( const TRect& bounds, TSItem *aStrings );
/*
%pythoncode
%{
    def __init__(self, *args):
        _swig_setattr(self, TRadioButtons, 'this', _tv.new_TRadioButtons(*args))
        _swig_setattr(self, TRadioButtons, 'thisown', 1)
        args[2].thisown = 0
%}
*/
    virtual void draw();
    virtual Boolean mark( int item );
    virtual void movedTo( int item );
    virtual void press( int item );
    virtual void setData( void *rec );

//    static char button[];
//    static char obutton[];
    static char check;
    static char ocheck;

private:

#if !defined( NO_STREAM )
    virtual const char *streamableName() const
        { return name; }

protected:

    TRadioButtons( StreamableInit );

public:

    static const char * const name;
    static TStreamable *build();
#endif // NO_STREAM
};

class TRadioButtons32 : public TRadioButtons
{
public:
 TRadioButtons32(const TRect& bounds,TSItem *aStrings) :
   TRadioButtons(bounds,aStrings) {};
 virtual uint32 dataSize();
private:
#if !defined( NO_STREAM )
 virtual const char *streamableName() const { return name; }
protected:
 TRadioButtons32(StreamableInit);
public:
 static const char * const name;
 static TStreamable *build();
#endif // NO_STREAM
};


