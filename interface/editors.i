/* ------------------------------------------------------------------------*/
/*                                                                         */
/*   EDITORS.H                                                             */
/*                                                                         */
/*   Copyright (c) Borland International 1991                              */
/*   All Rights Reserved.                                                  */
/*                                                                         */
/*   defines the classes TIndicator, TEditor, TMemo, TFileEditor,          */
/*   and TEditWindow                                                       */
/*                                                                         */
/* ------------------------------------------------------------------------*/

%{
#define Uses_TIndicator
#define Uses_TMemo
#define Uses_TEditor
#define Uses_TFileEditor
#define Uses_TEditWindow
#define Uses_TFindDialogRec
#define Uses_TReplaceDialogRec
#include <tv.h>
%}

enum {
  ufUpdate = 0x01,
  ufLine   = 0x02,
  ufView   = 0x04
};

enum {
  smExtend = 0x01,
  smDouble = 0x02
};

enum {
  sfSearchFailed = UINT_MAX
};

enum {
  cmSave        = 80,
  cmSaveAs      = 81,
  cmFind        = 82,
  cmReplace     = 83,
  cmSearchAgain = 84
};

enum {
  cmCharLeft    = 500,
  cmCharRight   = 501,
  cmWordLeft    = 502,
  cmWordRight   = 503,
  cmLineStart   = 504,
  cmLineEnd     = 505,
  cmLineUp      = 506,
  cmLineDown    = 507,
  cmPageUp      = 508,
  cmPageDown    = 509,
  cmTextStart   = 510,
  cmTextEnd     = 511,
  cmNewLine     = 512,
  cmBackSpace   = 513,
  cmDelChar     = 514,
  cmDelWord     = 515,
  cmDelStart    = 516,
  cmDelEnd      = 517,
  cmDelLine     = 518,
  cmInsMode     = 519,
  cmStartSelect = 520,
  cmHideSelect  = 521,
  cmIndentMode  = 522,
  cmUpdateTitle = 523,
  cmInsertText  = 524
};

enum {
  edOutOfMemory   = 0,
  edReadError     = 1,
  edWriteError    = 2,
  edCreateError   = 3,
  edSaveModify    = 4,
  edSaveUntitled  = 5,
  edSaveAs        = 6,
  edFind          = 7,
  edSearchFailed  = 8,
  edReplace       = 9,
  edReplacePrompt = 10
};

enum {
  efCaseSensitive   = 0x0001,
  efWholeWordsOnly  = 0x0002,
  efPromptOnReplace = 0x0004,
  efReplaceAll      = 0x0008,
  efDoReplace       = 0x0010,
  efBackupFiles     = 0x0100
};

const int
  maxLineLength = 256;

// SET: Added these old constants here
enum {
  cmOpen       = 100,
  cmNew        = 101,
  cmChangeDrct = 102,
  cmDosShell   = 103,
  cmCalculator = 104,
  cmShowClip   = 105,
  cmMacros     = 106
};

typedef ushort (*TEditorDialog)( int, ... );
ushort defEditorDialog( int dialog, ... );

class TIndicator : public TView
{

public:

    TIndicator( const TRect& );

    virtual void draw();
    virtual TPalette& getPalette() const;
    virtual void setState( ushort, Boolean );
    void setValue( const TPoint&, Boolean );

protected:

    TPoint location;
    Boolean modified;

#ifndef NO_STREAM

private:

//    static const char near dragFrame;
//    static const char near normalFrame;

    virtual const char *streamableName() const
        { return name; }

protected:

    TIndicator( StreamableInit );

public:

//    static const char * const near name;
    static TStreamable *build();

#endif
};



class TRect;
class TScrollBar;
class TIndicator;
class TEvent;

class TEditor : public TView
{

public:

    TEditor( const TRect&, TScrollBar *, TScrollBar *, TIndicator *, uint32 );
    virtual ~TEditor();

    virtual void shutDown();

    char bufChar( uint32 );
    uint32 bufPtr( uint32 );
    virtual void changeBounds( const TRect& );
    virtual void convertEvent( TEvent& );
    Boolean cursorVisible();
    void deleteSelect();
    virtual void doneBuffer();
    virtual void draw();
    virtual TPalette& getPalette() const;
    virtual void handleEvent( TEvent& );
    virtual void initBuffer();
    Boolean insertBuffer( char *, uint32, uint32, Boolean, Boolean );
    virtual Boolean insertFrom( TEditor * );
    Boolean insertText( const void *, uint32, Boolean );
    void scrollTo( int, int );
    Boolean search( const char *, ushort );
    virtual Boolean setBufSize( uint32 );
    void setCmdState( ushort, Boolean );
    void setSelect( uint32, uint32, Boolean);
    virtual void setState( ushort, Boolean );
    void trackCursor( Boolean );
    void undo();
    virtual void updateCommands();
    virtual Boolean valid( ushort );

