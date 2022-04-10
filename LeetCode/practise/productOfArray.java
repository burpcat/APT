// https://leetcode.com/problems/product-of-array-except-self/
// 238. Product of Array Except Self
// Approach
//1. First run a for loop to determine the maximum product of the array, if hits zero, increment the count and do NOT count into product
//2. Run a second for loop, and if number of zeroes > 1, then the product will be zero anyway
//3. If the number of zeroes in the array are 1, and the nums[i] is a zero, then we directly return the product to return array
//4. If the number of zeroes are 1, and nums[i] is any other number, then there is a zero element present in the array which will make the product zero anyway so return zero

class Solution {
    public int[] productExceptSelf(int[] nums) {
        
        int arr_len = nums.length;
        int total = 1;
        
        int z = 0;
        
        int[] return_arr = new int[arr_len];
            
        for(int i=0; i< arr_len; i++){
            if(nums[i]==0){
                z++;
            }
            else{
                total *= nums[i];
            }
        }
        
        System.out.println(total);
        System.out.println(z);
        
        for(int i=0; i<arr_len;i++){
            if(z>1){                // We can also combine the below elif with a or                                         statement here
                return_arr[i] = 0;
            }
            else if(z==1 && nums[i]== 0){
                return_arr[i] = total;
            }
            else if(z==1 && nums[i]!=0){
                return_arr[i] = 0;
            }
            else{
                return_arr[i] = total/nums[i];
            }
        }
        
        return return_arr;
    }
}
