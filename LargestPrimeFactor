/*
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
*/

#include <iostream>
using namespace std;

long num = 600851475143;
/*
    Checks whether the number is prime or not.
    Input is a number.
    Returns a boolean value if the same.
*/
bool primeChecker(long prime);

/*
    Generates the next prime number needed.
    Input is a previous prime number
    Returns the next prime number.
*/
long primeGenerator(long prime);

int main()
{
    long temp = num;
    long limit = num / 2;
    long prime = 2;
    long max = 0;
    bool flag;   

    while(prime < limit)
    {
        if(temp % prime == 0)
        {
          //  cout << prime << endl;
            max = prime;
            temp /= prime;
            flag = primeChecker(temp);
            
            if(flag)
            {
                max = temp;  // Logic to shorten the steps.. Reverse Iteration
                break;
            }
        }

        else
            prime = primeGenerator(prime);
    }
    
    if(max == 0)
        cout << "The number itself is a prime" << endl;
    else
        cout << max << endl;
    
    return 0;
}

long primeGenerator(long prime)
{
  //  cout << prime << endl;
    prime++;
    bool flag = false;
    
    for(long i = prime; i < num / 2; i++ )
    {
        flag = primeChecker(i);
        if(flag)
        {
            return i;
        }   
    }
}

bool primeChecker(long prime)
{
    if (prime % 2 == 0)
        return false;
    
    for(int i = 3; i < prime / 2; i = i + 2)
    {        
        if(prime % i == 0)
            return false;
    }
    
    return true;
}
