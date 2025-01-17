class Solution {
    public boolean doesValidArrayExist(int[] derived) {
        int xorSum = 0; // Initialize XOR sum
        for (int n : derived) {
            // if(n!=0 && n!=1)
            //return false;     //to check if the given array only contains 1 and 0 but it is not neccessary
            xorSum ^= n; // XOR each element
        }
        return xorSum == 0; // If XOR sum is 0, return true
    }
}