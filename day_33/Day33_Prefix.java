package day_33;

import java.util.Arrays;

public class Day33_Prefix {
    public static void main(String[] args) {
        String[] strs = {"flower", "flow", "flight"};
        System.out.println("Common Prefix: " + longestCommonPrefix(strs));
        // Expected: "fl"
    }

    public static String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        
        // 1. Sort the array
        Arrays.sort(strs);
        
        // 2. Grab the first and last strings
        String s1 = strs[0];
        String s2 = strs[strs.length - 1];
        
        int idx = 0;
        // 3. Compare characters until they differ
        while(idx < s1.length() && idx < s2.length()){
            if(s1.charAt(idx) == s2.charAt(idx)){
                idx++;
            } else {
                break;
            }
        }
        
        return s1.substring(0, idx);
    }
}