class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        //two unknowns = nested for loop
        // one unknown: target - current = number to save in hashmap

        HashMap <Integer, Integer> map = new HashMap<>(); //number, index
        for (int i = 0; i < nums.length; i++) {

            int complement = target - nums[i];

            if (map.containsKey(complement)) {
                return new int[]{map.get(complement), i }; //complement is already found first 
            }
            else {
                map.put(nums[i], i);
            }
        }
        return new int[]{};
    }
}