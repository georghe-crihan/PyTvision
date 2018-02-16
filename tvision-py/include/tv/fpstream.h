/*
 *      Turbo Vision - Version 2.0
 *
 *      Copyright (c) 1994 by Borland International
 *      All Rights Reserved.
 *

Modified by Robert H”hne to be used for RHIDE.
Modified to compile with gcc v3.x by Salvador E. Tropea, with the help of
Andris Pavenis and Christoph Bauer.

 *
 *
 */

/* ------------------------------------------------------------------------*/
/*                                                                         */
/*   class fpstream                                                        */
/*                                                                         */
/*   Base class for reading and writing streamable objects to              */
/*   bidirectional file streams                                            */
/*                                                                         */
/* ------------------------------------------------------------------------*/

#if defined( Uses_fpstream ) && !defined( __fpstream )
#define __fpstream

class fpstream : public fpbase, public iopstream
{
};

#endif  // Uses_fpstream

