// C++ > Introduction > Pointer
// https://www.hackerrank.com/challenges/c-tutorial-pointer/problem

#include <iostream>
using namespace std;

void update(int *a, int *b)
{
    int sum = *a + *b;
    int absDifference = (*a - *b > 0 ? *a - *b : -(*a - *b));
    *a = sum;
    *b = absDifference;
}

int main()
{

    int a, b;
    cin >> a;
    cin >> b;
    int *pa = &a, *pb = &b;
    update(pa, pb);
    cout << a << "\n"
         << b;

    return 0;
}