// https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-count-vowels-and-consonants/problem
// SmartInterviewsBasic > Count Vowels & Consonants



#include <iostream>
using namespace std;

void Traverse_string(string &basic_input,int N){
    int vowel_count=0,cons_count=0;
    for (int i=0;i<N;i++){
        if (tolower(basic_input[i])== 'a' ||tolower(basic_input[i])== 'e' ||tolower(basic_input[i])== 'i' ||tolower(basic_input[i])== 'o' ||tolower(basic_input[i])== 'u' ){
            vowel_count++;
        }
        else{
           cons_count++;
        }
    }
    cout << vowel_count << " "<< cons_count;
}

int main(){

    string basic_input;

    cin >> basic_input;
    int N = basic_input.length();

    Traverse_string(basic_input,N);
    return 0;
}