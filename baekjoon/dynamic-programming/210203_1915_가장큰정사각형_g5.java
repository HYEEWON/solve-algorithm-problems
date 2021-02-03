import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static int[][] board, dp;
    static int lengths;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        board = new int[n+1][m+1];
        for (int i=1; i<=n; ++i) {
            String[] ins = br.readLine().split("");
            for (int j=1; j<=m; ++j) {
                board[i][j] = Integer.parseInt(ins[j-1]);
            }
        }

        dp = new int[n+1][m+1];
        lengths = 0;
        for (int i=1; i<=n; ++i) {
            for (int j=1; j<=m; ++j) {
                if (board[i][j] == 1) {
                    dp[i][j] = Math.min(dp[i][j-1], Math.min(dp[i-1][j], dp[i-1][j-1])) + 1;
                    lengths = Math.max(lengths, dp[i][j]);
                }
            }
        }

        bw.write(String.valueOf(lengths*lengths));
        bw.flush();
        bw.close();
        br.close();
    }
}