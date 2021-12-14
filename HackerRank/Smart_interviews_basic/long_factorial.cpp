// https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-long-factorial/submissions/code/1339741061
// Smart Interviews Basic > Long factorial

#include<iostream>
using namespace std;

int main(){

    long int number=1;  // using long int since the constraints are large
    int n;

    cin >> n;

    for(int i=1;i<=n;i++){
        number = number * i;
    }    

    cout << number;
    return 0;
}