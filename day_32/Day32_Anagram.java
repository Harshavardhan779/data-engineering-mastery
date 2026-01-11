package day_32;

public class Day32_Anagram {
    public static void main(String[] args) {
        String s = "anagram";
        String t = "nagaram";
        System.out.println("Is Anagram? " + isAnagram(s, t));
        // Expected: true
    }

    public static boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        
        // Frequency array for 26 lowercase letters
        int[] count = new int[26];
        
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++; // Increment for s
            count[t.charAt(i) - 'a']--; // Decrement for t
        }
        
        // Check if all counts are zero
        for (int c : count) {
            if (c != 0) return false;
        }
        
        return true;
    }
}