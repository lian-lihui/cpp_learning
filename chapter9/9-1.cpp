#include <iostream>
#include <cstring>
#include "9-1.h"
using namespace std;

void
setgolf( golf & g, const char * name, int hc )
{
    strcpy( g.fullname, name );
    g.handicap = hc;
}

int
setgolf( golf & g )
{
    cout<< "Enter the name of the player:\n";
    cin>> g.fullname;
    cout<< "Enter the handicap of the player:\n";
    cin>> g.handicap;
    if (g.fullname )
        return 0;
    else
        return 1;
}

void
handicap( golf & g, int hc )
{
    g.handicap = hc;
}

void
showgolf( const golf & g )
{
    cout<< g.fullname<< " plays a socre of "<< g.handicap<< ".\n";   
}
