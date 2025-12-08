package day_02;
import java.util.*;
public class Day2_ReverseArray {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        // Call your reverse function here
        reverse(arr);
        System.out.println(Arrays.toString(arr));
        // Print result
    }

    public static void reverse(int[] arr){
        int l=0;
        int r=arr.length-1;
        while(l<r){
            int temp=arr[l];
            arr[l]=arr[r];
            arr[r]=temp;
            l++;
            r--;
        }

    }
}
