// https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
// 1365. How Many Numbers Are Smaller Than the Current Number


//Brute force solution



class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {

        int[] count_arr = new int[nums.length];

        for(int i=0; i<nums.length ; i++){

            int sum =0;

            for(int j =0; j<nums.length; j++){

                if(nums[i]>nums[j]){
                    sum++;
                    count_arr[i] = sum;
                }
            }
        }

        return count_arr;

    }
}
