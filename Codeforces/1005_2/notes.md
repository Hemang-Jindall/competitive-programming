CF 1005B - Verity is Discouraged
Goal: FInd the maximum length of the array subtracted by the number of distinct elements in the array after choosing a subarray to remove from the array

Initial Idea
1. Check if every element is distinct, the answer in that case is 0.
2. Check if the length of the array is 1, the answer in that case is 0.
3. Find the most prominent number and get rid of the subarray between its most prominent occurances.