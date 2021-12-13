//https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-check-bit/submissions/code/1339706007
// Smart Interview Basic > Check Bit


#include <iostream>
using namespace std;
int main(){

    int n,i;

    cin >> n >> i;

    if (n & (i<<(i))){
        cout << "true";
    }
    else{
        cout << "false";
    }

    
    return 0;
}