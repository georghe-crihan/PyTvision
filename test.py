#!/usr/bin/env python
import sys
import tv
import _tv
from tv import *
#import inithelper
#from inithelper import TAppWrapper

sys.stderr = open("/tmp/tvtest.log", "w")


cmAbout = 990
cmOpenFile = 991
cmSayYou = 992
cmSayMe = 993

       

class MyDialog(TDialog):
    def __init__(self, bounds, title):
        TDialog.__init__(self, bounds, title)
        r = self.getExtent()
        r.grow(-2, -2)
        r = TRect(2, 5, 18, 7)
        self.options |= ofCentered;

        btn = TButton(r, "~T~est", cmOK, bfDefault)
        self.insert(btn)

        self.inl = inl = TInputLine(TRect(2, 7, 20, 8), 40)
        self.insert(inl)

        lb = TListBox(TRect(2, 10, 40, 14), 2, None)
        self.insert(lb)
        items = TStringCollection(10, 10)
        items.insert("hello")
        items.insert("hello2")
        lb.newList(items)

        stc = TStaticText(TRect(42, 2, 58, 3), "static text")
        self.insert(stc)

        items = TSItem("value 1", None) +\
                TSItem("value 2", None) +\
                TSItem("value 3", None)
                
        print >>sys.stderr, "items=", items
        rb = TRadioButtons(TRect(42, 5, 58, 8), items)
        self.insert(rb)

        items = TSItem("option 1", None) +\
                TSItem("option 2", None)
        cb = TCheckBoxes(TRect(42, 10, 58, 12), items)
        self.insert(cb)


    def getInput(self):
        return self.inl.getData()


    def handleEvent(self, event):
        try:
            if event.what == evCommand:
                print >>sys.stderr, "COMMAND", event.message.command
        finally:
            TDialog.handleEvent(self, event)


    def valid(self, command):
        print >>sys.stderr, "valid", command
        return TDialog.valid(self, command)
        #messageBox(self.getInput(), mfInformation|mfOKButton)



class MethodHolder(TMethodHolder):
    def initDeskTop(self, r):
        print >>sys.stderr, r.a.x, r.a.y, r.b.x, r.b.y
        r.a.y += 1
        r.b.y -= 1
        dt = TDeskTop(r)
        dt.thisown = 0
        return dt

    def initMenuBar(self, r):
        try:
            return self._initMenuBar(r)
        except:
            import traceback
            traceback.print_exc()

    def _initMenuBar(self, r):
        r.b.y = r.a.y + 1
        print >>sys.stderr, "mh.initMenuBar"
       
        menu = [
                ("~A~bout", cmAbout, kbAltA),
                ("~F~ile", kbAltF,
                 (("~O~pen", cmOpenFile, kbAltO, hcNoContext, "Alt-O"),
                  ),),                
                ("~H~ello", kbAltH,
                 (("~Y~ou", cmSayYou, kbAltY, hcNoContext, "Alt-X"),
                  ("~M~e", cmSayMe, kbAltM),
                  )),
                ]
        mm = cMakeMenu(menu)

        m = TMenu(mm)
        mb = TMenuBar(r, m)
        mb.thisown = 0
        return mb
#        return TMethodHolder.initMenuBar(self, r)

mh = MethodHolder()
cvar.TAppWrapper_methods = mh

class MyApp(TAppWrapper):
    def __init__(self):
        TAppWrapper.__init__(self, mh)

    def idle(self):
        trc = sys.gettotalrefcount()
        print >>sys.stderr, trc

    def run(self):
        dlg = MyDialog(TRect(0,0,60,16), "Test Dialog")
        dlg.flags |= wfGrow;
        cvar.TProgram_deskTop.execView(dlg)
        messageBox(dlg.getInput(), mfInformation|mfOKButton)
        self._input = dlg.getInput()
        #dlg = EditDialog(TRect(0,0,60,16), "Test Dialog")
        #cvar.TProgram_deskTop.execView(dlg)
        w = TWindow(TRect(0,0,60,16), "Editor", 0)

        editor = TEditor(TRect(1, 1, 40, 12), None, None, None, 4096)
        editor.insertText(self._input, len(self._input), 0)
        w.insert(editor)
        cvar.TProgram_deskTop.insert(w)

        messageBox("Bye", mfInformation|mfOKButton)

        TAppWrapper.run(self)

    def getInput(self):
        return self._input

    def handleEvent(self, event):
        if event.what == evCommand:
            print >>sys.stderr, "app.handleEvent command", event.message.command
            c = event.message.command
            if c == cmOpenFile:
                dlg = TFileDialog("*.py", "Open File", "", 0, 0)
                cvar.TProgram_deskTop.execView(dlg)
            elif c == cmSayYou:
                messageBox("YOU", mfInformation|mfOKButton)
            elif c == cmSayMe:
                messageBox("ME", mfInformation|mfOKButton)                


        TApplication.handleEvent(self, event)


#af = TAppFactory()
#app = af.makeApplication()
#app = TEditorApp()
app = MyApp()

app.run()
#print >>sys.stderr, app.getInput()

#inl = TInputLine(TRect(2, 7, 20, 8), 40)
#for n in xrange(1000):
#    v = inl.getData()
#    print sys.gettotalrefcount()


#assert(tv.cmQuit == 1)

