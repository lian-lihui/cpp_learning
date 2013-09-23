#include <iostream>

int
main()
{
    using namespace std;

    for (int i = 0; i < 5; ++i)
        cout<< i<< " in "<< &i<< endl;

    return 0;
}
