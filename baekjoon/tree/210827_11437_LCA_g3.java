import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static ArrayList<Integer>[] list;
    static boolean[] visit;
    static int[] depths; // 각 노드의 깊이
    static int[][] parents; //parents[v][k]: 정점 v의 2^k번째 조상 번호
    static int maxDepth; // 트리의 최대 깊이

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());

        list = new ArrayList[N+1];
        for (int i=1; i<N+1; ++i) {
            list[i] = new ArrayList<>();
        }

        for(int i=1; i<N; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            list[a].add(b); list[b].add(a);
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

        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            int LCA = lca(a, b);
            sb.append(LCA + "\n");
        }

        bw.write(sb.toString());
        bw.close();
        br.close();
    }

    // 완전탐색으로 각 노드들의 depth 저장
    public static void dfs(int now, int depth) {
        visit[now] = true;
        depths[now] = depth;

        for (int next : list[now]) {
            if (visit[next]) continue;
            parents[next][0] = now;
            dfs(next, depth+1);
        }
    }

    // DP를 이용해 각 노드별 2^K 번째 조상 노드를 저장
    public static void dp() {
        for (int i=1; i<maxDepth; ++i) {
            for (int j=1; j<N+1; ++j) {
                parents[j][i] = parents[parents[j][i-1]][i-1];
            }
        }
    }

    // 노드 x, y의 최소 공통 조상을 찾는 함수
    public static int lca(int x, int y) {
        // 두 노드의 깊이를 동일하게 맞춤
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

        for(int i=maxDepth-1; i>=0; i--){
            if(parents[x][i] != parents[y][i]){
                x=parents[x][i];
                y=parents[y][i];
            }
        }
        return parents[x][0];
    }
}
