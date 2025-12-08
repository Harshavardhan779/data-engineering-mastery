import java.util.*;
public class Day1_DSA {
    public static void main(String[] str){
        ArrayList<Integer> all=new ArrayList<>();
        ArrayList<Integer> even=new ArrayList<>();
        for(int i=0;i<10;i++){
            all.add(i);
        }
        for(int n:all){
            if(n%2==0){
                even.add(n);
            }
        }
        System.out.println("The elements are "+even);
    }
}
