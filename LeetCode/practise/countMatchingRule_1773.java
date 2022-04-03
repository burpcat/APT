// https://leetcode.com/problems/count-items-matching-a-rule/
// 1773. Count Items Matching a Rule


// Approach
// In traditional array, we can use [][] for indexing, but here we used get .get() element
// since Im new to Java af, and used the saem .get() for the sub_array to match the element

class Solution {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {

        int count = 0;
        int decider = 0;


        // Creating a index
        if(ruleKey.equals("type")){
            decider = 0;
        }
        else if(ruleKey.equals("color")){
            decider = 1;
        }
        else if(ruleKey.equals("name")){
            decider = 2;
        }

        for(int i=0; i<items.size(); i++){

        // Python is way better imho

        // Stored the sub array of the list in another list, and then parsed it

            List<String> sub_str= items.get(i);

            if(sub_str.get(decider).equals(ruleValue)){
                count++;
            }
        }

        return count;


    }
}
