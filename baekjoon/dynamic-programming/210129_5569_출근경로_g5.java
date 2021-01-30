import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int w, h;
    static int[][][] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        w = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());

        dp = new int[2][101][101]; //동[0]으로 이동과 북[1]으로 이동을 따로 관리

        dp[0][0][1] = 1;
        dp[1][1][0] = 1;

        for (int i = 0; i < h; ++i) {
            for (int j = 0; j < w; ++j) {
                if (j < w-1) { // 동으로 이동
                    dp[0][i][j+1] = (dp[0][i][j+1] + dp[0][i][j]) % 100000;
                    dp[0][i][j+2] = (dp[0][i][j+2] + dp[1][i][j]) % 100000;
                }
                if (i < h-1) { // 북으로 이동
                    dp[1][i+2][j] = (dp[1][i+2][j] + dp[0][i][j]) % 100000;
                    dp[1][i+1][j] = (dp[1][i+1][j] + dp[1][i][j]) % 100000;
                }
            }
        }

        int answer = dp[0][h-1][w-1];
        answer = (answer + dp[1][h-1][w-1]) % 100000;
        answer = (answer + dp[0][h-1][w]) % 100000;
        answer = (answer + dp[1][h][w-1]) % 100000;
        System.out.println(answer);
    }
}