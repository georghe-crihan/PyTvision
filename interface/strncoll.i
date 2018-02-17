%{
#define Uses_TStringCollection
#include <tv.h>
%}

class TStringCollection : public TSortedCollection
{

public:

    TStringCollection( ccIndex aLimit, ccIndex aDelta );

private:

    virtual int compare( void *key1, void *key2 );
    virtual void freeItem( void *item );
#if !defined( NO_STREAM )
    virtual const char *streamableName() const
	{ return name; }
    virtual void *readItem( ipstream& );
    virtual void writeItem( void *, opstream& );

protected:

    TStringCollection( StreamableInit ) : TSortedCollection ( streamableInit ) {};

public:

    static const char * const name;
    static TStreamable *build();

    TStringCollection & operator = (const TStringCollection &);
#endif // NO_STREAM
};


