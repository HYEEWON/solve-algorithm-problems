// 다익스트라 알고리즘
import java.io.*;
import java.util.*;

public class Main {
    static class Node implements Comparable<Node> {
        int to, weight;
        Node(int to, int weight) {
            this.to = to;
            this.weight = weight;
        }

        @Override
        public int compareTo(Node node) {
            return weight - node.weight;
        }
    }

    static PriorityQueue<Node> pq = new PriorityQueue<>();
    static ArrayList<Node>[] list;
    static int[] distance;
    static int V, E, K;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(br.readLine());

        list = new ArrayList[V+1];
        for (int i=1; i<V+1; ++i) {
            list[i] = new ArrayList<>();
        }

        for (int i=0; i<E; ++i) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            list[u].add(new Node(v, w));
        }

        distance = new int[V+1];
        Arrays.fill(distance, Integer.MAX_VALUE);
        dijkstra(K);

        for (int i=1; i<V+1; ++i) {
            if (distance[i] == Integer.MAX_VALUE) System.out.println("INF");
            else System.out.println(distance[i]);
        }
    }

    public static void dijkstra(int node) {
        boolean[] check = new boolean[V+1];

        pq.add(new Node(node, 0)); //시작점
        distance[node] = 0;

        while(!pq.isEmpty()) {
            Node tmp = pq.poll();
            if (check[tmp.to]) continue;
            check[tmp.to] = true;

            for (Node n : list[tmp.to]) {
                if (distance[n.to] > distance[tmp.to]+n.weight) {
                    distance[n.to] = distance[tmp.to]+n.weight;
                    pq.add(new Node(n.to, distance[n.to]));
                }
            }
        }
    }
}
