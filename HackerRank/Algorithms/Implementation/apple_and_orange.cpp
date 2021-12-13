#include <iostream>
using namespace std;

int main(){

int i,apple_count=0,orange_count=0;

int sam_l,sam_u,tree_0,tree_1,apple_q,orange_q;


cin >> sam_l >> sam_u;
cin >> tree_0 >> tree_1;
cin >> apple_q >> orange_q;

int apple_array[apple_q],orange_array[orange_q];

for (i=0;i<apple_q;i++)
    {
    cin >> apple_array[i]; 

    if((apple_array[i]+tree_0 >= sam_l) && (apple_array[i]+tree_0 <= sam_u)){
        apple_count ++;
    }

    }

for (i=0;i<orange_q;i++)
    {
    cin >> orange_array[i]; 

    if((orange_array[i]+tree_1 >= sam_l) && (orange_array[i]+tree_1 <= sam_u)){
        orange_count ++;
    }

    }

cout << apple_count << "\n" << orange_count;
return 0;
}