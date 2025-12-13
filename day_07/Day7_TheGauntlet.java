package day_07;

import java.util.HashSet;
import java.util.Arrays;

public class Day7_TheGauntlet {
    public static void main(String[] args) {
        // --- TEST 1: Contains Duplicate ---
        int[] nums1 = {1, 2, 3, 1};
        System.out.println("1. Contains Duplicate: " + containsDuplicate(nums1)); // Expected: true

        // --- TEST 2: Stock Buy/Sell ---
        int[] prices = {7, 1, 5, 3, 6, 4};
        System.out.println("2. Max Profit: " + maxProfit(prices)); // Expected: 5 (Buy at 1, Sell at 6)

        // --- TEST 3: Majority Element ---
        int[] nums2 = {2, 2, 1, 1, 1, 2, 2};
        System.out.println("3. Majority Element: " + majorityElement(nums2)); // Expected: 2
    }

    // ---------------------------------------------------------
    // PROBLEM 1: Contains Duplicate (LeetCode #217)
    // Logic: Use a HashSet. If add() returns false, it's a dupe.
    // ---------------------------------------------------------
    public static boolean containsDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) {
            if (set.contains(num)) {
                return true; // Found a duplicate!
            }
            set.add(num);
        }
        return false;
    }

    // ---------------------------------------------------------
    // PROBLEM 2: Best Time to Buy and Sell Stock (LeetCode #121)
    // Logic: Track the Lowest Price seen so far, and calculate potential profit.
    // ---------------------------------------------------------
    public static int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;

        for (int price : prices) {
            if (price < minPrice) {
                minPrice = price; // Found a new lowest buying price
            } else if (price - minPrice > maxProfit) {
                maxProfit = price - minPrice; // Check if selling today gives better profit
            }
        }
        return maxProfit;
    }

    // ---------------------------------------------------------
    // PROBLEM 3: Majority Element (LeetCode #169)
    // Logic: Moore Voting Algorithm (O(N) time, O(1) space)
    // ---------------------------------------------------------
    public static int majorityElement(int[] nums) {
        int candidate = nums[0];
        int count = 0;

        for (int num : nums) {
            if (count == 0) {
                candidate = num; // Pick new candidate
            }
            // If num matches candidate, vote UP. Else vote DOWN.
            if (num == candidate) count++;
            else count--;
        }
        return candidate;
    }
}