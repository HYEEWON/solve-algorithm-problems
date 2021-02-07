import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static int[] mem, C;
    static int dp[][];
    static int answer = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        mem = new int[N+1];
        for (int i = 1; i <= N; ++i) {
            mem[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        C = new int[N+1];
        for (int i = 1; i <= N; ++i) {
            C[i] = Integer.parseInt(st.nextToken());
        }

        dp = new int[N+1][100*N+1];
        // dp[i][j]: i번째 앱까지 썼을 때, j 비용으로 얻을 수 있는 최대 메모리

        for (int i=1; i<N+1; ++i) {
            for (int j=1; j<100*N+1; ++j) {
                if (i == 1 && C[i] <= j) dp[i][j] = mem[i];
                else {
                    // i번째 앱을 비 활성화할 때의 메모리, i번째 앱을 활성화했을 때의 메모리
                    // i번째 앱은 j-cost[i]부터 cost[i]만큼의 비용을 사용
                    if (C[i] <= j) dp[i][j] = Math.max(dp[i-1][j-C[i]]+mem[i], dp[i-1][j]);
                    else dp[i][j] = dp[i-1][j];
                }
                if (dp[i][j] >= M) answer = Math.min(answer, j);
            }
        }
        System.out.println(answer);
    }
}