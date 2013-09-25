#include <iostream>
#include <cctype>
#include "10-5.h"

int
main()
{
    using namespace std;
    Stack st;
    char ch;
    customer cd;
    cout<< "Please enter A to add a customer data, \n"
        << "P to process a CD, or Q to quit.\n";
    while (cin>> ch && toupper( ch ) != 'Q')
    {
        while (cin.get() != '\n')
            continue;
        if (!isalpha( ch ))
        {
            cout<< '\a';
            continue;
        }
        switch( toupper( ch ) )
        {
            case 'A': cout<< "Enter the name of the customer: ";
                      cin.get( cd.fullname );
                      cout<< "Enter the payment of the costomer: ";
                      cin>> cd.payment;
                      if (st.isfull())
                          cout<< "stack already full\n";
                      else
                          st.push( cd );
                      break;
            case 'P': if (st.isempty())
                          cout<< "Stack already empty\n";
                      else
                      {
                          st.pull( cd );
                          cout<< "Customer "<< cd.fullname<< " popped\n";
                      }
                      break;
        }
        cout<< "Please enter A to add a customer data, \n"
            << "P to process a CD, or Q to quit.\n";
    }
    cout<< "Bye\n";

    return 0;
}
