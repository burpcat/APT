// https://leetcode.com/problems/concatenation-of-array/
// 1929. Concatenation of Array

class Solution {
    public int[] getConcatenation(int[] nums) {
        
        int nums_len = nums.length;
        
        int[] ans = new int[2*nums_len];
        
        for (int i=0;i<2*nums_len;i++){
            if(i<nums_len){
                ans[i] = nums[i];
            }
            else{
                ans[i] = nums[i-nums_len];
            }
        }
        
        
        return ans;
    }
}
