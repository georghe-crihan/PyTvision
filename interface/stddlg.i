enum {

//  Commands

    cmFileOpen     = 1001,   // Returned from TFileDialog when Open pressed
    cmFileReplace  = 1002,   // Returned from TFileDialog when Replace pressed
    cmFileClear    = 1003,   // Returned from TFileDialog when Clear pressed
    cmFileInit     = 1004,   // Used by TFileDialog internally
    cmChangeDir    = 1005,   // Used by TChDirDialog internally
    cmRevert       = 1006,   // Used by TChDirDialog internally
    cmFileSelect   = 1007,   // Returned from TFileDialog when Select pressed
    cmDirSelection = 1008,   // New: Used by TChDirDialog internally and
                             // TDirListBox externally

//  Messages

    cmFileFocused = 102,    // A new file was focused in the TFileList
    cmFileDoubleClicked     // A file was selected in the TFileList
            = 103
};
