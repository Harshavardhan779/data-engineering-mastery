package day_26;

public class Day26_Lite {
    public static void main(String[] args) {
        int[][] matrix = {
            {1, 4, 7, 11, 15},
            {2, 5, 8, 12, 19},
            {3, 6, 9, 16, 22},
            {10, 13, 14, 17, 24}
        };
        int target = 5;
        
        System.out.println("Found Target 5? " + searchMatrix(matrix, target));
        // Expected: true
    }

    public static boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0) return false;
        
        int n = matrix.length; 
        int m = matrix[0].length;
        
        // Start at Top-Right Corner
        int row = 0;
        int col = m - 1;
        
        while (row < n && col >= 0) {
            if (matrix[row][col] == target) {
                return true;
            } else if (matrix[row][col] > target) {
                col--; // Current is too big, remove this column
            } else {
                row++; // Current is too small, remove this row
            }
        }
        return false;
    }
}