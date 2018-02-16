#include <tv/configtv.h>

#ifdef TVCompf_djgpp
#include <dpmi.h>
#include <unistd.h>

void CLY_YieldProcessor(int micros)
{
 __dpmi_yield();
 if (micros>0)
    usleep(micros);
}
#endif

#ifdef TVOS_UNIX
#include <unistd.h>
 // See if this system have the POSIX function
 #if 0 //def _POSIX_PRIORITY_SCHEDULING
 #include <sched.h>

 void CLY_YieldProcessor(int micros)
 {
  sched_yield();
  if (micros>0)
     usleep(micros);
 }
 #else
 // No POSIX, just sleep
 void CLY_YieldProcessor(int micros)
 {
  if (micros<0)
     micros=10;
  usleep(micros);
 }
 #endif
#endif

#ifdef TVComp_BCPP //TVOSf_NT
void CLY_YieldProcessor(int micros)
{
 extern void __tvWin32Yield(int micros);
 if (micros<0)
    micros=27472; // 1000000 / (18.2 * 2)
 __tvWin32Yield(micros);
}
#endif

#if defined(TVOS_Win32) && !defined(TVComp_BCPP) //!defined(TVOSf_NT)
#define WIN32_LEAN_AND_MEAN
#include <windows.h>

void CLY_YieldProcessor(int micros)
{
 Sleep(micros/1000);
}
#endif
