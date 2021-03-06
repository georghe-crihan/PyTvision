/* 
 * Mouse window routines header.
 *
 *  Copyright (c) 2002 by Jose Angel Sanchez Caso (JASC)
 *  Based in code by Salvador E. Tropea (SET)
 *  Covered by the GPL license. 
 */
 
#if defined(TVOS_Win32) && !defined(WINDOWSMOUSE_HEADER_INCLUDED)
#define WINDOWSMOUSE_HEADER_INCLUDED

struct THWMouseWinGr: virtual public TDisplayWinGr  // Access to display attributes
		    ,                THWMouse
{ THWMouseWinGr();
  static void Init();
  
  static void GetEvent( MouseEventType &me );

  static int testEvents( UINT   message
                       , WPARAM wParam
		       , LPARAM lParam );

  static void init();


protected:
 virtual ~THWMouseWinGr();

private:

// Support variables

/* static unsigned mouseX;
static unsigned mouseY; */

// Support methods

static int setMouse( LPARAM lParam
		   , int ev );


};

#endif // WINDOWSMOUSE_HEADER_INCLUDED

