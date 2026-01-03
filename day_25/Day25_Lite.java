package day_25;

public class Day25_Lite {
    public static void main(String[] args) {
        int[][] matrix = {
            {1, 3, 5, 7},
            {10, 11, 16, 20},
            {23, 30, 34, 60}
        };
        int target = 3;
        
        System.out.println("Found Target 3? " + searchMatrix(matrix, target));
        // Expected: true
    }

    public static boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0) return false;
        
        int n = matrix.length;
        int m = matrix[0].length;
        
        // Treat as a 1D array from index 0 to (n*m - 1)
        int low = 0;
        int high = (n * m) - 1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            // Map 1D 'mid' back to 2D coordinates
            int row = mid / m;
            int col = mid % m;
            
            if (matrix[row][col] == target) {
                return true;
            } else if (matrix[row][col] < target) {
                low = mid + 1; // Look right
            } else {
                high = mid - 1; // Look left
            }
        }
        return false;
    }
}