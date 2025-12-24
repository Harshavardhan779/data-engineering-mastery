package day_16;

public class Day16_BinarySearch {
    public static void main(String[] args) {
        int[] sortedNums = {1, 3, 5, 9, 13, 15, 19, 25};
        
        // --- TEST 1: Standard Binary Search ---
        int target = 13;
        int index = binarySearch(sortedNums, target);
        System.out.println("1. Found " + target + " at index: " + index);
        // Expected: 4
        
        // --- TEST 2: Lower Bound ---
        // Find first element >= 14 (Should be 15, at index 5)
        int lbTarget = 14; 
        int lbIndex = lowerBound(sortedNums, lbTarget);
        System.out.println("2. Lower Bound of " + lbTarget + " is at index: " + lbIndex);
        // Expected: 5
    }

    // ---------------------------------------------------------
    // PROBLEM 1: Binary Search (LeetCode #704)
    // Time: O(log N) | Space: O(1)
    // ---------------------------------------------------------
    public static int binarySearch(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;
        
        while (low <= high) {
            // Calculate mid safely (avoids overflow)
            int mid = low + (high - low) / 2;
            
            if (nums[mid] == target) {
                return mid;
            } else if (target > nums[mid]) {
                low = mid + 1; // Look in Right half
            } else {
                high = mid - 1; // Look in Left half
            }
        }
        return -1; // Not found
    }

    // ---------------------------------------------------------
    // PROBLEM 2: Lower Bound (Striver Concept)
    // Smallest index such that arr[ind] >= target
    // ---------------------------------------------------------
    public static int lowerBound(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;
        int ans = nums.length; // Default to size if not found
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (nums[mid] >= target) {
                ans = mid;    // This could be the answer
                high = mid - 1; // But look left to see if there is a smaller index
            } else {
                low = mid + 1; // Too small, look right
            }
        }
        return ans;
    }
}