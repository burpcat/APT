// C++ > Introduction > Arrays Introduction
// https://www.hackerrank.com/challenges/arrays-introduction/problem

#include <iostream>
using namespace std;

int main()
{

    int n;
    cin >> n;

    int main[n];
    for (int i = 0; i < n; i++)
    {
        cin >> main[i];
    }

    for (int i = n - 1; i >= 0; i--)
    {
        cout << main[i] << " ";
    }

    return 0;
}