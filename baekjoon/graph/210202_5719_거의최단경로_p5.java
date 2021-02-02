import java.io.*;
import java.util.*;

public class Main {
    static class Node implements Comparable<Node> {
        int dest, weight;

        Node(int dest, int weight) {
            this.dest = dest;
            this.weight = weight;
        }

        @Override
        public int compareTo(Node o) {
            return weight - o.weight;
        }
    }

    static int N, M, S, D; // 장소 수, 도로 수, 시작점, 도착점
    static int[][] list;
    static int[] dist;
    static PriorityQueue<Node> pq = new PriorityQueue<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            if (N == 0 && M == 0) return;

            st = new StringTokenizer(br.readLine());
            S = Integer.parseInt(st.nextToken());
            D = Integer.parseInt(st.nextToken());

            list = new int[N][N];

            for (int i = 0; i < M; ++i) {
                st = new StringTokenizer(br.readLine());
                int u = Integer.parseInt(st.nextToken());
                int v = Integer.parseInt(st.nextToken());
                int p = Integer.parseInt(st.nextToken());

                list[u][v] = p;
            }

            dist = new int[N]; Arrays.fill(dist, Integer.MAX_VALUE);
            dijkstra(S);

            bfs(D);

            dist = new int[N]; Arrays.fill(dist, Integer.MAX_VALUE);
            dijkstra(S);

            if (dist[D] == Integer.MAX_VALUE) System.out.println(-1);
            else System.out.println(dist[D]);
        }
    }

    public static void dijkstra(int start) {
        boolean[] check = new boolean[N];

        pq.add(new Node(start, 0));
        dist[start] = 0;

        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            if (check[cur.dest]) continue;
            check[cur.dest] = true;

            for (int i = 0; i < N; i++) {
                if (list[cur.dest][i] == 0) continue;
                if (dist[i] > dist[cur.dest]+list[cur.dest][i]) {
                    dist[i] = dist[cur.dest]+list[cur.dest][i];
                    pq.add(new Node(i, dist[i]));
                }
            }
        }
    }

    public static void bfs(int end) {
        Queue<Integer> q = new LinkedList<>();
        boolean[] check = new boolean[N];
        
        q.add(end);
        while (!q.isEmpty()) {
            Integer cur = q.poll();
            if (check[cur]) continue;
            check[cur] = true;
            
            for (int i=0; i< N; ++i) {
                if (list[i][cur] == 0) continue;
                if (dist[cur] == dist[i]+list[i][cur]) {
                    list[i][cur] = 0;
                    q.add(i);
                }
            }
        }
    }
}