%module nscoll
%{
#define Uses_TNSCollection
#include <tv.h>
%}

class TNSCollection : public TObject
{

public:

    TNSCollection( ccIndex aLimit, ccIndex aDelta );
    ~TNSCollection();

    virtual void shutDown();

    void *at( ccIndex index )
    {
      if( index < 0 || index >= count )
          error(1,0);
      return items[index];
    }
    virtual ccIndex indexOf( void *item );

    void atFree( ccIndex index );
    void atRemove( ccIndex index );
    void remove( void *item );
    void removeAll();
    void free( void *item );
    void freeAll();

    virtual void atInsert( ccIndex index, void *item );
    void atPut( ccIndex index, void *item );
    void atReplace( ccIndex index, void *item ); // SET: Why not? ;-)
    virtual ccIndex insert( void *item );
%pythoncode
%{
def insert(self, p):
    p.thisown = 0
    return _tv.TNSCollection_insert(self, p)
%}

    virtual void error( ccIndex code, ccIndex info );

    void *firstThat( ccTestFunc Test, void *arg );
    void *lastThat( ccTestFunc Test, void *arg );
    void forEach( ccAppFunc action, void *arg );

    void pack();
    virtual void setLimit( ccIndex aLimit );

    ccIndex getCount()
        { return count; }

    // SET: I added it to create collections with static strings inserted
    // in it. I think that's a common case and strduping each insertion is
    // a real waste.
    void setOwnerShip(Boolean option) { shouldDelete=option; }
    // SET: That's quite natural. I did it slower than at() but also smaller
    // I added it after error became virtual which makes it really bloated.
//    void *operator[](ccIndex i);

protected:

    TNSCollection();

    void **items;
    ccIndex count;
    ccIndex limit;
    ccIndex delta;
    Boolean shouldDelete;

private:

    virtual void freeItem( void *item );

};

