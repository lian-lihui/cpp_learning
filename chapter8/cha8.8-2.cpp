#include <iostream>
#include <string>
struct CandyBar
{
     char name[40];
     double weight;
     int calories;
};

const CandyBar & refen( CandyBar & input, const char * na = "Millennium Munch", double wgt = 2.85, int cal = 350 );
void ShowStru( const CandyBar & input );
using namespace std;

int
main()
{
    CandyBar choco;
    refen( choco );
    ShowStru( choco );

    return 0;
}

int 
refen( CandyBar &input, const char * na, double wgt, int cal )
{
    if ( !na ) 
        return 1;

    snprintf( input.name, 40, "%s", na );
    input.weight = wgt;
    input.calories = cal;


    return 0;
}

void ShowStru( const CandyBar & input )
{
    cout<< "The name of this CandyBar is "<< input.name<< ", "
        << "weight is "<< input.weight<< ", "<< "calories is "
        << input.calories<< ". \n";
}
