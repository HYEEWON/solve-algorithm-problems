import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static Integer[][] triangle, answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        triangle = new Integer[n][n];
        answer = new Integer[n][n];
        for (int i = 0; i < n; ++i) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j=0; j<i+1; ++j) {
                int t = Integer.parseInt(st.nextToken());
                triangle[i][j] = t;
            }
        }

        answer[0][0] = triangle[0][0];
        for (int i = 1; i < n; ++i) {
            for (int j=0; j<i+1; ++j) {
                if (j == 0) answer[i][j] = answer[i-1][j] + triangle[i][j];
                else if (j == i) answer[i][j] = answer[i-1][j-1] + triangle[i][j];
                else answer[i][j] = Math.max(answer[i-1][j-1]+triangle[i][j], answer[i-1][j]+triangle[i][j]);
            }
        }
        System.out.println(Collections.max(Arrays.asList(answer[n-1])));
    }
}
