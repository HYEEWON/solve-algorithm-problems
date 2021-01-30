import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int K, M;
    static int numbers[];
    static double[][] triangle = new double[2501][2501];
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        M = Integer.parseInt(br.readLine());
        numbers = new int[M];
        int total = 0;
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; ++i) {
            numbers[i] = Integer.parseInt(st.nextToken());
            total += numbers[i];
        }
        K = Integer.parseInt(br.readLine());

        pascal();
        double down = triangle[total][K];
        double up = 0;
        for (int i = 0; i < M; ++i) {
            up += triangle[numbers[i]][K];
        }
        System.out.println(String.format("%.18f", up/down));
    }

    public static void pascal() {
        triangle[0][0] = triangle[1][0] = triangle[1][1] = 1;
        for (int i = 2; i < 2501; ++i) {
            triangle[i][0] = triangle[i][i] = 1;
            for (int j = 1; j < i; ++j) {
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
            }
        }
    }
}
