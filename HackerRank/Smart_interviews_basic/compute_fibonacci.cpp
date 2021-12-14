#include <iostream>

using namespace std;

int main(){

    int n,i,first=0,second=1,next=0;    // Since fibonacci starts with 0,1,2,3,5,8...
    cin >> n;

    for(i=1;i<n;i++){

    next = first+second;
    first = second;
    second = next;
    }

    cout << next; // Directly prints the nth fibonacci number instead of printing the entire series


    return 0;
}