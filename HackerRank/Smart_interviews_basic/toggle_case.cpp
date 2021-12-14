// https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-toggle-case-of-characters
// Smart Interviews Basic > Toggle case of characters

#include <iostream>
using namespace std;

void some_function(string &basic_input,int N){
    char temp_var;
    for (int i=0;i<N;i++){
        if(basic_input[i] == tolower(basic_input[i])){
            temp_var = toupper(basic_input[i]);
            cout << temp_var;
            
            // Try to print uppercase characters from here
        }
        else{
            temp_var = tolower(basic_input[i]);
            cout << temp_var;
            // Try to print lowercase characters from here
        }
    }
}

int main(){

    string basic_input;
    int N;

    cin >> basic_input;
    N = basic_input.length();
    some_function(basic_input,N);


    
    return 0;
}