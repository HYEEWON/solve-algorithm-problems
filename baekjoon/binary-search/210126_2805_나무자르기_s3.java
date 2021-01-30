import java.io.*;
import java.util.*;

public class Main {
    static Long[] trees;
    static int N = 0, M = 0;
    static long answer = 0;

    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try{

            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            trees = new Long[N];
            st = new StringTokenizer(br.readLine());
            for (int i=0; i<N; ++i){
                trees[i] = Long.parseLong(st.nextToken());
            }
        } catch (IOException e) {}

        Arrays.sort(trees);
        long start = 0, end = trees[trees.length-1];
        while (start <= end) {
            long mid = (start+end) / 2;
            long sum = 0;

            for (long tree:trees) {
                if (tree>mid) sum += (tree-mid);
            }

            if (M <= sum) {
                answer = Math.max(mid, answer);
                start = mid + 1;
            }
            else end = mid - 1;
        }
        System.out.println(answer);
        return;
    }
}