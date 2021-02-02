// 다익스트라 알고리즘
import java.io.*;
import java.util.*;

public class Main {
    static class Node implements Comparable<Node> {
        int node, cost;

        Node(int node, int cost) {
            this.node = node;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node o) {
            return cost-o.cost;
        }
    }

    static int N, M, K;
    static PriorityQueue<Integer>[] dist;
    static ArrayList<Node>[] list;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        list = new ArrayList[N+1];
        dist = new PriorityQueue[N+1];
        for (int i=1; i<N+1; ++i) {
            list[i] = new ArrayList<>();
            dist[i] = new PriorityQueue<>();
        }

        for (int i=0; i<M; ++i) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            list[a].add(new Node(b, c));
        }

        dijkstra(1);

        for (int i = 1; i <= N; ++i){
            if (dist[i].size() >= K) System.out.println(dist[i].peek() * -1);
            else System.out.println(-1);
        }
    }

    public static void dijkstra(int start) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        
        pq.add(new Node(start, 0));
        dist[start].add(0);

        while (!pq.isEmpty()) {
            Node now = pq.poll();

            for (Node node : list[now.node]) {
                if (dist[node.node].size() < K) { //그냥 추가
                    dist[node.node].add((now.cost+node.cost)*(-1));
                    pq.add(new Node(node.node, now.cost+node.cost));
                } else if (dist[node.node].peek()*(-1) > now.cost+node.cost){
                    dist[node.node].poll();
                    dist[node.node].add((now.cost+node.cost)*(-1));
                    pq.add(new Node(node.node, now.cost+node.cost));
                }
            }
        }
    }
}