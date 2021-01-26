import java.io.*;
import java.util.*;

public class Main {
    static int N = 0;
    static Integer[][] board;
    static Integer[][] dpMin;
    static Integer[][] dpMax;

    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try {
            N = Integer.parseInt(br.readLine());
            board = new Integer[N][3];
            for(int i=0; i<N; ++i) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for(int j=0; j<3; ++j) {
                    board[i][j] = Integer.parseInt(st.nextToken());
                }
            }
        } catch (IOException e) {}

        dpMin = new Integer[N][3];
        dpMax = new Integer[N][3];

        for (int i=0; i<N; ++i) {
            for(int j=0; j<3; ++j) {
                if (i == 0) {
                    dpMin[i][j] = board[i][j];
                    dpMax[i][j] = board[i][j];
                }
                else {
                    if (j == 0) {
                        dpMin[i][j] = Math.min(dpMin[i-1][j]+board[i][j], dpMin[i-1][j+1]+board[i][j]);
                        dpMax[i][j] = Math.max(dpMax[i-1][j]+board[i][j], dpMax[i-1][j+1]+board[i][j]);
                    }
                    else if (j == 2) {
                        dpMin[i][j] = Math.min(dpMin[i-1][j]+board[i][j], dpMin[i-1][j-1]+board[i][j]);
                        dpMax[i][j] = Math.max(dpMax[i-1][j]+board[i][j], dpMax[i-1][j-1]+board[i][j]);
                    }
                    else {
                        dpMin[i][j] = Math.min(Math.min(dpMin[i-1][j]+board[i][j], dpMin[i-1][j-1]+board[i][j]), dpMin[i-1][j+1]+board[i][j]);
                        dpMax[i][j] = Math.max(Math.max(dpMax[i-1][j]+board[i][j], dpMax[i-1][j-1]+board[i][j]), dpMax[i-1][j+1]+board[i][j]);
                    }
                }
            }
        }
        System.out.println(Collections.max(Arrays.asList(dpMax[N-1]))+" "+Collections.min(Arrays.asList(dpMin[N-1])));
    }
}