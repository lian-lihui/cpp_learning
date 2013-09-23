// strgfun.cpp -- functions with a string argument

#include <iostream>
int c_in_str( const char * str, char ch );

int
main()
{
    using namespace std;
    char mmm[15] = "minimum";
    char * wail = "ululate";  // deprecated conversion

    int ms = c_in_str( mmm, 'm' );
    int us = c_in_str( wail, 'u' );
    
    cout<< ms<< " m characters in "<< mmm<< endl;
    cout<< us<< " u characters in "<< wail<< endl;

    return 0;
}


// this function counts the number of ch characters
// in the string str
int c_in_str( const char * str, char ch )
{
    int count = 0;

    while (*str)
    {
        if (*str == ch)
            ++count;
        ++str;
    }

    return count;
}

