// https://leetcode.com/problems/create-target-array-in-the-given-order/
// 1389. Create Target Array in the Given Order



class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {

        ArrayList<Integer> output_array = new ArrayList<Integer>();

        int main_len = nums.length; // Length of nums array

        for(int i=0; i<main_len; i++){

            output_array.add(index[i],nums[i]);
        }

        // Converting ArrayList to a normal Array

        int[] result = output_array.stream().mapToInt(i -> i).toArray();

        return result;


    }
}
