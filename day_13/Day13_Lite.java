package day_13;

import java.util.HashSet;

public class Day13_Lite {
    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 1};
        System.out.println("Contains Duplicate: " + containsDuplicate(nums));
        // Expected: true
    }

    public static boolean containsDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) {
            if (set.contains(num)) {
                return true;
            }
            set.add(num);
        }
        return false;
    }
}