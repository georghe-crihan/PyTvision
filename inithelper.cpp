#include "inithelper.h"

TMethodHolder* TAppWrapper::methods = NULL;

TStatusLine *TAppWrapper::_sInitStatusLine(TRect r)
{
  return methods->initStatusLine(r);
}

TMenuBar *TAppWrapper::_sInitMenuBar(TRect r)
{
  return methods->initMenuBar(r);
}

TDeskTop *TAppWrapper::_sInitDeskTop(TRect r)
{
  return methods->initDeskTop(r);
}

TStatusLine *TMethodHolder::initStatusLine(TRect r) {
  return TProgram::initStatusLine(r);
}

TMenuBar *TMethodHolder::initMenuBar(TRect r) {
  return TProgram::initMenuBar(r);
}

TDeskTop *TMethodHolder::initDeskTop(TRect r) {
  return TProgram::initDeskTop(r);
}



TAppWrapper::TAppWrapper(TMethodHolder *mh) :
  TProgInit(&TAppWrapper::_sInitStatusLine,
	    &TAppWrapper::_sInitMenuBar,
	    &TAppWrapper::_sInitDeskTop)
{
  methods = mh;
}


