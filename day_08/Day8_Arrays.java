package day_08;

import java.util.Arrays;

public class Day8_Arrays {
    public static void main(String[] args) {
        // TEST 1: Merge Sorted Array
        int[] nums1 = {1, 2, 3, 0, 0, 0}; // 0s are empty space
        int m = 3;
        int[] nums2 = {2, 5, 6};
        int n = 3;
        merge(nums1, m, nums2, n);
        System.out.println("1. Merged: " + Arrays.toString(nums1));

        // TEST 2: Remove Element (Delete '3')
        int[] nums3 = {3, 2, 2, 3};
        int newLength = removeElement(nums3, 3);
        System.out.println("2. Length after removal: " + newLength);

        // TEST 3: Remove Duplicates
        int[] nums4 = {1, 1, 2};
        int uniqueCount = removeDuplicates(nums4);
        System.out.println("3. Unique Count: " + uniqueCount);
    }

    // ---------------------------------------------------------
    // PROBLEM 1: Merge Sorted Array (LeetCode #88)
    // Logic: Fill from the BACK to avoid overwriting.
    // ---------------------------------------------------------
    public static void merge(int[] nums1, int m, int[] nums2, int n) {
        int p1 = m - 1; // End of valid nums1
        int p2 = n - 1; // End of nums2
        int pMerge = m + n - 1; // End of total array

        while (p2 >= 0) {
            if (p1 >= 0 && nums1[p1] > nums2[p2]) {
                nums1[pMerge] = nums1[p1];
                p1--;
            } else {
                nums1[pMerge] = nums2[p2];
                p2--;
            }
            pMerge--;
        }
    }

    // ---------------------------------------------------------
    // PROBLEM 2: Remove Element (LeetCode #27)
    // Logic: If num is NOT val, put it at 'k' and increment 'k'.
    // ---------------------------------------------------------
    public static int removeElement(int[] nums, int val) {
        int k = 0; // The writer pointer
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[k] = nums[i];
                k++;
            }
        }
        return k;
    }

    // ---------------------------------------------------------
    // PROBLEM 3: Remove Duplicates (LeetCode #26)
    // Logic: If current number != previous unique number, write it.
    // ---------------------------------------------------------
    public static int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;
        int k = 1; // Start at 1 because index 0 is always unique
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) { // Found a new unique number
                nums[k] = nums[i];
                k++;
            }
        }
        return k;
    }
}