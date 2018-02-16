/*
 *      Turbo Vision - Version 2.0
 *
 *      Copyright (c) 1994 by Borland International
 *      All Rights Reserved.
 *
 * Modified by Robert H”hne to be used for RHIDE.
 *
 * Modified by Jose Angel Sanchez Caso (JASC) to have machine endian and
 *  integer size compatibility.
 *
 * Added functions to rework the endian stuff by SET: readShort, readInt,
 * readLong, read8, read16, read32 and read64.
 *
 * Modified to compile with gcc v3.x by Salvador E. Tropea (SET), with
 * the help of Andris Pavenis and Christoph Bauer.
 *
 * ------------------------------------------------------------------------*
 *                                                                         *
 *   class ipstream                                                        *
 *                                                                         *
 *   Base class for reading streamable objects                             *
 *                                                                         *
 * ------------------------------------------------------------------------*/

#if defined( Uses_ipstream ) && !defined( __ipstream )
#define __ipstream

class TStreamableClass;
class TPReadObjects;

class ipstream : virtual public pstream
{
public:
    #ifndef TVComp_BCPP
    ipstream& operator >> (signed char    &ch ) { return (*this);}
    #endif
    ipstream& operator >> (char           &ch ) { return (*this);}
    ipstream& operator >> (unsigned char  &ch ) { return (*this);}
    ipstream& operator >> (signed short   &sh ) { return (*this);}
    ipstream& operator >> (unsigned short &sh ) { return (*this);}
    ipstream& operator >> (signed int     &i  ) { return (*this);}
    ipstream& operator >> (unsigned int   &i  ) { return (*this);}
    ipstream& operator >> (signed long    &l  ) { return (*this);}
    ipstream& operator >> (unsigned long  &l  ) { return (*this);}
    ipstream& operator >> (float          &f  ) { return (*this);}
    ipstream& operator >> (double         &d  ) { return (*this);}

    friend ipstream& operator >> ( ipstream&, TStreamable& );
    friend ipstream& operator >> ( ipstream&, void *& );
};

#endif  // Uses_ipstream

