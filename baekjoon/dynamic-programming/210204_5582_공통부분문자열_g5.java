import java.io.*;
import java.util.*;

public class Main {
    static String A, B;
    static int[][] dp;
    static int answer = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        A = br.readLine();
        B = br.readLine();

        int lengA = A.length();
        int lengB = B.length();
        dp = new int[lengA+1][lengB+1];

        for (int i=1; i<=lengA; ++i) {
            for (int j=1; j<=lengB; ++j) {
                if (i == 1) {
                    if (A.charAt(i - 1) == B.charAt(j - 1)) dp[i][j] = 1;
                } else {
                    if (A.charAt(i - 1) == B.charAt(j - 1)) dp[i][j] = dp[i-1][j-1]+1;
                    answer = Math.max(dp[i][j], answer);
                }
            }
        }
        System.out.println(answer);
    }
}