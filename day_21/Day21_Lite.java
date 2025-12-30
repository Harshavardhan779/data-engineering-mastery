package day_21;

public class Day21_Lite {
    public static void main(String[] args) {
        int[] pages = {12, 34, 67, 90};
        int students = 2;
        
        System.out.println("Min-Max Pages: " + findPages(pages, students));
        // Expected: 113
    }

    public static int findPages(int[] A, int M) {
        if (M > A.length) return -1; // More students than books

        int low = 0, high = 0;
        for (int p : A) {
            low = Math.max(low, p); // Min possible answer (max single book)
            high += p;              // Max possible answer (one student reads all)
        }
        
        int ans = high;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (isPossible(A, mid, M)) {
                ans = mid;     // Feasible, try to reduce pages
                high = mid - 1;
            } else {
                low = mid + 1; // Impossible, need to increase pages
            }
        }
        return ans;
    }

    // Check if we can allocate books such that no one reads > pagesLimit
    static boolean isPossible(int[] A, int pagesLimit, int students) {
        int cnt = 1;
        int sumAllocated = 0;
        
        for (int pages : A) {
            if (sumAllocated + pages > pagesLimit) {
                cnt++; // New student needed
                sumAllocated = pages;
                if (cnt > students) return false;
            } else {
                sumAllocated += pages;
            }
        }
        return true;
    }
}