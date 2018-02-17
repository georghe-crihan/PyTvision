/* ---------------------------------------------------------------------- */
/*      TCheckBoxes                                                       */
/*                                                                        */
/*      Palette layout                                                    */
/*        1 = Normal text                                                 */
/*        2 = Selected text                                               */
/*        3 = Normal shortcut                                             */
/*        4 = Selected shortcut                                           */
/* ---------------------------------------------------------------------- */

%{
#define Uses_TCheckBoxes
#include <tv.h>
%}

class TRect;
class TSItem;

class TCheckBoxes : public TCluster
{

public:

    TCheckBoxes( const TRect& bounds, TSItem *aStrings) :
      TCluster( bounds, aStrings ) {};

    virtual void draw();
    
    virtual Boolean mark( int item );
    virtual void press( int item );

//    static char button[];
//    static char obutton[];

private:

#if !defined( NO_STREAM )
    virtual const char *streamableName() const
        { return name; }

protected:

    TCheckBoxes( StreamableInit );

public:

    static const char * const name;
    static TStreamable *build();
#endif
};

// SET: That's a 32 bits version, the only difference is that it uses a
// 32 bits value for set/getData

class TCheckBoxes32 : public TCheckBoxes
{
public:
 TCheckBoxes32(const TRect& bounds,TSItem *aStrings) :
   TCheckBoxes(bounds,aStrings) {};
 virtual uint32 dataSize();
private:
#if !defined( NO_STREAM )
 virtual const char *streamableName() const { return name; }
protected:
 TCheckBoxes32(StreamableInit);
public:
 static const char * const name;
 static TStreamable *build();
#endif
};


