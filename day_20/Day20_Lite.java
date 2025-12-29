package day_20;
import java.util.Arrays;

public class Day20_Lite {
    public static void main(String[] args) {
        int[] stalls = {1, 2, 8, 4, 9};
        int k = 3; // We have 3 cows
        
        System.out.println("Max Min Distance: " + aggressiveCows(stalls, k));
        // Expected Output: 3
    }

    public static int aggressiveCows(int[] stalls, int k) {
        Arrays.sort(stalls); // Step 1: Sort stalls [1, 2, 4, 8, 9]
        
        int low = 1, high = stalls[stalls.length-1] - stalls[0];
        int ans = 1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (canPlace(stalls, k, mid)) { // Can we place cows 'mid' distance apart?
                ans = mid;    // Yes! Store answer
                low = mid + 1; // Try for a larger distance
            } else {
                high = mid - 1; // No! Too ambitious, reduce distance
            }
        }
        return ans;
    }

    // Greedy Check: Try to place cows with 'dist' gap
    static boolean canPlace(int[] stalls, int k, int dist) {
        int count = 1, last = stalls[0];
        for (int i = 1; i < stalls.length; i++) {
            if (stalls[i] - last >= dist) {
                count++;
                last = stalls[i];
            }
            if (count >= k) return true;
        }
        return false;
    }
}