%module cmdset
%{
#define Uses_TCommandSet
#include <tv.h>
%}

class TCommandSet
{

public:

    TCommandSet();
    %ignore TCommandSet( const TCommandSet& );
    TCommandSet( const TCommandSet& );
    ~TCommandSet();

    Boolean has( int cmd );

    %rename(disableCmdInt) disableCmd( int cmd );
    void disableCmd( int cmd );
    %rename(disableCmdRange) disableCmd( int cmdStart, int cmdEnd );
    void disableCmd( int cmdStart, int cmdEnd ); // SET: Added
    %rename(enableCmdInt) enableCmd( int cmd );
    void enableCmd( int cmd );
    %rename(enableCmdRange) enableCmd( int cmdStart, int cmdEnd );
    void enableCmd( int cmdStart, int cmdEnd ); // SET: Added
    void enableAllCommands();
    %ignore operator += ( int cmd );
    void operator += ( int cmd );
    %ignore operator -= ( int cmd );
    void operator -= ( int cmd );

    void disableCmd( const TCommandSet& );
    void enableCmd( const TCommandSet& );
    void operator += ( const TCommandSet& );
    void operator -= ( const TCommandSet& );

    Boolean isEmpty();

    %rename(set) operator = (const TCommandSet& );
    TCommandSet& operator = (const TCommandSet& );

    TCommandSet& operator &= ( const TCommandSet& );
    TCommandSet& operator |= ( const TCommandSet& );

/*
    friend TCommandSet operator & ( const TCommandSet&, const TCommandSet& );
    friend TCommandSet operator | ( const TCommandSet&, const TCommandSet& );

    friend int operator == ( const TCommandSet& tc1, const TCommandSet& tc2 );
    friend int operator != ( const TCommandSet& tc1, const TCommandSet& tc2 );
*/

private:
    uint32 *cmds;

};

