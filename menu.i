%{
#define Uses_TMenu
#include <tv.h>
%}

class TMenuItem;

%{
#include <stdio.h>
%}

/*
%typemap(in) TMenuItem& itemList {   // from sequence to a list of TMenuItems
  TMenuItem* cur = NULL;
  TMenuItem* last = NULL;
  TMenuItem* first = NULL;
//  fprintf(stderr, "typemap TMenu length %d\n", PyObject_Length($input));
  if (PySequence_Check($input)) {
    for(int i=0; i < PyObject_Length($input); ++i) {
        char *aName;
        ushort aCommand;
        ushort aKeyCode;
        ushort aHelpCtx = hcNoContext;
        if (!PyArg_ParseTuple($input, "shh|h", &aName, &aCommand,
                              &aKeyCode, &aHelpCtx )) {
            for(cur = first; cur; cur = cur->next) delete cur;
            PyErr_SetString(PyExc_TypeError,"tuple must have 4 elements");
            return NULL;
        }
        last = cur;
        cur = new TMenuItem(aName, aCommand, aKeyCode, aHelpCtx);
//        fprintf(stderr, "typemap TMenuItem %s\n", aName);
        if(last) last->next = cur;
        if(!first) first = cur;
    }
    $1 = first;
  } else {
    PyErr_SetString(PyExc_TypeError,"expected a tuple.");
    return NULL;
  }
}
*/





%inline %{

#define Uses_TViews
#define Uses_TKeys
#include <tv.h>


TSubMenu& makeMenu__(PyObject *args)
{
    return (
        *new TSubMenu( "~F~ile", kbAltF )+
            *new TMenuItem( "~O~pen", cmHelp, kbF3, hcNoContext, "F3" )+
            *new TMenuItem( "~N~ew",  cmHelp,   kbF4, hcNoContext, "F4" )+
            newLine()+
            *new TMenuItem( "E~x~it", cmQuit, cmQuit, hcNoContext, "Alt-X" )+
        *new TSubMenu( "~W~indow", kbAltW )+
            *new TMenuItem( "~N~ext", cmNext,     kbF6, hcNoContext, "F6" )+
            *new TMenuItem( "~Z~oom", cmZoom,     kbF5, hcNoContext, "F5" )+
            *new TMenuItem( "~D~ialog", cmHelp, kbF2, hcNoContext, "F2" )
            // new dialog menu added here
        );
};


TMenuItem* cMakeMenu(PyObject *args)
{
  TMenuItem* cur = NULL;
  TMenuItem* first = NULL;
//  fprintf(stderr, "cMakeMenu TMenu length %d\n", PyObject_Length(args));
  if (PySequence_Check(args)) {
    for(int i=0; i < PyObject_Length(args); ++i) {
        char *aName;
        ushort aCommand;
        ushort aKeyCode;
        ushort aHelpCtx = hcNoContext;
        char *p = NULL;
        PyObject *o = PySequence_GetItem(args, i);
        Py_DECREF(o);
        PyObject *submenu_o;
        if (PyArg_ParseTuple(o,
                             "shh|hs", &aName, &aCommand,
                             &aKeyCode, &aHelpCtx, &p )) {
            cur = new TMenuItem(aName, aCommand, aKeyCode, aHelpCtx, p);
            if(first) {
                *first += *cur;
            } else {
                first = cur;
            }
        } else if (PyErr_Clear(), PyArg_ParseTuple(o,
                   "shO|h", &aName, &aKeyCode, &submenu_o, &aHelpCtx )) {
            TMenuItem *subitem = cMakeMenu(submenu_o);
            if(!subitem) {
//              for(cur = first; cur; cur = cur->next) delete cur;
//                fprintf(stderr, "subitem make failed.\n");
                return NULL;
            }
            TSubMenu *submenu = new TSubMenu(aName, aKeyCode, aHelpCtx);
            *submenu += *subitem;
            *first += *submenu;
        } else {
	  PyErr_Clear();
//            for(cur = first; cur; cur = cur->next) delete cur;
//	    fprintf(stderr, "tuple parse error\n");
            PyErr_SetString(PyExc_TypeError,"tuple parse error");
            return NULL;
        }	

//        fprintf(stderr, "make TMenuItem %s\n", aName);
    }
//    fprintf(stderr, "cMakeMenu return\n");
    return first;
  } else {
//    fprintf(stderr, "expected a tuple.\n");
    PyErr_SetString(PyExc_TypeError,"expected a tuple.");
    return NULL;
  }
}
%}


class TMenu
{

public:
    TMenu() : items(0), deflt(0) {};
    TMenu( TMenuItem& itemList )
        { items = &itemList; deflt = &itemList; }
    TMenu( TMenuItem& itemList, TMenuItem& TheDefault )
        { items = &itemList; deflt = &TheDefault; }
    ~TMenu();

    TMenuItem *items;
    TMenuItem *deflt;

};

