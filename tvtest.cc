#define Uses_MsgBox
#define Uses_TApplication
#include <tv.h>


class MyApp : public TApplication {
public:
  MyApp() : TProgInit( &initStatusLine,
		       &initMenuBar,
		       &initDeskTop )
  {
  };
  void run()
  {
    messageBox("hello", mfError | mfOKButton);
  };
};

int main(int argc, char* argv[]) {
  MyApp app;
  app.run();
  return 0;
}
