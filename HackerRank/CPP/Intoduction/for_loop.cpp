// C++ > Introduction > For Loop
//https://www.hackerrank.com/challenges/c-tutorial-for-loop/forum

#include <iostream>

using namespace std;

int main()
{
    string s[] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    int a, b, i;
    cin >> a;
    cin >> b;

    for (i = a; i <= b; i++)
    {
        if (i <= 9)
        {
            //cout << i;
            cout << s[i - 1] << "\n";
        }
        else if ((i > 9) && (i % 2 == 0))
        {
            cout << "even\n";
        }
        else if ((i > 9) && (i % 2 != 0))
        {
            cout << "odd\n";
        }
    }
    return 0;
}