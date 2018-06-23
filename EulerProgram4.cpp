/* 
 * File:   main.cpp
 * Author: Neeraj
 *
 * Created on April 10, 2018, 2:56 AM
 */

/*
 * A palindromic number reads the same both ways. 
 * The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
 * Find the largest palindrome made from the product of two 3-digit numbers.
 */

#include <cstdlib>
#include <iostream>
#include <string>
#include <bits/stdc++.h>
#include <sstream>

using namespace std;

bool findPalindrome(int number); // Finds if a number is Palindrome or not.
bool findFactors(int value); // Finds if the Palindrome is divisible 2 - 3 digit numbers.

int main() // Main Begin
{
    int largestPossibleNum = 999 * 999;
    bool flag = false;
    
    while (!flag && largestPossibleNum > 0)
    {        
        flag = findPalindrome(largestPossibleNum);
        largestPossibleNum--;
        
        if(flag)
            break;
    }    
    return 0;    
}

bool findPalindrome(int number)
{
    string revStr = to_string(number); // int to String Converstion
    string str = revStr;
    
    reverse(str.begin(), str.end()); // Reverse of the String
    
    if (str == revStr) // If its a Palindrome
    {
       // cout << str << endl;
        stringstream integer(str); // String to Int Conversion
        int val = 0;
        integer >> val;        
        return findFactors(val);       
    }
    else
        return false;      
}

bool findFactors(int value)
{    
    int factor[] = {1000, 1000};
    
    for(int i = 0; i < 2; i++)
    {
        while(factor[i] > 100)
        {
            int temp = factor[i];
            
            if(value % temp == 0 && factor[0] != factor[1])
                break;
            else
                factor[i]--;
        }
        if(factor[i] == 100)
            return false;
    }
    
    if(factor[0] * factor[1] != value)
        return false;
    
    cout << value << endl;
    
    return true;
}
