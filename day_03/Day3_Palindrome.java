package day_03;



public class Day3_Palindrome {
    public static void main(String[] args) {
        // Test Cases
        checkPalindrome("madam");    // Should be true
        checkPalindrome("hello");    // Should be false
        checkPalindrome("Racecar");  // Should be true (Handle case sensitivity!)
    }

    public static void checkPalindrome(String input) {
        // 1. Clean the string (remove spaces, make lowercase)
        // This is important for "Racecar" vs "racecar"
        String cleanStr = input.toLowerCase();
        
        int left = 0;
        int right = cleanStr.length() - 1;
        boolean isPal = true;

        while (left < right) {
            if (cleanStr.charAt(left) != cleanStr.charAt(right)) {
                isPal = false;
                break; // Exit loop immediately if mismatch found
            }
            left++;
            right--;
        }

        if (isPal) {
            System.out.println("✅ '" + input + "' is a Palindrome");
        } else {
            System.out.println("❌ '" + input + "' is NOT a Palindrome");
        }
    }
}
