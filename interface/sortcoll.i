%{
#define Uses_TSortedCollection
#include <tv.h>
%}

class TSortedCollection : public TNSSortedCollection, public TCollection
{

public:

    TSortedCollection( ccIndex aLimit, ccIndex aDelta) :
        TCollection( aLimit, aDelta ) {}

private:

    virtual int compare( void *key1, void *key2 ) = 0;
#if !defined( NO_STREAM )
    virtual const char *streamableName() const
        { return name; }
    virtual void *readItem( ipstream& ) = 0;
    virtual void writeItem( void *, opstream& ) = 0;

protected:

    TSortedCollection( StreamableInit );
    virtual void *read( ipstream& );
    virtual void write( opstream& );

public:

    static const char * const name;
#endif // NO_STREAM
};

