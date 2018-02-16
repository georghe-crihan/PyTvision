%module applictn

%{
#define Uses_TApplication
#include <tv.h>
%}

%feature("director") TApplication;

class TApplication : public TProgram
{

public:

    TApplication() : TProgInit(), TProgram() { };
    virtual ~TApplication();

    virtual void suspend();
    virtual void resume();

};


