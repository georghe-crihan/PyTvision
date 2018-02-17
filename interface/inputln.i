/* ---------------------------------------------------------------------- */
/*      class TInputLine                                                  */
/*                                                                        */
/*      Palette layout                                                    */
/*        1 = Passive                                                     */
/*        2 = Active                                                      */
/*        3 = Selected                                                    */
/*        4 = Arrows                                                      */
/* ---------------------------------------------------------------------- */

%module inputln
%{
#define Uses_TInputLine
#define Uses_TInputLineBase
//#define Uses_TInput1Line
#include <tv.h>
%}

class TRect;
struct TEvent;
class TValidator;

class TInputLineBase : public TView
{
public:
 TInputLineBase(const TRect& bounds, int aMaxLen);
 ~TInputLineBase();

 virtual uint32 dataSize();
// virtual void getData(void *rec);
 virtual TPalette& getPalette() const;
 virtual void handleEvent(TEvent& event);
 void selectAll(Boolean enable);
 virtual void setState(ushort aState, Boolean enable);
 void SetValidator(TValidator *);
 virtual Boolean valid(ushort);
 virtual Boolean insertChar(unsigned val); // Added by SET
 virtual Boolean insertChar(TEvent &event)=0;
 virtual void    assignPos(int index, unsigned val)=0;
 virtual Boolean pasteFromOSClipboard()=0;
 virtual void    copyToOSClipboard()=0;
 virtual void    setDataFromStr(void *str)=0;
// const void *getData() { return data; };
 const char *getData();
 %rename(getTextData) getData();

 int curPos;
 int firstPos;
 int selStart;
 int selEnd;

 static char rightArrow;
 static char leftArrow;
 static char orightArrow;
 static char oleftArrow;

protected:
 virtual void resizeData() {}
 TValidator * validator;
 void deleteSelect();
 void makeVisible(); // Added by SET
 Boolean canScroll( int delta );

 // Inline helpers to make the code cleaner
 int insertModeOn();
 int lineIsFull();
 int posIsEnd();

 // IMHO exposing these two is a very bad idea, I added a couple of members to
 // work with them: setDataFromStr & getData. All TV code uses these new
 // members. If we don't hide them then we must compute the string length all
 // the time. SET.
 char *data;
 int maxLen;

 int cellSize;
 int dataLen;

private:
 int mouseDelta( TEvent& event );
 int mousePos( TEvent& event );

#if !defined( NO_STREAM )
 //virtual const char *streamableName() const
 //    { return name; }

protected:

// TInputLineBase(StreamableInit);
 virtual void write(opstream&);
 virtual void *read(ipstream&);
 virtual void writeData(opstream&)=0;
 virtual void *readData(ipstream&)=0;

public:

 //static const char * const name;
 //static TStreamable *build();
#endif // NO_STREAM
};



template <typename T, typename D>
class TInputLineBaseT: public TInputLineBase
{
public:
 TInputLineBaseT(const TRect& bounds, int aMaxLen);

 virtual void    setData(void *rec);
 virtual void    setDataFromStr(void *str);
 virtual void    assignPos(int index, unsigned val);
 virtual Boolean pasteFromOSClipboard();
 virtual void    copyToOSClipboard();
 virtual void    draw();

#if !defined( NO_STREAM )
protected:
 TInputLineBaseT(StreamableInit) : TInputLineBase(streamableInit) {}

 virtual void writeData(opstream&);
 virtual void *readData(ipstream&);
#endif // NO_STREAM
};

%template(TInputLineBaseChar) TInputLineBaseT<char,TDrawBuffer>;

class TInputLine : public TInputLineBaseT<char,TDrawBuffer>
{
public:
 TInputLine(const TRect& bounds, int aMaxLen);

 virtual Boolean insertChar(TEvent &event);

#if !defined( NO_STREAM )
 virtual const char *streamableName() const
     { return name; }

protected:
 TInputLine::TInputLine(StreamableInit) :
   TInputLineBaseT<char,TDrawBuffer>(streamableInit) {}

public:
 static const char * const name;
 static TStreamable *build();
#endif // NO_STREAM
};

%template(TInputLineBaseU16) TInputLineBaseT<uint16,TDrawBufferU16>;

class TInputLineU16 : public TInputLineBaseT<uint16,TDrawBufferU16>
{
public:
 TInputLineU16(const TRect& bounds, int aMaxLen);

 virtual Boolean insertChar(TEvent &event);

#if !defined( NO_STREAM )
 virtual const char *streamableName() const
     { return name; }

protected:
 TInputLineU16(StreamableInit) :
   TInputLineBaseT<uint16,TDrawBufferU16>(streamableInit) {}
 
public:
 static const char * const name;
 static TStreamable *build();
#endif // NO_STREAM
};


#if 0
// This is based on TVTools idea, but I think is better to implement it
// in this way and not like a macro.
class TInput1Line : public TInputLine
{
public:
 TInput1Line(int x, int y, int max);
};

class TInput1LineU16 : public TInputLineU16
{
public:
 TInput1LineU16(int x, int y, int max);
};
#endif


