%typemap(in) void* {
    $1 = PyString_AsString($input);
}

%typemap(in) Boolean = bool;

//%typemap(in) void* insertObject {
//    PyObject *zero = PyInt_FromLong(0);
//    PyObject_SetAttrString($input,(char*)"thisown",zero);
//    Py_DECREF(zero);
//    $1 = PyString_AsString($input);
//}

%typemap(directorin) Boolean = bool;

%newobject obCopy;
%define DIRECTOR_VALUE_IN(Type)
%typemap(directorin) Type {
  Type *obCopy = new Type();
  *obCopy = $1_name;
  PyObject *o = SWIG_NewPointerObj((void*)obCopy, $descriptor(Type *), 1);
  if(o == NULL) {
     Py_DECREF(o);
     throw Swig::DirectorTypeMismatchException("Cannot build a copy");
  } else {
     $input = o;
  }
}

%enddef

DIRECTOR_VALUE_IN(TPoint);
DIRECTOR_VALUE_IN(TRect);


%define POINTER_IN_DISOWN(Type)
%typemap(in) Type* {
  if($input != Py_None)
    PyObject_SetAttrString($input, "thisown", PyInt_FromLong(0));
  if ((SWIG_ConvertPtr($input, (void **) &$1, $descriptor(Type *), SWIG_POINTER_EXCEPTION | 0 )) == -1) SWIG_fail;
}
%enddef

POINTER_IN_DISOWN(TSItem);
POINTER_IN_DISOWN(TMenu);
POINTER_IN_DISOWN(TSubMenu);
POINTER_IN_DISOWN(TScrollBar);



// a typemap hack to deallocate TEvent correctly
%typemap(directorin) TEvent& "
  // hello in $1 $input $1_name
  $input = SWIG_NewPointerObj(&$1_name, SWIGTYPE_p_TEvent, 0);
  PyObject *_tvref_event = $input;
"

%typemap(directorargout) TEvent& "Py_XDECREF(_tvref_event);"
