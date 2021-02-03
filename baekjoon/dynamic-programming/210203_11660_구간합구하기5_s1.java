import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static int[][] board, answer;

    public static void main(String[] args)  throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        board = new int[N+1][N+1];
        answer = new int[N+1][N+1];

        for (int i=1; i<N+1; ++i) {
            st = new StringTokenizer(br.readLine());
            for (int j=1; j<N+1; ++j) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i=1; i<N+1; ++i) {
            for (int j=1; j<N+1; ++j) {
                answer[i][j] = answer[i-1][j] + answer[i][j-1] - answer[i-1][j-1] + board[i][j];
            }
        }

        for (int i=0; i<M; ++i) {
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());

            bw.write(answer[x2][y2] - answer[x1-1][y2] - answer[x2][y1-1] + answer[x1-1][y1-1]+"\n");
            bw.flush();
        }
        br.close();
        bw.close();
    }
}
