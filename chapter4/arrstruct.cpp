// arrstruct.cpp -- an array of structures

#include <iostream>
struct inflatable
{
    char name[20];
    float volume;
    double price;
};

int
main()
{
    using namespace std;

    inflatable guest[2] = 
    {
        {"Bambi", 0.5, 21.99},
        {"Godzilla", 2000, 565.99}
    };

    cout << "The guest " << guest[0].name << " and " << guest[1].name
        << "\nhave a combined volume of "
        << guest[0].volume + guest[1].volume << " cubic feet.\n";

    return 0;
}
