// C++ > Introduction > Conditional Statements
// https://www.hackerrank.com/challenges/c-tutorial-conditional-if-else/problem

#include <iostream>
using namespace std;

int main()
{
    string s[] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

    int a;

    cin >> a;

    if (a <= 9)
    {
        cout << s[a - 1];
    }
    else if (a > 9)
    {
        cout << "Greater than 9";
    }

    return 0;
}