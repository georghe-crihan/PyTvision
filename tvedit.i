/*----------------------------------------------------------*/
/*                                                          */
/*   Turbo Vision 1.0                                       */
/*   Copyright (c) 1991 by Borland International            */
/*                                                          */
/*   Turbo Vision TVEDIT header file                        */
/*----------------------------------------------------------*/

%module tvedit
%{
#define Uses_TEditorApp
#include <tv.h>
%}

class TMenuBar;
class TStatusLine;
class TEditWindow;
class TDialog;

class TEditorApp : public TApplication
{

public:

    TEditorApp();

    virtual void handleEvent( TEvent& event );
    static TMenuBar *initMenuBar( TRect );
    static TStatusLine *initStatusLine( TRect );
    virtual void outOfMemory();

// private:

    virtual TEditWindow *openEditor( const char *fileName, Boolean visible );

protected:

    virtual void fileOpen();
    void fileNew();
    void changeDir();
    virtual void dosShell();
    void showClip();
    void tile();
    void cascade();
};

extern TEditWindow *clipWindow;

ushort execDialog( TDialog *d, void *data );
TDialog *createFindDialog();
TDialog *createReplaceDialog();
//ushort doEditDialog( int dialog, ... );
