package day_11;

import java.util.Arrays;

public class Day11_StriverMedium {
    public static void main(String[] args) {
        // --- TEST 1: Kadane's Algorithm (Max Subarray) ---
        int[] nums1 = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        System.out.println("1. Max Subarray Sum: " + maxSubArray(nums1));
        // Expected: 6

        // --- TEST 2: Rearrange Array by Sign ---
        int[] nums2 = {3, 1, -2, -5, 2, -4};
        int[] rearranged = rearrangeArray(nums2);
        System.out.println("2. Rearranged: " + Arrays.toString(rearranged));
        // Expected: [3, -2, 1, -5, 2, -4]
        
        // --- REVIEW: Majority Element (Rapid Fire) ---
        // Quick check if you remember Day 7 logic
        int[] nums3 = {2, 2, 1, 1, 1, 2, 2};
        System.out.println("3. Majority Element: " + majorityElement(nums3));
    }

    // ---------------------------------------------------------
    // PROBLEM 1: Maximum Subarray (Kadane's Algorithm)
    // Striver Step 3.2.4
    // Time: O(N), Space: O(1)
    // ---------------------------------------------------------
    public static int maxSubArray(int[] nums) {
        int maxSum = Integer.MIN_VALUE;
        int currentSum = 0;

        for (int num : nums) {
            currentSum += num;
            
            if (currentSum > maxSum) {
                maxSum = currentSum;
            }
            
            // If current "baggage" is negative, drop it.
            if (currentSum < 0) {
                currentSum = 0;
            }
        }
        return maxSum;
    }

    // ---------------------------------------------------------
    // PROBLEM 2: Rearrange Array Elements by Sign
    // Striver Step 3.2.5
    // Time: O(N), Space: O(N)
    // ---------------------------------------------------------
    public static int[] rearrangeArray(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        
        int posIndex = 0;
        int negIndex = 1;
        
        for (int num : nums) {
            if (num > 0) {
                result[posIndex] = num;
                posIndex += 2;
            } else {
                result[negIndex] = num;
                negIndex += 2;
            }
        }
        return result;
    }

    // ---------------------------------------------------------
    // REVIEW: Majority Element (Moore's Voting Algo)
    // ---------------------------------------------------------
    public static int majorityElement(int[] nums) {
        int count = 0;
        int candidate = 0;
        
        for (int num : nums) {
            if (count == 0) candidate = num;
            if (num == candidate) count++;
            else count--;
        }
        return candidate;
    }
}