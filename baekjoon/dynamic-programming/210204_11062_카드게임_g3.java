import java.io.*;
import java.util.*;

public class Main {
    static int T, N;
    static int[] cards;
    static int[][][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        T = Integer.parseInt(br.readLine());
        for(int t=0; t<T; ++t) {
            N = Integer.parseInt(br.readLine());
            cards = new int[N+1];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i=1; i<=N; ++i) {
                cards[i] = Integer.parseInt(st.nextToken());
            }

            dp = new int[2][N+1][N+1]; //면, 행, 열
            for (int i=0; i<2; ++i) {
                for (int j=0; j<N+1; ++j) {
                    Arrays.fill(dp[i][j], -1);
                }
            }
            bw.write(dfs(0, 1, N)+"\n");
            bw.flush();
        }
        bw.close();
        br.close();
    }

    public static int dfs(int turn, int x, int y) { // 남은 카드가 x ~ y일 경우
        if (dp[turn][x][y] != -1) return dp[turn][x][y];
        if (x == y) {
            if (turn == 0) return cards[x];
            return 0;
        }
        if (turn == 0) { // 근우
            dp[turn][x][y] = Math.max(cards[x] + dfs(1, x+1, y), cards[y] + dfs(1, x, y-1));
        } else { //명우의 최선의 선택 == 근우의 값을 최소화 -> min 함수 이용
            dp[turn][x][y] = Math.min(dfs(0, x+1, y), dfs(0, x, y-1));
        }
        return dp[turn][x][y];
    }
}
