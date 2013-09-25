// static.cpp -- using a static local variable
#include <iostream>
#include <cstring>
#include <string>
using namespace std;

// function prototype
void strcount( const string str );

int
main()
{
    string input;

    cout<< "Enter a line: \n";
    getline( cin, input );
    while (strcmp( input, " " ))
    {
        strcount( input );
        cout<< "Enter next line (empty line to quit): \n";
        getline( cin, input );
    }
    cout<< "Bye\n";

    return 0;
}

void strcount( const string str )
{
    static int total = 0;
    int count = 0;

    cout<< "\""<< str<< "\" contains ";
    while (*str++)
        count++;
    total += count;
    cout<< count<< " characters\n";
    cout<< total<< " characters total\n";
}
