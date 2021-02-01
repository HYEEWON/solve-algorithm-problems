//최소 공통 조상
import java.io.*;
import java.util.*;

public class Main {
    static int N, M, maxDepth;
    static ArrayList<Integer>[] list;
    static boolean[] visit;
    static int[] depths;
    static int[][] parents;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        list = new ArrayList[N+1];
        for(int i=0; i<N+1; i++){
            list[i] = new ArrayList<Integer>();
        }
        for(int i=1; i<N; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            list[a].add(b); list[b].add(a);
        }

        int tmp = 1;
        maxDepth = 0; // 최대 depth
        while (tmp <= N) {
            tmp <<= 1; // 비트 연산 x2
            maxDepth++;
        }

        visit = new boolean[N+1];
        depths = new int[N+1];
        parents = new int[N+1][maxDepth]; 
        // parents[k][v]: 정점 v의 2^k번째 조상 번호호

        dfs(1, 1);
        dp();

        M = Integer.parseInt(br.readLine());
        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            int LCA = lca(a, b);
            System.out.println(LCA);
        }


    }

    // 완전탐색으로 각 노드들의 depth 저장
    static void dfs(int now, int depth) {
        visit[now] = true;
        depths[now] = depth;
        for (int next:list[now]) {
            if (visit[next]) continue;
            parents[next][0] = now; // 바로 위의 부모 노드
            dfs(next, depth+1);
        }
    }

    // DP를 이용해 각 노드별 2^K 번째 조상 노드를 저장
    static void dp() {
        for (int i = 1; i < maxDepth; ++i) {
            for (int j = 1; j <= N; ++j) {
                parents[j][i] = parents[parents[j][i-1]][i-1];
            }
        }
    }

    static int lca(int x, int y) {
        if (depths[x] > depths[y]) {
            int tmp = x;
            x = y;
            y = tmp;
        }

        for (int i = maxDepth-1; i >= 0; --i) {
            if (depths[parents[y][i]] >= depths[x]) y = parents[y][i];
        }

        if (x == y) return x;

        for(int i=maxDepth-1; i>=0; i--){
            if(parents[x][i] != parents[y][i]){
                x=parents[x][i];
                y=parents[y][i];
            }
        }
        return parents[x][0];
    }
}