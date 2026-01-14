package day_35;

import java.util.HashSet;

public class Day35_CloseDuplicate {
    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 1};
        int k = 3;
        System.out.println("Contains Close Duplicate: " + containsNearbyDuplicate(nums, k));
        // Expected: true
    }

    public static boolean containsNearbyDuplicate(int[] nums, int k) {
        HashSet<Integer> window = new HashSet<>();
        
        for (int i = 0; i < nums.length; i++) {
            // 1. If we found a duplicate in the current window
            if (window.contains(nums[i])) {
                return true;
            }
            
            // 2. Add current number to window
            window.add(nums[i]);
            
            // 3. Maintain window size: remove the element that is now too far away
            if (window.size() > k) {
                window.remove(nums[i - k]);
            }
        }
        return false;
    }
}