    int charPos( uint32, uint32 );
    uint32 charPtr( uint32, int );
    Boolean clipCopy();
    void clipCut();
    void clipPaste();
    void deleteRange( uint32, uint32, Boolean );
    void doUpdate();
    void doSearchReplace();
    void drawLines( int, int, uint32 );
    virtual void formatLine(void *, uint32, int, ushort );
    void find();
    uint32 getMousePtr( TPoint );
    Boolean hasSelection();
    void hideSelect();
    Boolean isClipboard();
    uint32 lineEnd( uint32 );
    uint32 lineMove( uint32, int );
    uint32 lineStart( uint32 );
    void lock();
    void newLine();
    uint32 nextChar( uint32 );
    uint32 nextLine( uint32 );
    uint32 nextWord( uint32 );
    uint32 prevChar( uint32 );
    uint32 prevLine( uint32 );
    uint32 prevWord( uint32 );
    void replace();
    void setBufLen( uint32 );
    void setCurPtr( uint32, uchar );
    void startSelect();
    void toggleInsMode();
    void unlock();
    void update( uchar );
    void checkScrollBar( const TEvent&, TScrollBar *, int& );

    TScrollBar *hScrollBar;
    TScrollBar *vScrollBar;
    TIndicator *indicator;
    char *buffer;
    uint32 bufSize;
    uint32 bufLen;
    uint32 gapLen;
    uint32 selStart;
    uint32 selEnd;
    uint32 curPtr;
    TPoint curPos;
    TPoint delta;
    TPoint limit;
    int drawLine;
    uint32 drawPtr;
    uint32 delCount;
    uint32 insCount;
    Boolean isValid;
    Boolean canUndo;
    Boolean modified;
    Boolean selecting;
    Boolean overwrite;
    Boolean autoIndent;

    static TEditorDialog editorDialog;
    static ushort editorFlags;
    static char findStr[maxFindStrLen];
    static char replaceStr[maxReplaceStrLen];
    static TEditor * clipboard;
    static uint32 tabSize;
    uchar lockCount;
    uchar updateFlags;
    int keyState;

#ifndef NO_STREAM

private:

    virtual const char *streamableName() const
        { return name; }

protected:

    TEditor( StreamableInit );
    virtual void write( opstream& );
    virtual void *read( ipstream& );

public:

    static const char * const name;
    static TStreamable *build();

#endif
};

class TEvent;

struct TMemoData
{
    uint32 length;
    char buffer[65536];
};

class TMemo : public TEditor
{

public:

    TMemo( const TRect&, TScrollBar *, TScrollBar *, TIndicator *, uint32 );
    virtual void getData( void *rec );
    virtual void setData( void *rec );
    virtual uint32 dataSize();
    virtual TPalette& getPalette() const;
    virtual void handleEvent( TEvent& );

#ifndef NO_STREAM

private:

    virtual const char *streamableName() const
        { return name; }

protected:

    TMemo( StreamableInit );
    virtual void write( opstream& );
    virtual void *read( ipstream& );

public:

    static const char * const name;
    static TStreamable *build();

#endif  // NO_STREAM
};



//#include <dir.h>

class TRect;
class TScrollBar;
class TIndicator;
class TEvent;

class TFileEditor : public TEditor
{

public:

    char fileName[PATH_MAX];
    TFileEditor( const TRect&,
                 TScrollBar *,
                 TScrollBar *,
                 TIndicator *,
                 const char *
               );
    virtual void doneBuffer();
    virtual void handleEvent( TEvent& );
    virtual void initBuffer();
    Boolean loadFile();
    Boolean save();
    Boolean saveAs();
    Boolean saveFile();
    virtual Boolean setBufSize( uint32 );
    virtual void shutDown();
    virtual void updateCommands();
    virtual Boolean valid( ushort );

private:

    static const char * backupExt;

#ifndef NO_STREAM
    virtual const char *streamableName() const
        { return name; }

protected:

    TFileEditor( StreamableInit );
    virtual void write( opstream& );
    virtual void *read( ipstream& );

public:

    static const char * const name;
    static TStreamable *build();
#endif // NO_STREAM
};


class TFileEditor;

class TEditWindow : public TWindow
{

public:

    TEditWindow( const TRect&, const char *, int );
    virtual void close();
    virtual const char *getTitle( short );
    virtual void handleEvent( TEvent& );
    virtual void sizeLimits( TPoint& min, TPoint& max );

    TFileEditor *editor;

private:

    static const char * clipboardTitle;
    static const char * untitled;

#ifndef NO_STREAM
    virtual const char *streamableName() const
        { return name; }

protected:

    TEditWindow( StreamableInit );
    virtual void write( opstream& );
    virtual void *read( ipstream& );

public:

    static const char * const name;
    static TStreamable *build();
#endif // NO_STREAM
};


struct TFindDialogRec
{
    TFindDialogRec( const char *str, ushort flgs )
        {
        strcpy( find, str );
        options = flgs;
        }
    char find[maxFindStrLen];
    ushort options;
};


struct TReplaceDialogRec
{
    TReplaceDialogRec( const char *str, const char *rep, ushort flgs )
        {
        strcpy( find, str );
        strcpy( replace, rep );
        options = flgs;
        }
    char find[maxFindStrLen];
    char replace[maxReplaceStrLen];
    ushort options;
};

