


class Solution {
    public int maximumPopulation(int[][] logs) {

        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        for(int i=0; i<logs.length;i++){

            // Finding the leftmost birth year
            if(logs[i][0]<min){
                min = logs[i][0];
            }

            // Finding the rightmost death year
            if(logs[i][1]>max){
                max = logs[i][1];
            }
        }

        // Creating a array of size, only of required length
        int result[] = new int[max-min+1];

        for(int i=0 ; i<logs.length; i++){
            for(int j= logs[i][0]; j<logs[i][1]; j++){

                //Incrementing the value of the year if anyone's alive
                result[j-min]++;
            }
        }

        int min_num =0;

	// Loop to find the first highest element
        for(int i=0; i<result.length;i++){
            if(result[i]> result[min_num]){
                min_num =i;
            }
        }


    return min_num+min; // we add minimum here to find the year
    }
}
