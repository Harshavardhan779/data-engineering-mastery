package day_22;

public class Day22_Lite {
    public static void main(String[] args) {
        int[] weights = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int days = 5;
        
        System.out.println("Min Ship Capacity: " + shipWithinDays(weights, days));
        // Expected: 15
        // (1,2,3,4,5), (6,7), (8), (9), (10) -> 5 days.
    }

    public static int shipWithinDays(int[] weights, int days) {
        int low = 0, high = 0;
        for (int w : weights) {
            low = Math.max(low, w); // Min capacity must hold the heaviest item
            high += w;              // Max capacity is carrying everything at once
        }
        
        int ans = high;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (canShip(weights, days, mid)) {
                ans = mid;
                high = mid - 1; // Try smaller capacity
            } else {
                low = mid + 1;  // Need bigger capacity
            }
        }
        return ans;
    }

    static boolean canShip(int[] weights, int daysLimit, int capacity) {
        int daysUsed = 1;
        int currentLoad = 0;
        
        for (int w : weights) {
            if (currentLoad + w > capacity) {
                daysUsed++;       // New day needed
                currentLoad = w;  // Start new day with this package
            } else {
                currentLoad += w;
            }
        }
        return daysUsed <= daysLimit;
    }
}