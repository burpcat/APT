// https://leetcode.com/problems/matrix-diagonal-sum/
// 1572. Matrix Diagonal Sum


//Approach
// First, used for loop to iterate throughar[i][i]
// At the same time, iterated the last ith element of the same row
// If the array was even, then there aren't duplicat elements
// But the if the array is odd, then arr[arr.length/2][arr.length/2] is the only repetitive element, and we remove it



class Solution {
    public int diagonalSum(int[][] mat) {

        int sum =0;
        int len = mat.length;

        for(int i=0; i<mat.length; ++i){

                sum += (mat[i][i] + mat[i][len-1-i]);

        }
        if(len%2!=0){
                sum -= mat[len/2][len/2];
            }

    return sum;
    }
}


