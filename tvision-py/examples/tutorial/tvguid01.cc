/*---------------------------------------------------------*/
/*                                                         */
/*   Turbo Vision 1.0                                      */
/*   TVGUID01 Demo Source File                             */
/*   Copyright (c) 1991 by Borland International           */
/*                                                         */
/*---------------------------------------------------------*/

/*
  Taked from the Sergio Sigala <ssigala@globalnet.it> Turbo Vision port to
UNIX.
  LSM: TurboVision for UNIX
  ftp://sunsite.unc.edu /pub/Linux/devel/lang/c++/tvision-0.6.tar.gz
  Copying policy: BSD
  Adapted by Salvador Eduardo Tropea (SET) <set-soft@usa.net>.

  That's the minimal TVision application.
*/

#define Uses_TApplication
#include <tv.h>

// tv.h will pull in the headers needed for TApplication and its
// base classes. Add a #define Uses_Txxx statement (before the
// #include <tv.h> line) for each Turbo Vision class used in
// your program. Explicit or implied duplications are harmless:
// for example, #define Uses_TProgram would be redundant here,
// but harmless.

class TMyApp : public TApplication
{

public:
	TMyApp();

};

TMyApp::TMyApp() :
	TProgInit( &TMyApp::initStatusLine,
		       &TMyApp::initMenuBar,
		       &TMyApp::initDeskTop
		     )
{
}

int main()
{
	TMyApp myApp;
	myApp.run();
	return 0;
}
