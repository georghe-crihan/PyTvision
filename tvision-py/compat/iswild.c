#ifndef ISWILD_INCLUDED
#define ISWILD_INCLUDED
/*
 Copyright (C) 1996-1998 Robert H”hne
 Copyright (C) 2000      Salvador E. Tropea
 Covered by the GPL license.
*/

#include <string.h>

inline int CLY_IsWild(const char *f)
{
 return strpbrk(f,"?*")!=0;
}
#endif
