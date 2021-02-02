import java.io.*;
import java.util.*;

public class Main {
    static int V, E; //정점 수, 간선 수
    static ArrayList<Integer>[] graph;
    static int[] visit;
    static int order = 0;

    static boolean[] cutVertices;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());

        graph = new ArrayList[V+1];
        for (int i=0; i<V+1; ++i) {
            graph[i] = new ArrayList<Integer>();
        }

        for (int i=0; i<E; ++i) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());

            graph[A].add(B); graph[B].add(A);
        }

        visit = new int[V+1];
        cutVertices = new boolean[V+1];

        for (int i=1; i<V+1; ++i) {
            if (visit[i] == 0) dfs(i, true);
        }

        int count = 0;
        for (int i=0; i<cutVertices.length; ++i) {
            if (cutVertices[i]) count++;
        }
        System.out.println(count);
        for (int i=0; i<cutVertices.length; ++i) {
            if (cutVertices[i]) System.out.print(i+" ");
        }
    }

    public static int dfs(int here, boolean isRoot) {
        visit[here] = ++order;
        int ret = visit[here];

        int childCount=0;//root인 경우만 사용할 변수

        for(int next:graph[here]) {
            if (visit[next] > 0) {
                ret = Math.min(ret, visit[next]); // 자식들 중 방문 순서가 가장 빠른 값
                continue;
            }
            childCount++;
            int low = dfs(next, false);
            if (!isRoot && low >= visit[here]) {
                cutVertices[here] = true;
            }
            ret = Math.min(ret, low);
        }

        // 루트이고 자식의 개수가 2개 이상이면 단절점
        if(isRoot && childCount>1) {
            cutVertices[here] = true;
        }
        return ret;
    }
}