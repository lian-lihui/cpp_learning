#ifndef TEN_FIVE_H_
#define TEN_FIVE_H_

struct customer
{
    char fullname[35];
    double payment;
};

typedef customer Item;

class Stack
{
private:
    enum{ MAX = 10 };
    Item items[MAX];
    int top;
    double total;
public:
    Stack();
    bool isempty()const;
    bool isfull()const;
    bool push( const Item & item );
    bool pull( const Item & item );
};

#endif
