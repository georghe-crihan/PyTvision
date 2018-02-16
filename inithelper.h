#ifndef  __TXAPPLICATION_H
#define __TXAPPLICATION_H

#define Uses_TApplication
#define Uses_TProgram
#include <tv.h>

class TMethodHolder {
 public:
  virtual TStatusLine *initStatusLine( TRect );
  virtual TMenuBar *initMenuBar( TRect );
  virtual TDeskTop *initDeskTop( TRect );
  virtual ~TMethodHolder() { };
};

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


#endif //  __TXAPPLICATION_H
