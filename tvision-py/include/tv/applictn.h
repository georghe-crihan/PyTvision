/*
 *      Turbo Vision - Version 2.0
 *
 *      Copyright (c) 1994 by Borland International
 *      All Rights Reserved.
 *

Modified by Robert H�hne to be used for RHIDE.

 *
 *
 */

#if defined( Uses_TApplication ) && !defined( __TApplication )
#define __TApplication

class TApplication : public TProgram
{

//protected:
public:

    TApplication();
    virtual ~TApplication();

    virtual void suspend();
    virtual void resume();

};

#endif

