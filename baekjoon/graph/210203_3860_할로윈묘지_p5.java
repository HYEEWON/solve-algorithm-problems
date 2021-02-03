// 벨만포드
import java.io.*;
import java.util.*;

public class Main {
    static class Pose {
        int x, y;
        Pose(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static class Edge {
        Pose start, end;
        int weight;

        Edge(Pose start, Pose end, int weight) {
            this.start = start;
            this.end = end;
            this.weight = weight;
        }
    }

    static int W, H, G, E;
    static ArrayList<Edge> move;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static int[][] map;
    static long[][] dist;
    static boolean hasCycle;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            W = Integer.parseInt(st.nextToken());
            H = Integer.parseInt(st.nextToken());
            if (W == 0 && H == 0) return;

            map = new int[W][H];
            move = new ArrayList<>();

            G = Integer.parseInt(br.readLine());
            for (int i = 0; i < G; ++i) {
                st = new StringTokenizer(br.readLine());
                int X = Integer.parseInt(st.nextToken());
                int Y = Integer.parseInt(st.nextToken());
                map[X][Y] = -1;
            }

            E = Integer.parseInt(br.readLine());
            for (int i = 0; i < E; ++i) {
                st = new StringTokenizer(br.readLine());
                int X1 = Integer.parseInt(st.nextToken());
                int Y1 = Integer.parseInt(st.nextToken());
                int X2 = Integer.parseInt(st.nextToken());
                int Y2 = Integer.parseInt(st.nextToken());
                int T = Integer.parseInt(st.nextToken());
                move.add(new Edge(new Pose(X1, Y1), new Pose(X2, Y2), T));
                map[X1][Y1] = 2;
            }

            for (int i = 0; i < W; ++i) {
                for (int j = 0; j < H; ++j) {
                    if (map[i][j] != 0) continue;
                    if (i == W - 1 && j == H - 1) continue;
                    for (int k = 0; k < 4; ++k) {
                        int nx = i + dx[k];
                        int ny = j + dy[k];
                        if (nx >= 0 && nx < W && ny >= 0 && ny < H && map[i][j] != -1)
                            move.add(new Edge(new Pose(i, j), new Pose(nx, ny), 1));
                    }
                }
            }

            dist = new long[W][H];
            for (int i = 0; i < W; i++) Arrays.fill(dist[i], Long.MAX_VALUE);
            hasCycle = false;
            bellmanFord(0, 0);

            if (hasCycle) {
                System.out.println("Never");
                continue;
            }
            if (dist[W - 1][H - 1] == Long.MAX_VALUE) System.out.println("Impossible");
            else System.out.println(dist[W - 1][H - 1]);
        }
    }

    public static void bellmanFord(int startX, int startY) {
        boolean update = false;
        dist[startX][startY] = 0;

        for (int i=0; i<W*H-G; ++i) {
            for (Edge edge:move) {
                if (dist[edge.start.x][edge.start.y] != Long.MAX_VALUE
                        && dist[edge.end.x][edge.end.y] > dist[edge.start.x][edge.start.y] + edge.weight){
                    dist[edge.end.x][edge.end.y] = dist[edge.start.x][edge.start.y] + edge.weight;
                    update = true;
                }
            }
            if (!update) break;
        }
        for (Edge edge:move) {
            if (dist[edge.start.x][edge.start.y] != Long.MAX_VALUE
                    && dist[edge.end.x][edge.end.y] > dist[edge.start.x][edge.start.y] + edge.weight){
                hasCycle = true;
            }
        }
    }

}