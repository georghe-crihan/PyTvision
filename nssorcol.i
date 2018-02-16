%{
#define Uses_TNSSortedCollection
#include <tv.h>
%}


class TNSSortedCollection: public virtual TNSCollection
{

public:

    TNSSortedCollection( ccIndex aLimit, ccIndex aDelta) :
        TNSCollection( aLimit, aDelta ), duplicates(False)
            { delta = aDelta; setLimit( aLimit ); }

    virtual Boolean search( void *key, ccIndex& index );

    virtual ccIndex indexOf( void *item );
    virtual ccIndex insert( void *item );

    Boolean duplicates;
    virtual void *keyOf( void *item );

protected:

    TNSSortedCollection() : duplicates(False) {}

private:

    virtual int compare( void *key1, void *key2 ) = 0;

};

