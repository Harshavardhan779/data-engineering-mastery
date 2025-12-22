// package day_14;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;

public class Day14_StriverMedium {
    public static void main(String[] args) {
        // --- TEST 1: Longest Consecutive Sequence ---
        int[] nums1 = {100, 4, 200, 1, 3, 2};
        System.out.println("1. Longest Sequence: " + longestConsecutive(nums1));
        // Expected: 4

        // --- TEST 2: Leaders in Array ---
        int[] nums2 = {10, 22, 12, 3, 0, 6};
        System.out.println("2. Leaders: " + leaders(nums2));
        // Expected: [22, 12, 6]
    }

    // ---------------------------------------------------------
    // PROBLEM 1: Longest Consecutive Sequence
    // Time: O(N) | Space: O(N)
    // ---------------------------------------------------------
    public static int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;
        
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) set.add(num);
        
        int longestStreak = 0;
        
        for (int num : set) {
            // Only attempt to count if 'num' is the START of a sequence
            if (!set.contains(num - 1)) {
                int currentNum = num;
                int currentStreak = 1;
                
                while (set.contains(currentNum + 1)) {
                    currentNum++;
                    currentStreak++;
                }
                longestStreak = Math.max(longestStreak, currentStreak);
            }
        }
        return longestStreak;
    }

    // ---------------------------------------------------------
    // PROBLEM 2: Leaders in Array
    // Time: O(N) | Space: O(N)
    // ---------------------------------------------------------
    public static ArrayList<Integer> leaders(int[] nums) {
        ArrayList<Integer> result = new ArrayList<>();
        int maxFromRight = Integer.MIN_VALUE;
        
        // Iterate from Right -> Left
        for (int i = nums.length - 1; i >= 0; i--) {
            if (nums[i] >= maxFromRight) {
                result.add(nums[i]);
                maxFromRight = nums[i];
            }
        }
        
        // Reverse because we collected them backwards
        Collections.reverse(result); 
        return result;
    }
}