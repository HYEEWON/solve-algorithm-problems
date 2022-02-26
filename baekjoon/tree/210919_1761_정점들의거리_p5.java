// 최소 공통 조상

import java.io.*;
import java.util.*;

public class Main {
    public static class Node {
        int node;
        int weight;

        public Node(int node, int weight) {
            this.node = node;
            this.weight = weight;
        }
    }

    static int N, M, maxDepth;
    static ArrayList<Node>[] tree;
    static boolean[] visit;
    static int[] depths, dist;
    // dist[i]: i ~ root 사이의 거리
    static int[][] parents;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        tree = new ArrayList[N+1];
        for (int i=1; i<N+1; ++i) {
            tree[i] = new ArrayList<>();
        }

        for (int i=0; i<N-1; ++i) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            tree[a].add(new Node(b, w));
            tree[b].add(new Node(a, w));
        }

        int tmp = 1;
        maxDepth = 0;
        while (tmp<=N) {
            tmp <<= 1;
            maxDepth++;
        }

        visit = new boolean[N+1];
        depths = new int[N+1];
        parents = new int[N+1][maxDepth];
        dist = new int[N+1];
        
        //루트 1
        dfs(1, 1, 0);
        dp();

        M = Integer.parseInt(br.readLine());
        for (int i=0; i<M; ++i) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int nodeLca = lca(a, b);
            sb.append((dist[a] + dist[b] - 2*dist[nodeLca]) + "\n");
        }
        bw.write(sb.toString());
        bw.close();
        br.close();
    }

    public static void dfs(int now, int depth, int weight) {
        visit[now] = true;
        depths[now] = depth;
        dist[now] = weight;
        
        for (Node next : tree[now]) {
            if (visit[next.node]) continue;
            parents[next.node][0] = now;
            dfs(next.node, depth+1, weight+next.weight);
        }
    }

    public static void dp() {
        for (int i=1; i<maxDepth; ++i) {
            for (int j=1; j<N+1; ++j) {
                parents[j][i] = parents[parents[j][i-1]][i-1];
            }
        }
    }

    public static int lca(int x, int y) {
        if (depths[x] > depths[y]) {
            int tmp = x;
            x = y;
            y = tmp;
        }

        for (int i = maxDepth-1; i >= 0; --i) {
            if (depths[parents[y][i]] >= depths[x])
                y = parents[y][i];
        }

        if (x == y)
            return x;

        for (int i = maxDepth-1; i >= 0; --i) {
            if (parents[x][i] != parents[y][i]) {
                x = parents[x][i];
                y = parents[y][i];
            }
        }
        return parents[x][0];
    }
}
