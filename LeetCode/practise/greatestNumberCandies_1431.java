//
// Kids with the Greatest number of Candies .1431


class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {

        // Since ArrayList extends List class, we can use this as a return type

        //ArrayList result = new ArrayList();
        // We are not obliged to mention <Boolean> after ArrayList

        ArrayList<Boolean> result = new ArrayList<Boolean>();

        int max = Arrays.stream(candies).max().getAsInt();

        for(int i=0; i<candies.length ; i++){
            int temp_max = candies[i] + extraCandies;

            result.add(temp_max>=max); // Condition gives us a boolean and directly appends it to ArrayList
        }


        return result;

    }
}
