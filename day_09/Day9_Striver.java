package day_09;

import java.util.Arrays;

public class Day9_Striver {
    public static void main(String[] args) {
        // --- TEST 1: Rotate Array (Reversal Algo) ---
        int[] nums1 = {1, 2, 3, 4, 5, 6, 7};
        int k = 3;
        rotate(nums1, k);
        System.out.println("1. Rotated Array: " + Arrays.toString(nums1)); 
        // Expected: [5, 6, 7, 1, 2, 3, 4]

        // --- TEST 2: Missing Number (Math Approach) ---
        int[] nums2 = {3, 0, 1};
        System.out.println("2. Missing Number: " + missingNumber(nums2)); 
        // Expected: 2

        // --- TEST 3: Max Consecutive Ones ---
        int[] nums3 = {1, 1, 0, 1, 1, 1};
        System.out.println("3. Max Consecutive Ones: " + findMaxConsecutiveOnes(nums3));
        // Expected: 3
    }

    // ---------------------------------------------------------
    // PROBLEM 1: Rotate Array (LeetCode #189)
    // Striver's Approach: Reversal Algorithm
    // Time: O(N), Space: O(1)
    // ---------------------------------------------------------
    public static void rotate(int[] nums, int k) {
        int n = nums.length;
        k = k % n; // In case k is larger than array size
        
        // 1. Reverse the whole array
        reverse(nums, 0, n - 1);
        // 2. Reverse the first k elements
        reverse(nums, 0, k - 1);
        // 3. Reverse the remaining elements
        reverse(nums, k, n - 1);
    }

    // Helper method for reversal
    public static void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }

    // ---------------------------------------------------------
    // PROBLEM 2: Missing Number (LeetCode #268)
    // Striver's Approach: Summation Formula
    // Time: O(N), Space: O(1)
    // ---------------------------------------------------------
    public static int missingNumber(int[] nums) {
        int n = nums.length;
        int expectedSum = n * (n + 1) / 2;
        int actualSum = 0;
        
        for (int num : nums) {
            actualSum += num;
        }
        return expectedSum - actualSum;
    }

    // ---------------------------------------------------------
    // PROBLEM 3: Max Consecutive Ones (LeetCode #485)
    // Time: O(N), Space: O(1)
    // ---------------------------------------------------------
    public static int findMaxConsecutiveOnes(int[] nums) {
        int maxCount = 0;
        int currentCount = 0;
        
        for (int num : nums) {
            if (num == 1) {
                currentCount++;
                maxCount = Math.max(maxCount, currentCount);
            } else {
                currentCount = 0;
            }
        }
        return maxCount;
    }
}