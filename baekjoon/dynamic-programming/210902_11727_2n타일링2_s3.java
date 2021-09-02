import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int[] dp = new int[N+1];
        dp[1] = 1;

        if (N > 1)
            dp[2] = 3;
        if (N > 2)
            for (int i=3; i<N+1; ++i)
                dp[i] = (dp[i-1] + dp[i-2]*2) % 10007;
        bw.write(String.valueOf(dp[N]));
        bw.close();
        br.close();
    }
}
