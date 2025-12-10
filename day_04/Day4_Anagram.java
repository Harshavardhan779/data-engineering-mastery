package day_04;

import java.util.Arrays;

public class Day4_Anagram {
    public static void main(String[] args) {
        String s1 = "listen";
        String s2 = "silent";
        
        if (isAnagram(s1, s2)) {
            System.out.println("✅ " + s1 + " and " + s2 + " are Anagrams");
        } else {
            System.out.println("❌ Not Anagrams");
        }
    }

    public static boolean isAnagram(String s, String t) {
        // 1. Edge Case: Different lengths cannot be anagrams
        if (s.length() != t.length()) return false;

        // 2. The Sorting Approach (O(N log N)) - Easiest to understand
        // Convert to char array, sort, and compare
        char[] sChars = s.toCharArray();
        char[] tChars = t.toCharArray();
        
        Arrays.sort(sChars);
        Arrays.sort(tChars);
        
        return Arrays.equals(sChars, tChars);
    }
}