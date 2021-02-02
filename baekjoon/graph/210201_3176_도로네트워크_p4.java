import java.io.*;
import java.util.*;

// 최소 공통 조상
public class Main {
    static class Node {
        int node, distance;

        Node(int node, int distance) {
            this.node = node;
            this.distance = distance;
        }
    }

    static int N, K, maxDepth;
    static HashMap<Integer, ArrayList<Node>> list = new HashMap<>();
    static boolean[] visit;
    static int[] depths;
    static int[][] parents, maxDist, minDist;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());

        for (int i=0; i<N-1; ++i) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            if (!list.containsKey(a)) list.put(a, new ArrayList<Node>());
            ArrayList<Node> tmp = list.get(a); tmp.add(new Node(b, c));
            list.put(a, tmp);
            if (!list.containsKey(b)) list.put(b, new ArrayList<Node>());
            tmp = list.get(b); tmp.add(new Node(a, c));
            list.put(b, tmp);
        }

        // 트리의 최대 높이
        int tmp = 1;
        maxDepth = 0;
        while (tmp <= N) {
            tmp <<= 1;
            maxDepth++;
        }

        visit = new boolean[N+1];
        depths = new int[N+1];
        parents = new int[N+1][maxDepth];
        maxDist = new int[N+1][maxDepth];
        minDist = new int[N+1][maxDepth];

        dfs(1, 1);
        dp();

        K = Integer.parseInt(br.readLine());
        for (int i=0; i<K; ++i) {
            st = new StringTokenizer(br.readLine());
            int d = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());

            Node result = lca(d, e);
            System.out.println(result.node+" "+result.distance);
        }

    }

    public static void dfs(int now, int depth) {
        visit[now] = true;
        depths[now] = depth;
        for (Node node:list.get(now)) {
            if (visit[node.node]) continue;
            parents[node.node][0] = now;
            maxDist[node.node][0] = node.distance;
            minDist[node.node][0] = node.distance;
            dfs(node.node, depth+1);
        }
    }

    public static void dp() {
        for (int i = 1; i < maxDepth; ++i) {
            for (int j = 1; j <= N; ++j) {
                parents[j][i] = parents[parents[j][i-1]][i-1];
                minDist[j][i] = Math.min(minDist[j][i-1], minDist[parents[j][i-1]][i-1]);
                maxDist[j][i] = Math.max(maxDist[j][i-1], maxDist[parents[j][i-1]][i-1]);
            }
        }
    }

    public static Node lca(int x, int y) {
        if (depths[x] > depths[y]) {
            int tmp = x;
            x = y;
            y = tmp;
        }

        int minD = Integer.MAX_VALUE;
        int maxD = Integer.MIN_VALUE;

        for (int i = maxDepth-1; i >= 0; --i) {
            if (depths[parents[y][i]] >= depths[x]) { //(depths[y] - depths[x] >= (1 << i))
                minD = Math.min(minD, minDist[y][i]);
                maxD = Math.max(maxD, maxDist[y][i]);
                y = parents[y][i];
            }
        }

        if (x == y) return new Node(minD, maxD);

        for (int i = maxDepth-1; i >= 0; --i) {
            if (parents[x][i] != parents[y][i]) {
                minD = Math.min(minD, Math.min(minDist[x][i], minDist[y][i]));
                maxD = Math.max(maxD, Math.max(maxDist[x][i], maxDist[y][i]));
                x = parents[x][i];
                y = parents[y][i];
            }
        }
        minD = Math.min(minD, Math.min(minDist[x][0], minDist[y][0]));
        maxD = Math.max(maxD, Math.max(maxDist[x][0], maxDist[y][0]));
        return new Node(minD, maxD);
    }
}
