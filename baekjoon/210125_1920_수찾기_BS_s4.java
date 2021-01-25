import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.Iterator;

public class Main {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = 0, M = 0;
        String[] array1 = {};
        String[] array2 = {};
        try {
            N = Integer.parseInt(br.readLine());
            array1 = br.readLine().split(" ");
            M = Integer.parseInt(br.readLine());
            array2 = br.readLine().split(" ");
        } catch(IOException e) {}

        int[] array = Arrays.stream(array1).mapToInt(Integer::parseInt).toArray();
        Arrays.sort(array);

        for (String s:array2){
            if (binarySearch(s, array)) System.out.println(1);
            else System.out.println(0);
        }
    }

    public static boolean binarySearch(String s, int[] array){
        int start = 0, end = array.length-1;
        int target = Integer.parseInt(s);
        while (start<=end){
            int mid = (start + end)/2;
            if (array[mid] == target) return true;
            else if (target > array[mid]) start = mid + 1;
            else end = mid - 1;
        }
        return false;
    }
}