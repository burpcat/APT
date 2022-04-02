//https://leetcode.com/problems/richest-customer-wealth/
//1672. Richest Customer Wealth

// 5ms

class Solution {
    public int maximumWealth(int[][] accounts) {

        int sum =0;


        for (int i=0; i<accounts.length; i++){

            int indi_sum =  IntStream.of(accounts[i]).sum();

            if(indi_sum > sum){
                sum = indi_sum;
            }
        }


        return sum;
    }
}


// OR

// 4ms

class Solution {
    public int maximumWealth(int[][] accounts) {

        int sum =0;

        //int sum = IntStream.of(some_arr).sum();

        for (int i=0; i<accounts.length; i++){

            int indi_sum =  IntStream.of(accounts[i]).sum();

            if(indi_sum > sum){
                sum = indi_sum;
            }
        }


        return sum;
    }
}
