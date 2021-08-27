// 다익스트라


// 두 번째 풀이
// 그래프를 정/역방향 2가지 버전으로 저장 -> 다익스트라 실행 횟수 감축 가능

import java.io.*;
import java.util.*;

public class Main {
    public static class Node implements Comparable<Node> {
        int node;
        int weight;

        public Node(int node, int weight) {
            this.node = node;
            this.weight = weight;
        }

        @Override
        public int compareTo(Node node) {
            return weight - node.weight;
        }
    }

    static int N, M, X;
    static ArrayList<Node>[] list;
    static ArrayList<Node>[] listOpp;
    static int[] dist;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());

        list = new ArrayList[N+1];
        listOpp = new ArrayList[N+1];
        for (int i=0; i<N+1; ++i) {
            list[i] = new ArrayList<>();
            listOpp[i] = new ArrayList<>();
        }

        for (int i=0; i<M; ++i) {
            st = new StringTokenizer(br.readLine());
            int S = Integer.parseInt(st.nextToken());
            int E = Integer.parseInt(st.nextToken());
            int W = Integer.parseInt(st.nextToken());

            list[S].add(new Node(E, W));
            listOpp[E].add(new Node(S, W));
        }

        int[] distToX = new int[N+1]; // i~X의 최대 거리를 저장
        dijkstra(X, list);
        for (int i=1; i<N+1; ++i) {        
            distToX[i] = dist[i];
        }
        dijkstra(X, listOpp);

        for (int i=1; i<N+1; ++i) {
            dist[i] += distToX[i];
        }

        Arrays.sort(dist);
        bw.write(Integer.toString(dist[N-1]));
        bw.close();
        br.close();
    }

    public static void dijkstra(int start, ArrayList<Node>[] way) {
        boolean isVisit[] = new boolean[N+1];
        dist = new int[N+1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0;

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(start, 0));

        while (!pq.isEmpty()) {
            Node cur = pq.poll();

            if (isVisit[cur.node])
                continue;
            isVisit[cur.node] = true;

            for (Node next : way[cur.node]) {
                if (dist[next.node] > dist[cur.node] + next.weight) {
                    dist[next.node] = dist[cur.node] + next.weight;
                    pq.add(new Node(next.node, dist[next.node]));
                }
            }
        }
    }
}



// 첫 번째 풀이
// 1~N부터 X까지의 거리 와 X부터 1~N까지의 거리를 구하여 더함
// 다익스트라를 각각 N번, 1번 실행하여 시간이 오래 걸림

import java.io.*;
import java.util.*;

public class Main {
    public static class Node implements Comparable<Node> {
        int node;
        int weight;

        public Node(int node, int weight) {
            this.node = node;
            this.weight = weight;
        }

        @Override
        public int compareTo(Node node) {
            return weight - node.weight;
        }
    }

    static int N, M, X;
    static ArrayList<Node>[] list;
    static int[] dist;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());

        list = new ArrayList[N+1];
        for (int i=0; i<N+1; ++i) {
            list[i] = new ArrayList<>();
        }

        for (int i=0; i<M; ++i) {
            st = new StringTokenizer(br.readLine());
            int S = Integer.parseInt(st.nextToken());
            int E = Integer.parseInt(st.nextToken());
            int W = Integer.parseInt(st.nextToken());

            list[S].add(new Node(E, W));
        }

        int[] distToX = new int[N+1]; // i~X의 최대 거리를 저장
        for (int i=1; i<N+1; ++i) {
            dijkstra(i);
            distToX[i] = dist[X];
        }
        dijkstra(X);

        for (int i=1; i<N+1; ++i) {
            dist[i] += distToX[i];
        }

        Arrays.sort(dist);
        bw.write(Integer.toString(dist[N-1]));
        bw.close();
        br.close();
    }

    public static void dijkstra(int start) {
        boolean isVisit[] = new boolean[N+1];
        dist = new int[N+1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0;

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(start, 0));

        while (!pq.isEmpty()) {
            Node cur = pq.poll();

            if (isVisit[cur.node])
                continue;
            isVisit[cur.node] = true;

            for (Node next : list[cur.node]) {
                if (dist[next.node] > dist[cur.node] + next.weight) {
                    dist[next.node] = dist[cur.node] + next.weight;
                    pq.add(new Node(next.node, dist[next.node]));
                }
            }
        }
    }
}
