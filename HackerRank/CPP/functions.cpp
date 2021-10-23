// Practise > C++ > Introduction > Functions
// https://www.hackerrank.com/challenges/c-tutorial-functions/problem
#include <iostream>
using namespace std;

int max_of_four(int a, int b, int c, int d)
{
    int max_num = max(a, max(b, max(c, d)));
    return max_num;
}

int main()
{
    int a, b, c, d;
    cin >> a;
    cin >> b;
    cin >> c;
    cin >> d;
    cout << max_of_four(a, b, c, d);

    return 0;
}