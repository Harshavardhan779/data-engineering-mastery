package day_29;

public class Day29_Square {
    public static void main(String[] args) {
        int num = 16;
        System.out.println("Is " + num + " a perfect square? " + isPerfectSquare(num));
        // Expected: true
    }

    public static boolean isPerfectSquare(int num) {
        if (num < 2) return true;
        
        long low = 1, high = num; // Use long to prevent overflow on mid*mid
        
        while (low <= high) {
            long mid = low + (high - low) / 2;
            long squared = mid * mid;
            
            if (squared == num) {
                return true;
            } else if (squared > num) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return false;
    }
}