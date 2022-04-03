// https://leetcode.com/problems/find-the-highest-altitude/
// 1732. Find the Highest Altitude


class Solution {
    public int largestAltitude(int[] gain) {

        ArrayList<Integer> list = new ArrayList<Integer>();

        int sum =0;

        // initial altitude is zero
        list.add(0);

        for(int i=0;i<gain.length;i++){
            sum += gain[i];
            list.add(sum);
        }

        // To find the maximum value
        int max = Collections.max(list);

    return max;

    }
}
