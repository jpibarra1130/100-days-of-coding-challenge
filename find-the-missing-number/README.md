Link: https://developersinspired.com/2020/03/07/find-the-missing-number-in-an-array/

1. Pertinent information:

    - n distinct numbers
    - only one missing from array
    - expected is a series

2. Some examples:
    - Input: [3,0,1], Output: 2
    - Input: [9,6,4,2,3,5,7,0,1], Output: 8

3. Brute Force
    Attempt 1:
    - Sort the array, and loop through the index.
    - If index != value at index in array, then index is the missing number

    Runtime Complexity: O(nlogn) mainly because of sorting (need to eliminate this)
    Space Complexity: O(1)


4. Optimise
    Attempt 2:
    - Convert the array into a set, and loop through the index and do a lookup
    - If index is missing then return the index

    Runtime Complexity: O(n)
    Space Complexity: O(n) because of the set

    Attempt 3:
    Requires knowledge of the formula for a series:
    Sum of a series is n * (n+1) / 2

    - Loop through the array and compute for the sum.
    - Expected (based on the formula) - the total sum from array is the missing number.

    Runtime Complexity: O(n)
    Space Complexity: O(1) because there's no additional storage needed

5. Ran the algo with the inputs in 2

6. Implementation is in main.py

7. Test cases in main.py

