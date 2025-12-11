package day_05;

import java.util.Arrays;
import java.util.HashMap;

public class Day5_TwoSum {
    public static void main(String[] args) {
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        
        int[] result = findTwoSum(nums, target);
        System.out.println("Result: " + Arrays.toString(result));
}
public static int[] findTwoSum(int[] nums,int target){
    HashMap<Integer,Integer> mymap=new HashMap<>();
    for(int i = 0; i < nums.length; i++){
        int diff=target-nums[i];
        if(mymap.containsKey(diff)){
            return new int[]{mymap.get(diff),i};
        }
        mymap.put(nums[i], i);
    }
    return new int[]{};
}
}