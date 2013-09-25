#include "10-5.h"
Stack::Stack()
{
    top = 0;
    total = 0.0;
}

bool Stack::isempty() const
{
    return top == 0;
}

bool Stack::isfull() const
{
    return top == MAX;
}

bool Stack::push( const Item & item )
{
    if (top < MAX)
    {
        items[top++] = item;
        return true;
    }
    else
        return false;
}

bool Stack::pull( const Item & item )
{
    if (top > 0)
    {
        total += items[top].payment;
        --top;
        return true;
    }
    else
        return false;
}
