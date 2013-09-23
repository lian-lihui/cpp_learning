#include <iostream>
#include <cstring>
template <class T>
T max5( T arr[] , int n );
using namespace std;

template <> char * max5( char *arr[], int n );

int
main()
{
    int a = 6, b = 4, c = 5;
    int ar1[a];
    double ar2[b];
    char* ar3[c];
    for ( int i = 0; i < c; ++i ) {
        ar3[i] = new char[1024];
    }


    /*
    cout<< "Enter "<< a<< " integer numbers: \n";
    for (int i = 0; i < a; ++i)
    {
        cin>> ar1[i];
    }
    int max1 = max5( ar1, a );

    cout<< "Enter "<< b<< " float numbers: \n";
    for (int i = 0; i < b; ++i)
    {
        cin>> ar2[i];
    }
    double max2 = max5( ar2, b );
    */
    
    cout<< "Enter "<< c<< " strings: \n";
    for (int i = 0; i < c; ++i)
    {
        cin>> ar3[i];
    }
    char * max3 = max5( ar3, c );

    cout/*<< "max 1 = "<< max1<< ", max2 = "<< max2  */
        << ", max is "<< max3<< endl;

    for ( int i = 0; i < c; ++i ) {
        delete [] ar3[i];
        ar3[i] = 0;
    }



    return 0;
}

template <class T>
T 
max5( T arr[], int n )
{
    T temp;
    for (int i = 0; i < n; ++i)
        temp = (temp > arr[i]) ? temp : arr[i];
    return temp;

}

template <> 
char * 
max5( char *arr[], int n )
{
    int temp = 0, t = 0;
    for (int i = 0; i < n; ++i)
    {
        if(temp < strlen(arr[i]))
        {
            temp = strlen(arr[i]);
            t = i;
        }
    }

    return arr[t];
}
