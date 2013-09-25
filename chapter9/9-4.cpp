#include <iostream>
#include "9-4.h"

void setSales( Sales & s, const double ar[], int n )
{
    double temp = ar[0];
    for (int i = 1; i < n; ++i)
    {
        temp = (temp < ar[i]) ? temp : ar[i];
    }
}
