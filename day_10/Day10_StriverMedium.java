package day_10;

import java.util.Arrays;
import java.util.HashMap;

public class Day10_StriverMedium {
    public static void main(String[] args) {
        // --- TEST 1: Sort Colors (Dutch National Flag) ---
        int[] nums1 = {2, 0, 2, 1, 1, 0};
        sortColors(nums1);
        System.out.println("1. Sorted Colors: " + Arrays.toString(nums1)); 
        // Expected: [0, 0, 1, 1, 2, 2]

        // --- TEST 2: Two Sum (HashMap) ---
        int[] nums2 = {2, 7, 11, 15};
        int target = 9;
        int[] result = twoSum(nums2, target);
        System.out.println("2. Two Sum Indices: " + Arrays.toString(result));
        // Expected: [0, 1]
    }

    // ---------------------------------------------------------
    // PROBLEM 1: Sort Colors (LeetCode #75)
    // Striver Step 3.2.1
    // Algorithm: Dutch National Flag (3 Pointers)
    // ---------------------------------------------------------
    public static void sortColors(int[] nums) {
        int low = 0;
        int mid = 0;
        int high = nums.length - 1;

        while (mid <= high) {
            if (nums[mid] == 0) {
                // Swap mid with low (Move 0 to front)
                int temp = nums[low];
                nums[low] = nums[mid];
                nums[mid] = temp;
                low++;
                mid++;
            } else if (nums[mid] == 1) {
                // It's in the correct place (middle), just move forward
                mid++;
            } else { // nums[mid] == 2
                // Swap mid with high (Move 2 to back)
                int temp = nums[mid];
                nums[mid] = nums[high];
                nums[high] = temp;
                high--;
                // Note: We don't increment mid here because the swapped element 
                // from 'high' hasn't been checked yet!
            }
        }
    }

    // ---------------------------------------------------------
    // PROBLEM 2: Two Sum (LeetCode #1)
    // Striver Step 3.2.2
    // Algorithm: HashMap for Complement Lookup
    // ---------------------------------------------------------
    public static int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            
            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i };
            }
            map.put(nums[i], i);
        }
        return new int[] {}; // Should not happen
    }
}