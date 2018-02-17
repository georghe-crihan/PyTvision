%{
#define Uses_TFileDialog
#include <tv.h>
%}


enum {
    fdOKButton      = 0x0001,      // Put an OK button in the dialog
    fdOpenButton    = 0x0002,      // Put an Open button in the dialog
    fdReplaceButton = 0x0004,      // Put a Replace button in the dialog
    fdClearButton   = 0x0008,      // Put a Clear button in the dialog
    fdHelpButton    = 0x0010,      // Put a Help button in the dialog
    fdSelectButton  = 0x0020,      // Put a Select button in the dialog
    fdDoneButton    = 0x0040,      // Say Done isntead of "Cancel"
    fdAddButton     = 0x0080,      // Put an Add button in the dialog
    fdNoLoadDir     = 0x0100      // Do not load the current directory
				   // contents into the dialog at Init.
				   // This means you intend to change the
				   // WildCard by using SetData or store
				   // the dialog on a stream.
};

struct TEvent;
class TFileInputLine;
class TFileList;

class TFileDialog : public TDialog
{

public:

    TFileDialog( const char *aWildCard, const char *aTitle,
		 const char *inputName, ushort aOptions, uchar histId );
    ~TFileDialog();

    virtual void getData( void *rec );
    void getFileName( char *s );
    virtual void handleEvent( TEvent& event );
    virtual void setData( void *rec );
    virtual Boolean valid( ushort command );
    virtual void shutDown();
    virtual void sizeLimits(TPoint& min, TPoint& max);

    TFileInputLine *fileName;
    TFileList *fileList;
    char wildCard[PATH_MAX];
    const char *directory;

private:

    void readDirectory();
    Boolean checkDirectory( const char * );

protected:
    void setUpCurDir(); // SET

#if !defined( NO_STREAM )
    virtual const char *streamableName() const
	{ return name; }

protected:

    TFileDialog( StreamableInit ) :  TWindowInit( &TFileDialog::initFrame ), 
            TDialog ( streamableInit ) {}
    virtual void write( opstream& );
    virtual void *read( ipstream& );

public:

    static const char * const name;
    static TStreamable *build();
#endif // NO_STREAM
};


