//https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
// 1295. Find Numbers with Even Digits 


class Solution {
    public int findNumbers(int[] nums) {

        int len = nums.length, count=0;

        for(int i=0; i<len; ++i){


            // Converts the given array element to a string, and compares the length
            // We can also use for each loop here
            if(((Integer.toString(nums[i])).length())%2==0){

                count++;
            }

        }
        return count;
    }
}
    public int findNumbers(int[] nums) {
        
        int len = nums.length, count=0;
        
        for(int i=0; i<len; ++i){
            
            
            // Converts the given array element to a string, and compares the length
            // We can also use for each loop here
            if(((Integer.toString(nums[i])).length())%2==0){
                
                count++;
           }
            
       
