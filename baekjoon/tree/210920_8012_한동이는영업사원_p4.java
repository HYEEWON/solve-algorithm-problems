// 최소 공통 조상

import java.io.*;
import java.util.*;

public class Main {
    static int N, M, maxDepth;
    static ArrayList<Integer>[] tree;
    static boolean[] visit;
    static int[] depths;
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
            tree[a].add(b);
            tree[b].add(a);
        }

        int tmp = 1;
        maxDepth = 0;
        while (tmp <= N) {
            tmp <<= 1;
            maxDepth++;
        }

        visit = new boolean[N+1];
        depths = new int[N+1];
        parents = new int[N+1][maxDepth];

        dfs(1, 1);
        dp();

        M = Integer.parseInt(br.readLine());
        int prev = Integer.parseInt(br.readLine());
        int LCA = -1;
        int answer = 0;
        for (int i=1; i<M; ++i) {
            int n = Integer.parseInt(br.readLine());
            LCA = lca(prev, n);
            answer += (depths[prev] + depths[n] - depths[LCA]*2);
            prev = n;
        }
        bw.write(String.valueOf(answer));
        bw.close();
        br.close();
    }

    public static void dfs(int now, int depth) {
        visit[now] = true;
        depths[now] = depth;

        for (int next : tree[now]) {
            if (visit[next]) continue;
            parents[next][0] = now;
            dfs(next, depth+1);
        }
    }

    public static void dp() {
        for (int i=1; i<maxDepth; ++i) {
            for (int j=1; j<N+1; ++j) {
                parents[j][i] = parents[parents[j][i-1]][i-1];
            }
        }
    }

    public static int lca(int a, int b) {
        if (depths[a] > depths[b]) {
            int tmp = a;
            a = b;
            b = tmp;
        }

        for (int i=maxDepth-1; i>=0; --i) {
            if (depths[parents[b][i]] >= depths[a])
                b = parents[b][i];
        }

        if (a == b)
            return a;

        for (int i=maxDepth-1; i>=0; --i) {
            if (parents[b][i] != parents[a][i]) {
                b = parents[b][i];
                a = parents[a][i];
            }
        }
        return parents[a][0];
    }
}
