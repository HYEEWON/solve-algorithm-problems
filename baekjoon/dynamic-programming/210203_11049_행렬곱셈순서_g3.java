import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[][] m;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        m = new int[N+1][N+1];
        for (int i=1; i<N+1; ++i) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            m[i][0] = r; m[i][1] = c;
        }

        dp = new int[N+1][N+1];
        for (int i = 0; i < N+1; ++i) {
            Arrays.fill(dp[i], Integer.MAX_VALUE);
        }
        dfs(1, N);
        System.out.println(dp[1][N]);
    }

    public static int dfs(int start, int end) {
        if (start == end) return 0;
        if (dp[start][end] != Integer.MAX_VALUE) return dp[start][end];

        for (int i=start; i < end; ++i) { //i: 끊는 지점
            dp[start][end] = Math.min(dp[start][end], dfs(start, i) + dfs(i+1, end)+ m[start][0] * m[i][1] * m[end][1]);
        }
        return dp[start][end];
    }
}