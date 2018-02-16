%{
#define Uses_TEvent
#include <tv.h>
%}

struct MouseEventType
{
 uchar buttons;
 Boolean doubleClick;
 TPoint where;
};

// This class is the base hardware interface with the mouse and shouldn't
// be used directly. You should use TMouse instead which is derived from
// it. That's why most members are protected.
// See thwmouse.cc
class THWMouse
{
protected:
 THWMouse();
 THWMouse(const THWMouse&) {};
 virtual ~THWMouse();

 static void show();
 static void hide();

 // Needed by some drivers to communicate the size of the screen.
 static void (*setRange)(ushort, ushort);
 static void getEvent(MouseEventType &me);
 // This function could fail according to the hardware.
 // In TV 2.0 it just doesn't exist when you compile for 32 bits.
// static void (*registerHandler)(unsigned, void (*)());

 static void suspend();
 static void resume();

 // Inline members:
 // Disable mouse
 static void inhibit();
 // Is mouse installed?
 static Boolean present();

 // SET: To override just part of the behavior:
 static void (*Show)();
 static void (*Hide)();
 static void (*Suspend)();
 static void (*Resume)();
 static void (*GetEvent)(MouseEventType &me);

 // SET: This is optional, is only needed if the harware uses forceEvent.
 static int  (*drawMouse)(int x, int y);

 // SET: Default behaviors
 static void defaultShow();
 static void defaultHide();
 static void defaultSetRange(ushort, ushort);
 static void defaultGetEvent(MouseEventType&);
 static void defaultRegisterHandler(unsigned, void (*)());
 static void defaultSuspend();
 static void defaultResume();
 static int  defaultDrawMouse(int x, int y);

public:
 // SET: Used to externally force a mouse event.
 // This is only used internally.
 static void forceEvent(int x, int y, int buttons);

protected:
 // This indicates how many buttons have the mouse. Is also used to determine
 // if the mouse is present, a value of 0 is mouse not available. See the
 // present() member.
 static uchar buttonCount;
 // SET: Suspend sets buttonCount to 0 to disable the mouse. The default
 // resume behavior is to restore this value.
 static uchar oldButtonCount;
 // SET: Just to avoid redundant calls
 static char  visible;
 // SET: Data used to force an event externally
 static MouseEventType forcedME;
 static char forced;
 static uchar btBeforeForce;

 // SET: Moved to the protected section
 static Boolean handlerInstalled;
 static Boolean noMouse;
 // The following counter is incremented when the mouse pointer is updated
 // by the driver. Only useful when done asynchronically.
 static volatile unsigned drawCounter;
};


// This class exposses the mouse interface.
class TMouse : public THWMouse
{
public:
 TMouse();
 ~TMouse();

 static void show();
 static void hide();

 static void suspend();
 static void resume();

 static void setRange( ushort, ushort );

 static void getEvent( MouseEventType& );
// static void registerHandler( unsigned, void (*)() );
 static Boolean present();

 static void resetDrawCounter();
 static unsigned getDrawCounter();
};

/****************************************************************************************/

struct CharScanType
{
 uchar charCode;        // The character encoded in the application code page
 uchar scanCode;
};

struct KeyDownEvent
{
 CharScanType charScan;
 ushort keyCode;        // Internal code, used for special keys (i.e. arrows)
 ushort shiftState;
 uchar  raw_scanCode;
 uint32 charCode;       // The Unicode16 of the key when the driver is in
                        // Unicode16 mode. 0xFFFF if no character is associated.
};

struct MessageEvent
{
    ushort command;
//    union
//        {
        void *infoPtr;
        long infoLong;
        ushort infoWord;
        short infoInt;
        uchar infoByte;
        char infoChar;
//        };
};

struct TEvent
{
    ushort what;
//    void getMouseEvent();
//    void getKeyEvent();
//    union
//    {
        MouseEventType mouse;
        KeyDownEvent keyDown;
        MessageEvent message;
//    };
};


