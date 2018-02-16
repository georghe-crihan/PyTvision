/*************************************************************************/
/*                                                                       */
/* SCOMBOWN.CPP                                                          */
/*                                                                       */
/* Copyright (c) 1992, Vincent J. Dentice                                */
/* All rights reserved                                                   */
/*                                                                       */
/* This file contains the stream registration object for the class       */
/* TComboWindow.                                                         */
/*                                                                       */
/*                                                                       */
/*   Date    Prg  Ver  Description                                       */
/* --------  ---  ---  ------------------------------------------------- */
/* 11/16/92  VJD  0.2  Added streamability to the TComboBox class.       */
/*                                                                       */
/*************************************************************************/


#define Uses_TComboWindow
#define Uses_TStreamableClass
#include "tcombobx.h"
__link( RWindow )


TStreamableClass RComboWindow( TComboWindow::name,
			       TComboWindow::build,
			       __DELTA(TComboWindow)
			     );
