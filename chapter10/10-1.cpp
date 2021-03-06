#include <iostream>
#include <cstring>
using namespace std;

class Account
{
private:
    static const BUF_SIZE = 30; //In this way, if size of 'name' need to be increased later, increase BUF_SIZE is enoutgh;
                                // No need to find all '30' and change them all. 
    char name[ BUF_SIZE ];
    long account;
    double deposit;
    
public:
    Account();
    Account( const char * co, int n, double pr );
    ~Account();
    void save( double num );
    void withdraw( double num );
    void show()const;
};

Account::Account()
{
    strncpy( name, "no name", BUF_SIZE );
    account = 0;
    deposit = 0.0;
}

Account::Account( const char * co, int n, double pr )
{
    strncpy( name, co, BUF_SIZE );
    name[BUF_SIZE - 1] = '\0';

    if (n < 0)
        cout<< "The bank account number can't be negative.\n";
    else
        account = n;
    deposit = pr;
}

Account::~Account()
{
}

void Account::save( double num )
{
    if (num < 0)
    {
        cout<< "The deposit can't be negative.\n";
    }
    else
        deposit += num;
}

while ( withdraw( num ) ) {
    cin>> num;
}
int 
Account::withdraw( double num )
{
    if (num < 0) {
        std::cerr<< "Please enter an positive number.\n";
        return 1;
    }
    else if (num > deposit) {
        cerr<< "You can't withdraw more money than the account number.\n";
        return 1;
    }
    else {
        deposit -= num;
        return 0;
    }
}

void Account::show()const
{
    cout<< name<< "'s bank account number is "<< account
        << ", and the deposit is "<< deposit<< endl;
}


int
main()
{
    cout.precision( 2 );
    cout.setf( ios_base::fixed, ios_base::floatfield );
    cout.setf( ios_base::showpoint );

    cout<< "Using constructors to create new accounts\n";
    Account account1( "Nano Smart", 42359801, 10000.0 );
    account1.show();
    Account account2 = Account( "Boffo Objects", 13537568, 5000.0 );
    account2.show();

    cout<< "Enter the funds you want to save in account1:\n";
    double save;
    cin>> save;
    account1.save( save );
    cout<< "Enter the funds you want to withdraw in account2:\n";
    double withdraw;
    cin>> withdraw;
    account2.withdraw( withdraw );
    account1.show();
    account2.show();
   
    return 0;
}
