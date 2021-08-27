// 벨만포드

import java.io.*;
import java.util.*;

public class Main {

    public static class Node {
        int next;
        int weight;
        public Node(int next, int cost) {
            this.next = next;
            this.weight = cost;
        }
    }

    static int N;
    static ArrayList<Node> list[];
    static int[] dist;
    static boolean hasCycle; // 음수 사이클이 없으면 false
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int TC = Integer.parseInt(br.readLine());
        for (int tc=0; tc<TC; ++tc) {
            st = new StringTokenizer(br.readLine());

            N = Integer.parseInt(st.nextToken()); // 노드 수
            int M = Integer.parseInt(st.nextToken()); // 간선 수
            int W = Integer.parseInt(st.nextToken()); // 웜홀 수

            list = new ArrayList[N+1];
            for(int i = 1 ; i <= N; i++){
                list[i] = new ArrayList<>();
            }

            for (int m=0; m<M; ++m) {
                st = new StringTokenizer(br.readLine());

                int S = Integer.parseInt(st.nextToken());
                int E = Integer.parseInt(st.nextToken());
                int T = Integer.parseInt(st.nextToken());

                list[S].add(new Node(E, T));
                list[E].add(new Node(S, T));
            }

            for (int w=0; w<W; ++w) {
                st = new StringTokenizer(br.readLine());

                int S = Integer.parseInt(st.nextToken());
                int E = Integer.parseInt(st.nextToken());
                int T = Integer.parseInt(st.nextToken());

                list[S].add(new Node(E, (-1) * T));
            }

            // 출발 지점이 1 ~ N
            hasCycle = false;
            for(int i = 1; i <= N; i++) {
                dist = new int[N+1];
                if(bellmanFord(i)) {
                    hasCycle = true;
                    sb.append("YES\n");
                    break;
                }
            }

            if(!hasCycle)
                sb.append("NO\n");
        }

        bw.write(sb.toString());
        bw.close();
        br.close();
    }

    public static boolean bellmanFord(int start) {
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0;
        boolean isUpdate = false;

        for(int i = 1; i < N +1; i++) {
            isUpdate = false;

            for(int j = 1; j <= N; j++) {
                for(Node node : list[j]) {
                    if(dist[j] != Integer.MAX_VALUE && dist[node.next] > dist[j] + node.weight) {
                        dist[node.next] = dist[j] + node.weight;
                        isUpdate = true;
                        if (i == N)
                            return true;
                    }
                }
            }

            if(!isUpdate)
                break;
        }

        return false;
    }
}