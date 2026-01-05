package day_27;

public class Day27_Lite {
    public static void main(String[] args) {
        int[] arr = {1, 2, 1, 3, 5, 6, 4};
        
        System.out.println("Peak Index is: " + findPeakElement(arr));
        // Expected: 1 (for value 2) OR 5 (for value 6)
    }

    public static int findPeakElement(int[] nums) {
        int low = 0;
        int high = nums.length - 1;
        
        while (low < high) {
            int mid = low + (high - low) / 2;
            
            // If we are on an upward slope, peak is to the right
            if (nums[mid] < nums[mid + 1]) {
                low = mid + 1;
            } 
            // If we are on a downward slope, peak is here or to the left
            else {
                high = mid;
            }
        }
        return low; // low and high meet at the peak
    }
}