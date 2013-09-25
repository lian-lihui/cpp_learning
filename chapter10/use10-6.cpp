#include <iostream>
#include "10-6.h"

int
main()
{
    using namespace std;

    double num1, num2;
    Move move[2];
    cout<< "Enter two tes numbers: ";
    while(cin>> num1 && cin>> num2)
        move[0] = Move( 1, 2 );
    cout<< "Enter two test numbers: ";
    while (cin>> num1 && cin>> num2)
        move[1] = Move( 2, 3 );
    move[0].showmove();
    move[1].showmove();

    Move addition;
    addition = move[0].add( move[1] );
    move[1].reset( 2, 4 );

    addition.showmove();
    move[1].showmove();
    
    return 0;
}
