/*
 *      Turbo Vision - Version 2.0
 *
 *      Copyright (c) 1994 by Borland International
 *      All Rights Reserved.
 *

Modified by Robert H�hne to be used for RHIDE.

 *
 *
 */
// SET: Moved the standard headers here because according to DJ
// they can inconditionally declare symbols like NULL
#include <ctype.h>
#define Uses_string

#define Uses_THistory
#define Uses_TKeys
#define Uses_TRect
#define Uses_TEvent
#define Uses_TInputLine
#define Uses_THistoryWindow
#define Uses_opstream
#define Uses_ipstream
#define Uses_TPalette
#include <tv.h>

#define cpHistory "\x16\x17"

THistory::THistory( const TRect& bounds,
                    TInputLine *aLink,
                    ushort aHistoryId) :
    TView(bounds),
    link( aLink ),
    historyId( aHistoryId )
{
    options |= ofPostProcess;
    eventMask |= evBroadcast;
}

void THistory::shutDown()
{
    link = 0;
    TView::shutDown();
}

void THistory::draw()
{
    TDrawBuffer b;

    b.moveCStr( 0, icon, getColor(0x0102) );
    writeLine( 0, 0, size.x, size.y, b );
}

TPalette& THistory::getPalette() const
{
    static TPalette palette( cpHistory, sizeof( cpHistory )-1 );
    return palette;
}

void THistory::handleEvent( TEvent& event )
{
    THistoryWindow *historyWindow;
    TRect  r, p;
    ushort c;

    TView::handleEvent( event );
    if( event.what == evMouseDown ||
          ( event.what == evKeyDown &&
            ctrlToArrow( event.keyDown.keyCode ) ==  kbDown &&
            (link->state & sfFocused) != 0
          )
      )
        {
        link->select();
        historyAdd( historyId, (const char *)link->getData() );
        r = link->getBounds();
        r.a.x--;
        r.b.x++;
        r.b.y += 7;
        r.a.y--;
        p = owner->getExtent();
        r.intersect( p );
        r.b.y--;
        historyWindow = initHistoryWindow( r );
        if( historyWindow != 0 )
            {
            c = owner->execView( historyWindow );
            if( c == cmOK )
                {
                char rslt[256];
                historyWindow->getSelection( rslt );
                link->setDataFromStr( rslt );
                link->selectAll( True );
                link->drawView();
                }
            CLY_destroy( historyWindow );
            }
        clearEvent( event );
        }
    else
        if( event.what == evBroadcast )
            if( (event.message.command == cmReleasedFocus &&
                 event.message.infoPtr ==  link) ||
                event.message.command ==  cmRecordHistory
              )
                historyAdd( historyId, (const char *)link->getData() );
}

THistoryWindow *THistory::initHistoryWindow( const TRect& bounds )
{
    THistoryWindow *p = new THistoryWindow( bounds, historyId );
    p->helpCtx = link->helpCtx;
    return p;
}

#if !defined( NO_STREAM )
void THistory::write( opstream& os )
{
    TView::write( os );
    os << link << historyId;
}

void *THistory::read( ipstream& is )
{
    TView::read( is );
    is >> link >> historyId;
    return this;
}

TStreamable *THistory::build()
{
    return new THistory( streamableInit );
}

THistory::THistory( StreamableInit ) : TView( streamableInit )
{
}
#endif // NO_STREAM


