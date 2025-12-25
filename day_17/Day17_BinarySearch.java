package day_17;

import java.util.Arrays;

public class Day17_BinarySearch {
    public static void main(String[] args) {
        int[] nums = {5, 7, 7, 8, 8, 8, 10};
        int target = 8;
        
        int[] result = searchRange(nums, target);
        
        System.out.println("Array: " + Arrays.toString(nums));
        System.out.println("Target: " + target);
        System.out.println("First & Last Position: " + Arrays.toString(result));
        // Expected: [3, 5]
    }

    // ---------------------------------------------------------
    // PROBLEM: Find First and Last Position (LeetCode #34)
    // Time: O(log N) | Space: O(1)
    // ---------------------------------------------------------
    public static int[] searchRange(int[] nums, int target) {
        int first = findBound(nums, target, true);
        int last = findBound(nums, target, false);
        return new int[]{first, last};
    }

    // Helper Function to find boundaries
    // isFirst = true  -> Find First Occurrence
    // isFirst = false -> Find Last Occurrence
    private static int findBound(int[] nums, int target, boolean isFirst) {
        int low = 0, high = nums.length - 1;
        int ans = -1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (nums[mid] == target) {
                ans = mid; // Potential answer found
                
                if (isFirst) {
                    high = mid - 1; // Look Left for first occurrence
                } else {
                    low = mid + 1;  // Look Right for last occurrence
                }
            } else if (target > nums[mid]) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }
}