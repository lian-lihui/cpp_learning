#include <iostream>

int
main()
{
    using namespace std;

    cout << "What letter grade do you deserve? ";
    char ch;
    cin >> ch;
    ch = ch + 1;
    cout << ch << endl;
    cout << ( int )ch << endl;

    return 0;
}
