// hexoct2.cpp -- display values in hex and octal

#include <iostream>

int
main()
{
    using namespace std;
    int chest = 42;
    int waist = 42;
    int inseam = 42;
        
    cout << "Monsieur cuts a striking figure!" << endl;
    cout << "chest = " << chest << "  (decimal)" << endl;
    cout << hex; 
    cout << "waist = " << waist << " hexadecimal" << endl;
    cout << oct;
    cout << "inseam = " << inseam << " (octal)" << endl;

    return 0;
}
