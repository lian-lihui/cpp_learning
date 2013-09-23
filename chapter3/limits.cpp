#include <iostream>
#include <climits>

int
main()
{
    using namespace std;

    int max_int = INT_MAX;
    short max_short = SHRT_MAX;
    long max_long = LONG_MAX;

    // sizeof operator yields size of type or variable
    cout << "int is " << sizeof (int) << " bytes." << endl;
    cout << "short is " << sizeof (max_short) << " bytes." << endl;
    cout << "long is " << sizeof (max_long) << " bytes." << endl << endl;
    
    cout << "Maximum valued:" << endl;
    cout << "int: " << max_int << endl;
    cout << "short: " << max_short << endl;
    cout << "long: " << max_long << endl;

    cout << "Mininum short value = " << SHRT_MIN << endl;
    cout << "Bits per byte = " << CHAR_BIT << endl;

    return 0;    
}
