package day_24;

public class Day24_Lite {
    public static void main(String[] args) {
        int[][] matrix = {
            {0, 0, 1, 1},
            {0, 1, 1, 1}, // Max 1s here (Row 1)
            {0, 0, 0, 1}
        };
        
        System.out.println("Row with max 1s: " + rowWithMax1s(matrix));
        // Expected: 1
    }

    public static int rowWithMax1s(int[][] arr) {
        int maxRow = -1;
        int maxCount = -1;
        
        // Iterate through each row
        for (int i = 0; i < arr.length; i++) {
            // Find index of first 1 using Lower Bound logic
            int index = firstOneIndex(arr[i]);
            
            // If 1 exists in this row
            if (index != -1) {
                int count = arr[i].length - index;
                if (count > maxCount) {
                    maxCount = count;
                    maxRow = i;
                }
            }
        }
        return maxRow;
    }

    // Helper: Binary Search to find the first occurrence of 1
    static int firstOneIndex(int[] row) {
        int low = 0, high = row.length - 1;
        int ans = -1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (row[mid] == 1) {
                ans = mid;    // Found a 1, look left for an earlier one
                high = mid - 1;
            } else {
                low = mid + 1; // It's a 0, look right
            }
        }
        return ans;
    }
}