package day_30;

import java.util.Arrays;

public class Day30_Reverse {
    public static void main(String[] args) {
        char[] s = {'h', 'e', 'l', 'l', 'o'};
        
        System.out.println("Original: " + Arrays.toString(s));
        reverseString(s);
        System.out.println("Reversed: " + Arrays.toString(s));
        // Expected: [o, l, l, e, h]
    }

    public static void reverseString(char[] s) {
        int left = 0;
        int right = s.length - 1;
        
        while (left < right) {
            // 1. Swap the characters
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            
            // 2. Move pointers towards center
            left++;
            right--;
        }
    }
}