import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static int N = 0, K = 0;
    static int[][] dp; //nCk
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        dp = new int[N+1][K+1];
        for (int i = 0; i <= N; ++i) {
            for (int j = 0; j <= Math.min(i, K); ++j) {
                if (j == 0 || i == j) dp[i][j] = 1;
                else dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % 10007;
            }
        }
        System.out.println(dp[N][K]);
    }
}