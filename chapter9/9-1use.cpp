#include <iostream>
#include "9-1.h"

int
main()
{
    using namespace std;

    golf GOLF[4];
    char name[Len];
    int num;
    int i = 0;
    setgolf( GOLF[i] );
    cout<< "Enter the name of the player:\n";
    cin>> name;
    cout<< "Enter the score played:\n";
    cin>> num;
    i = 1;
    while (i < 4 && name != '\0')
    {
        setgolf( GOLF[i], name, num );
        ++i;
        if (i < 4)
        {
            cout<< "Enter the name of the player:\n";
            cin>> name;
            cout<< "Enter the score played:\n";
            cin>> num;
        }
    }
    for (int i = 0; i < 4; ++i)
        showgolf( GOLF[i] );

    return 0;
}
