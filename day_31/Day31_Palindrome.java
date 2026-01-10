package day_31;

public class Day31_Palindrome {
    public static void main(String[] args) {
        String s = "A man, a plan, a canal: Panama";
        System.out.println("Is Palindrome? " + isPalindrome(s));
        // Expected: true
    }

    public static boolean isPalindrome(String s) {
        if (s.isEmpty()) return true;
        
        int left = 0;
        int right = s.length() - 1;
        
        while (left < right) {
            char currFirst = s.charAt(left);
            char currLast = s.charAt(right);
            
            // 1. Skip non-alphanumeric characters (left side)
            if (!Character.isLetterOrDigit(currFirst)) {
                left++;
            }
            // 2. Skip non-alphanumeric characters (right side)
            else if (!Character.isLetterOrDigit(currLast)) {
                right--;
            }
            // 3. Compare characters (case insensitive)
            else {
                if (Character.toLowerCase(currFirst) != Character.toLowerCase(currLast)) {
                    return false;
                }
                left++;
                right--;
            }
        }
        return true;
    }
}