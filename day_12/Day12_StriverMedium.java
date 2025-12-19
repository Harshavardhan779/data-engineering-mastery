package day_12;

import java.util.Arrays;

public class Day12_StriverMedium {
    public static void main(String[] args) {
        // --- TEST 1: Next Permutation ---
        int[] nums1 = {1, 2, 3};
        nextPermutation(nums1);
        System.out.println("1. Next Permutation (1,2,3): " + Arrays.toString(nums1));
        // Expected: [1, 3, 2]

        int[] nums2 = {3, 2, 1};
        nextPermutation(nums2);
        System.out.println("2. Next Permutation (3,2,1): " + Arrays.toString(nums2));
        // Expected: [1, 2, 3]

        int[] nums3 = {1, 1, 5};
        nextPermutation(nums3);
        System.out.println("3. Next Permutation (1,1,5): " + Arrays.toString(nums3));
        // Expected: [1, 5, 1]
    }

    // ---------------------------------------------------------
    // PROBLEM: Next Permutation (LeetCode #31)
    // Striver Step 3.2.6
    // Time: O(N), Space: O(1)
    // ---------------------------------------------------------
    public static void nextPermutation(int[] nums) {
        int n = nums.length;
        int i = n - 2;

        // STEP 1: Find the break point (first element < next element from back)
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }

        if (i >= 0) {
            // STEP 2: Find the next greater element to swap with
            int j = n - 1;
            while (j >= 0 && nums[j] <= nums[i]) {
                j--;
            }
            swap(nums, i, j);
        }

        // STEP 3: Reverse everything to the right of i
        reverse(nums, i + 1, n - 1);
    }

    private static void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    private static void reverse(int[] nums, int start, int end) {
        while (start < end) {
            swap(nums, start, end);
            start++;
            end--;
        }
    }
}