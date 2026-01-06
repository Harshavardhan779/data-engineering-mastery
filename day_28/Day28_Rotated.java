package day_28;

public class Day28_Rotated {
    public static void main(String[] args) {
        int[] nums = {4, 5, 6, 7, 0, 1, 2};
        int target = 0;
        
        System.out.println("Index of " + target + ": " + search(nums, target));
        // Expected Output: 4
    }

    public static int search(int[] nums, int target) {
        int low = 0, high = nums.length - 1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (nums[mid] == target) return mid;
            
            // Check if Left Side is Sorted
            if (nums[low] <= nums[mid]) {
                if (nums[low] <= target && target < nums[mid]) {
                    high = mid - 1; // Target is in the left
                } else {
                    low = mid + 1;  // Target is in the right
                }
            } 
            // Otherwise, Right Side is Sorted
            else {
                if (nums[mid] < target && target <= nums[high]) {
                    low = mid + 1;  // Target is in the right
                } else {
                    high = mid - 1; // Target is in the left
                }
            }
        }
        return -1;
    }
}