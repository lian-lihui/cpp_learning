#include <iostream>
const int ArSize = 5;
template <class T>
T max5( T arr[ArSize] );
using namespace std;

int
main()
{
    int ar1[5];
    double ar2[5];
    cout<< "Enter 5 integer numbers: \n";
    for (int i = 0; i < ArSize; ++i)
    {
        cin>> ar1[i];
    }
    int max1 = max5( ar1 );
    cout<< "Enter 5 float numbers: \n";
    for (int i = 0; i < ArSize; ++i)
    {
        cin>> ar2[i];
    }
    double max2 = max5( ar2 );
    cout<< "max 1 = "<< max1<< ", max2 = "<< max2<< endl;

    return 0;
}

template <class T>
T max5( T arr[ArSize] )
{
    T temp;
    for (int i = 0; i < ArSize; ++i)
    {
        temp = (temp > arr[i]) ? temp : arr[i];
    }
    return temp;

}
