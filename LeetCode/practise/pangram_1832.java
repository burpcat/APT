// https://leetcode.com/problems/check-if-the-sentence-is-pangram/
// 1832. Check if the sentence is Pangram


class Solution {
    public boolean checkIfPangram(String sentence) {

        for(char i='a'; i<='z'; i++){

            if(!sentence.contains(String.valueOf(i))){
                return false;
            }
        }
        return true;
    }
}
