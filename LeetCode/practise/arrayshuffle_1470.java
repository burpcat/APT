// https://leetcode.com/problems/shuffle-the-array/
// 1470. Shuffle the Array



// Approach
// from the nums array, we need to place the first n elemeents in even positions, then after
// n elements in odd positions, so used a for loop to iterate from 0 to array length
// and then placed the first n elements at even places, and immediately placed the odd elements
// at the next place
//
// Used iter+n, to retreive the nth next number from the initial iterating place

class Solution {
    public int[] shuffle(int[] nums, int n) {

        int arr_len = nums.length;

        int[] return_array = new int[arr_len];

        int iter =0;

        for(int i=0; i<arr_len ; i+=2){
            // System.out.println(i);
            return_array[i] = nums[iter];
            return_array[i+1] = nums[iter+n];

            iter++;
        }


        return return_array;
    }
}
