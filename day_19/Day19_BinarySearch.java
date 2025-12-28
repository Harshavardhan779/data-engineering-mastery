package day_19;

public class Day19_BinarySearch {
    public static void main(String[] args) {
        // --- TEST CASE 1 ---
        int[] piles = {3, 6, 7, 11};
        int h = 8;
        System.out.println("1. Min Speed for piles {3,6,7,11}, H=8: " + minEatingSpeed(piles, h));
        // Expected: 4 (Hours: 3/4=1, 6/4=2, 7/4=2, 11/4=3 -> 1+2+2+3 = 8 hours)

        // --- TEST CASE 2 ---
        int[] piles2 = {30, 11, 23, 4, 20};
        int h2 = 5;
        System.out.println("2. Min Speed for piles {30,11,23,4,20}, H=5: " + minEatingSpeed(piles2, h2));
        // Expected: 30 (Must eat biggest pile in 1 hour since H=length)
    }

    // ---------------------------------------------------------
    // PROBLEM: Koko Eating Bananas (LeetCode #875)
    // Time: O(N * log(MaxPile))
    // ---------------------------------------------------------
    public static int minEatingSpeed(int[] piles, int h) {
        int low = 1;
        int high = getMax(piles);
        int ans = high;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            // Can we finish in time with speed 'mid'?
            if (canEatAll(piles, mid, h)) {
                ans = mid;    // This speed works, but can we go slower?
                high = mid - 1; 
            } else {
                low = mid + 1; // Too slow, need more speed
            }
        }
        return ans;
    }

    // Helper: Check total hours needed at speed 'k'
    private static boolean canEatAll(int[] piles, int speed, int limit) {
        long totalHours = 0; // Use long to prevent overflow
        for (int pile : piles) {
            // Math.ceil(pile / speed) logic
            // (pile + speed - 1) / speed is an integer trick for ceiling
            totalHours += (pile + speed - 1) / speed;
        }
        return totalHours <= limit;
    }

    // Helper: Find maximum pile size
    private static int getMax(int[] piles) {
        int max = 0;
        for (int p : piles) max = Math.max(max, p);
        return max;
    }
}