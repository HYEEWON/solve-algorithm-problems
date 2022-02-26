import java.io.*;
import java.util.*;

public class Main {
    public static class Pose {
        int y;
        int x;

        public Pose(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    static int W, H, answer;
    static int[] dy = {0, 0, 1, -1, 1, 1, -1, -1};
    static int[] dx = {1, -1, 0, 0, 1, -1, 1, -1};
    static int[][] visit, board;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        st = new StringTokenizer(br.readLine());
        W = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());

        while (W!=0 && H!=0) {
            answer = 0;

            board = new int[H][W];
            visit = new int[H][W];

            for (int y = 0; y < H; ++y) {
                st = new StringTokenizer(br.readLine());
                for (int x = 0; x < W; ++x) {
                    board[y][x] = Integer.parseInt(st.nextToken());
                }
            }

            for (int y = 0; y < H; ++y) {
                for (int x = 0; x < W; ++x) {
                    if (board[y][x] == 1 && visit[y][x] == 0) {
                        visit[y][x] = 1;
                        bfs(y, x);
                        answer++;
                    }
                }
            }

            sb.append(answer + "\n");
            st = new StringTokenizer(br.readLine());
            W = Integer.parseInt(st.nextToken());
            H = Integer.parseInt(st.nextToken());
        }
        bw.write(sb.toString());
        bw.close();
        br.close();
    }

    public static void bfs(int y, int x) {
        Queue<Pose> q = new LinkedList<>();
        q.add(new Pose(y, x));

        while(!q.isEmpty()) {
            Pose cur = q.poll();

            for (int i=0; i<8; ++i) {
                int ny = cur.y + dy[i];
                int nx = cur.x + dx[i];

                if (ny<0 || nx<0 || ny>=H || nx>=W || visit[ny][nx] == 1)
                    continue;
                if (board[ny][nx] == 1) {
                    visit[ny][nx] = 1;
                    q.add(new Pose(ny, nx));
                }
            }
        }
    }
}