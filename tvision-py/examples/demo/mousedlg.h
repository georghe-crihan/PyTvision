/*---------------------------------------------------------*/
/*                                                         */
/*   Mousedlg.h : Header file for mousedlg.cpp             */
/*                                                         */
/*---------------------------------------------------------*/
/*
 *      Turbo Vision - Version 2.0
 *
 *      Copyright (c) 1994 by Borland International
 *      All Rights Reserved.
 *
 */

class TClickTester : public TStaticText
{

public:

    TClickTester(TRect& r, char *aText);
    virtual TPalette& getPalette() const;
    virtual void handleEvent(TEvent& event);
    virtual void draw();

private:

    char clicked;

};


class TMouseDialog : public TDialog
{

public:

    TMouseDialog();
    virtual void handleEvent(TEvent& event);

private:

    TScrollBar *mouseScrollBar;
    short oldDelay;

};
