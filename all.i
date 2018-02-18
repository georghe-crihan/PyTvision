%module(directors="1") tv

%include exception.i

%include interface/tvcommon.i

%include interface/compatlayer.i
%include interface/ttypes.i
%include interface/system.i
%include interface/object.i
%include interface/event.i
%include interface/streambl.i

%include interface/nscoll.i
%include interface/nssorcol.i
%include interface/collectn.i
%include interface/sortcoll.i
%include interface/strncoll.i

%include interface/point.i
%include interface/rect.i
%include interface/palette.i
%include interface/cmdset.i
%include interface/view.i
%include interface/group.i
%include interface/window.i
%include interface/scrlbar.i
%include interface/scroller.i

%include interface/button.i
%include interface/inputln.i
%include interface/sttctext.i
%include interface/label.i
%include interface/sitem.i
%include interface/cluster.i
%include interface/radiobtn.i
%include interface/checkbox.i

%include interface/views.i

%include interface/menuitem.i
%include interface/submenu.i
%include interface/menu.i
%include interface/menuview.i
%include interface/menubox.i
%include interface/menubar.i

//%include interface/screen.i
%include interface/statsitm.i
%include interface/statsdef.i
%include interface/statslin.i
%include interface/desktop.i

%include interface/program.i
%include interface/applictn.i

%include interface/tkeys.i

%include interface/dialog.i
%include interface/filedlg.i
%include interface/tvedit.i
%include interface/dialogs.i
%include interface/msgbox.i
%include interface/lstviewr.i
%include interface/listbox.i
%include interface/editors.i
%include interface/stddlg.i

%include interface/inithelper.i
