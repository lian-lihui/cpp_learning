#include <iostream>
using namespace std;
void showtime( int, int );

int 
main()
{
    int hour;
    cout << "Enter the number of hours: "; 
    cin >> hour;
    int minute;
    cout << "Enter the number of minute: ";
    cin >> minute;
    showtime( hour, minute );

    return 0;
}

void showtime( int m, int n )
{
    cout << "Time: " << m << ":" << n << endl;
}
