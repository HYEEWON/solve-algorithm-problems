import java.io.*;
import java.util.*;

public class Main {
    static Vector<Integer> array = new Vector<>();
    static int[][][] dp;
    static int count = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        while (true) {
            int a = Integer.parseInt(st.nextToken());
            if (a == 0) break;
            array.add(a); count++;
        }

        dp = new int[5][5][array.size()+1];
        System.out.println(dfs(0, 0, 0));
    }

    public static int dfs(int left, int right, int cnt) {
        if (cnt == count) return 0;
        if (dp[left][right][cnt] != 0) return dp[left][right][cnt];
        dp[left][right][cnt] = Math.min(dfs(array.get(cnt), right, cnt+1)+cost(left, array.get(cnt)),
                dfs(left, array.get(cnt), cnt+1)+cost(right, array.get(cnt)));
        return dp[left][right][cnt];
    }

    public static int cost(int start, int end) {
        if (start == 0 || end == 0) return 2;
        int diff = Math.abs(start - end);
        if (diff == 1 || diff == 3) return 3;
        else if (diff == 2) return 4;
        else if (diff == 0) return 1; //start == end
        return 0;
    }
}
