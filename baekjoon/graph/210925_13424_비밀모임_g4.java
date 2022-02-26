// 다익스트라

import java.io.*;
import java.util.*;

public class Main {
    public static class Node implements Comparable<Node> {
        int node;
        long cost;

        public Node(int node, long cost) {
            this.node = node;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node o) {
            return Long.compare(this.cost, o.cost);
        }
    }

    static int T, N, M, K;
    static ArrayList<Node>[] graph;
    static int[] friends;
    static long[] dist;
    static long answer, minDist;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        T = Integer.parseInt(br.readLine());
        for (int t=1; t<T+1; ++t) {
            minDist = Long.MAX_VALUE;
            answer = 0;

            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            graph = new ArrayList[N+1];
            for (int i=0; i<N+1; ++i) {
                graph[i] = new ArrayList<>();
            }

            for (int i=0; i<M; ++i) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());
                graph[a].add(new Node(b, c));
                graph[b].add(new Node(a, c));
            }

            K = Integer.parseInt(br.readLine());
            friends = new int[K];
            st = new StringTokenizer(br.readLine());
            for (int i=0; i<K; ++i) {
                friends[i] = Integer.parseInt(st.nextToken());
            }

            for (int i=1; i<N+1; ++i) {
                long tmp = 0;
                dijkstra(i);
                for (int k=0; k<K; ++k) {
                    tmp += dist[friends[k]];
                }
                if (minDist > tmp) {
                    answer = i;
                    minDist = tmp;
                }
            }
            sb.append(answer + "\n");
        }
        bw.write(sb.toString());
        bw.close();
        br.close();
    }

    public static void dijkstra(int start) {
        dist = new long[N+1];
        Arrays.fill(dist, Long.MAX_VALUE);
        dist[start] = 0;
        
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(start, 0));

        while (!pq.isEmpty()) {
            Node cur = pq.poll();

            if (cur.cost > dist[cur.node])
                continue;

            for (Node next : graph[cur.node]) {
                if (dist[next.node] > cur.cost + next.cost) {
                    dist[next.node] = cur.cost + next.cost;
                    pq.add(new Node(next.node, dist[next.node]));
                }
            }
        }
    }
}