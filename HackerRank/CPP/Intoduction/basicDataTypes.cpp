// C++ > Introduction > Basic Data Types
// https://www.hackerrank.com/challenges/c-tutorial-basic-data-types/problem

#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{

    int i;
    long l;
    char c;
    float f;
    double d;

    cin >> i >> l >> c >> f >> d;

    cout << i << "\n"
         << l << "\n"
         << c << "\n";
    cout << fixed << setprecision(3) << f << "\n";
    cout << fixed << setprecision(9) << d << "\n";

    return 0;
}