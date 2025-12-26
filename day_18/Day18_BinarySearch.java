// package day_18;

public class Day18_BinarySearch {
    public static void main(String[] args) {
        // --- TEST 1: Perfect Square ---
        int n1 = 25;
        System.out.println("1. Sqrt of " + n1 + ": " + mySqrt(n1));
        // Expected: 5

        // --- TEST 2: Non-Perfect Square ---
        int n2 = 28;
        System.out.println("2. Sqrt of " + n2 + ": " + mySqrt(n2));
        // Expected: 5 (Truncated)
        
        // --- TEST 3: Large Number ---
        int n3 = 2147395600;
        System.out.println("3. Sqrt of " + n3 + ": " + mySqrt(n3));
        // Expected: 46340
    }

    // ---------------------------------------------------------
    // PROBLEM: Sqrt(x) (LeetCode #69)
    // Time: O(log N) | Space: O(1)
    // ---------------------------------------------------------
    public static int mySqrt(int x) {
        if (x == 0) return 0;
        
        long low = 1, high = x;
        long ans = 1; // Store the potential answer
        
        while (low <= high) {
            long mid = low + (high - low) / 2;
            
            // Check if mid * mid <= x
            if (mid * mid <= x) {
                ans = mid;    // This could be the answer
                low = mid + 1; // Try to find a larger number that fits
            } else {
                high = mid - 1; // mid*mid is too big
            }
        }
        return (int) ans;
    }
}