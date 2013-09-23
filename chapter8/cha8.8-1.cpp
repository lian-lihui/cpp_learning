#include <iostream>
void ptstr( char * str );
void ptstr( char * str, int n );
using namespace std;

int
main()
{
    char * string;
    cout<< "Enter string: \n";
    cin>> string;
    ptstr( string );
    ptstr( string, 1 );
}

void ptstr( char * str )
{
    cout<< str<< endl;
}

void ptstr( char * str, int n )
{
    cout<< str<< endl;
} 
