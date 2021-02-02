import java.io.*;
import java.util.*;

public class Main {
    static class Node {
        int first, second;

        Node(int first, int second) {
            this.first = first;
            this.second = second;
        }
    }
    static int V, E, K=0; //정점 수, 간선 수, 단절선 수
    static ArrayList<Integer>[] graph;
    static int[] visit; // 방문 순서
    static int order = 0;
    static ArrayList<Node> answer = new ArrayList<>();

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

        for (int i=1; i<V+1; ++i) {
            if (visit[i] == 0) dfs(i, 0);
        }

        Collections.sort(answer, (a1, a2) -> (a1.first == a2.first) ? a1.second - a2.second : a1.first - a2.first);
        System.out.println(answer.size());
        for (int i=0; i<answer.size(); ++i) {
            System.out.println(answer.get(i).first+" "+answer.get(i).second);
        }
    }

    // here: 현 위치, prev: 전 위치
    public static int dfs(int here, int prev) {
        visit[here] = ++order;
        int ret = visit[here];

        for (int next:graph[here]) {
            if (next == prev) continue;
            if (visit[next] > 0) {
                ret = Math.min(ret, visit[next]);
                continue;
            }
            int low = dfs(next, here);
            if (low > visit[here]) {
                if (here < next) answer.add(new Node(here, next));
                else answer.add(new Node(next, here));
            }
            ret = Math.min(ret, low);
        }
        return ret;
    }
}