%module collectn
%{
#define Uses_TCollection
#include <tv.h>
%}

class TCollection : public virtual TNSCollection
#if !defined( NO_STREAM )
                                                 , public TStreamable
#endif // NO_STREAM
{

public:

    TCollection( ccIndex aLimit, ccIndex aDelta );

#if !defined( NO_STREAM )
private:

    virtual const char *streamableName() const
        { return name; }

    virtual void *readItem( ipstream& ) = 0;
    virtual void writeItem( void *, opstream& ) = 0;


protected:

    TCollection( StreamableInit );
    virtual void *read( ipstream& );
    virtual void write( opstream& );

public:

    static const char * const name;
#endif // NO_STREAM
};

