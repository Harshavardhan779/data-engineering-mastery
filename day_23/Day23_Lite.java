package day_23;

public class Day23_Lite {
    public static void main(String[] args) {
        int[] arr = {2, 3, 4, 7, 11};
        int k = 5;
        
        System.out.println("The " + k + "th Missing Number is: " + findKthPositive(arr, k));
        // Expected: 9
    }

    public static int findKthPositive(int[] arr, int k) {
        int low = 0, high = arr.length - 1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            // How many numbers are missing up to index 'mid'?
            // Actual value - Expected Value (mid + 1)
            int missing = arr[mid] - (mid + 1);
            
            if (missing < k) {
                low = mid + 1; // Not enough missing numbers yet, go Right
            } else {
                high = mid - 1; // Too many missing numbers, go Left
            }
        }
        
        // The formula derived from algebra: low + k
        return low + k;
    }
}