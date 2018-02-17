%module(directors="1") inithelper
%{
#include "inithelper.h"
%}

%feature("director") TMethodHolder;

class TMethodHolder {
 public:
  virtual TStatusLine *initStatusLine( TRect );
  virtual TMenuBar *initMenuBar( TRect );
  virtual TDeskTop *initDeskTop( TRect );
  virtual ~TMethodHolder() { };
};

%feature("director") TAppWrapper;

class TAppWrapper : public TApplication
{
 public:
  static TStatusLine *_sInitStatusLine( TRect );
  static TMenuBar *_sInitMenuBar( TRect );
  static TDeskTop *_sInitDeskTop( TRect );
  static TMethodHolder *methods;
  TAppWrapper(TMethodHolder*);
  virtual ~TAppWrapper() { };

};


