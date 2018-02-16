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
/*   class opstream                                                        */
/*                                                                         */
/*   Base class for writing streamable objects                             */
/*                                                                         */
/* ------------------------------------------------------------------------*/

#if defined( Uses_opstream ) && !defined( __opstream )
#define __opstream

class TStreamableClass;
class TPWrittenObjects;

class opstream : virtual public pstream
{
public:
    opstream& operator << ( char           val ) { return *this; };
    #ifndef TVComp_BCPP
    opstream& operator << ( signed char    val ) { return *this; };
    #endif
    opstream& operator << ( unsigned char  val ) { return *this; };
    opstream& operator << ( signed short   val ) { return *this; };
    opstream& operator << ( unsigned short val ) { return *this; };
    opstream& operator << ( signed int     val ) { return *this; };
    opstream& operator << ( unsigned int   val ) {  return *this; };
    opstream& operator << ( signed long    val ) { return *this; };
    opstream& operator << ( unsigned long  val ) { return *this; };
    opstream& operator << ( float          val ) { return *this; };
    opstream& operator << ( double         val ) { return *this; };
    opstream& operator << ( long double    val ) { return *this; };

    friend opstream& operator << ( opstream&, TStreamable& );
    friend opstream& operator << ( opstream&, TStreamable * );

};

#endif  // Uses_opstream

