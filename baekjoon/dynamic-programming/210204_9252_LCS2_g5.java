import java.io.*;
import java.util.*;

public class Main {
    static String A, B;
    static int[][] dp;
    static int answer = 0;
    static Stack<String> str = new Stack<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        A = br.readLine();
        B = br.readLine();

        int lengA = A.length();
        int lengB = B.length();
        dp = new int[lengA+1][lengB+1];

        for (int i=1; i<=lengA; ++i) {
            for (int j=1; j<=lengB; ++j) {
                if (A.charAt(i - 1) == B.charAt(j - 1)) dp[i][j] = dp[i-1][j-1]+1;
                else dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
                answer = Math.max(dp[i][j], answer);
            }
        }

        System.out.println(answer);

        while(dp[lengA][lengB] != 0) {
            if (dp[lengA][lengB] == dp[lengA][lengB-1]) lengB--;
            else if (dp[lengA][lengB] == dp[lengA-1][lengB]) lengA--;
            else {
                str.add(String.valueOf(A.charAt(lengA-1)));
                lengA--;
                lengB--;
            }
        }

        while(!str.isEmpty()) {
            sb.append(str.pop());
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}