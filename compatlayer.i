/**[txh]********************************************************************

  Description:
  This header works as a distribution point. It parses the Uses_*
definitions and includes (or defines) the needed stuff.@p
  Important guidelines:@*

  Never include string.h use Use_string instead.
  strlwr and strupr are defined.@*
  stricmp and strnicmp are deprecated, use strcasecmp and strncasecmp
instead.@*
  Never use ios::bin (CLY_IOSBin).
  Never use filebuf::openprot (CLY_FBOpenProtDef).
  The O_TEXT and O_BINARY from fcntl needs Uses_fcntl.
  S_IS* from sys/stat needs Uses_sys_stat.
  Never use s/random, use s/rand which are ANSI/POSIX.
  Streambuf members: setbuf, seekoff and sync have wrappers requested with
Uses_PubStreamBuf.
  Request alloca with Uses_alloca.
  Never use movmem, use memmove instead (ANSI/POSIX).
  Even when supported the old calls to fexpand, isDir, pathValid,
validFileName, getCurDir, isWild, __file_exists, relativePath and driveValid
should be replaced by a CLY_* function.
  When possible POSIX compliant replacements are supplied for: glob, fnmatch
and regex.
  Added itoa for faster and safe integer to string conversion.

  Copyright (c) 2000-2003 by Salvador E. Tropea
  Covered by the GPL license.

***************************************************************************/

%module compatlayer
%{
#include <compatlayer.h>
%}

/* A global protection isn't suitable for all projects. Collisions should
   be solved individually.
#ifndef CLY_CompatLayerIncluded
#define CLY_CompatLayerIncluded
*/

#include <tv/configtv.h>

#ifdef Uses_fstream_simple
 #ifdef HAVE_SSC
  #define Uses_SSC_Streams 1
 #else
  #define Uses_fstream
 #endif
#endif

#ifdef Uses_iostream_simple
 #ifdef HAVE_SSC
  #define Uses_SSC_Streams 1
 #else
  #define Uses_iostream
 #endif
#endif

#ifdef Uses_SSC_Streams
 #define Uses_stdio
#endif

/* MSS memory leak debugger */
#ifdef MSS
 #include <mss.h>
#endif

#ifdef __cplusplus
 #define CLY_CFunc extern "C"
#else
 #define CLY_CFunc extern
#endif

#define TVComp_GCC

#if !defined(CLY_DoNotDefineSizedTypes) && !defined(CLY_SizedTypesDefined)
#define CLY_SizedTypesDefined 1
/* The following types should be platform independent */
typedef signed char int8;
typedef short       int16;
typedef int         int32;
typedef unsigned char  uint8;
typedef unsigned short uint16;
typedef unsigned int   uint32;
#if defined(TVComp_GCC)
typedef unsigned long long uint64;
typedef          long long int64;
#elif defined(TVComp_BCPP) || defined(TVComp_MSC)
typedef unsigned __int64 uint64;
typedef          __int64 int64;
#else
 #error Can not define uint64 type: unknown compiler.
#endif
#endif /* CLY_DoNotDefineSizedTypes */

#if defined(CLY_DefineUTypes) || defined(__cplusplus)
/* The following are just aliases and the size is platform dependant */
typedef unsigned char  uchar;
typedef unsigned short ushort;
typedef unsigned int   uint;
typedef unsigned long  ulong;
#endif /* CLY_DefineUTypes */


/*#endif // CLY_CompatLayerIncluded */

