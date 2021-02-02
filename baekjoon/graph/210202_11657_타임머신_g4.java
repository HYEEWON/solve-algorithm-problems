import java.io.*;
import java.util.*;

public class Main {
    static class Node {
        int node, weight;

        Node(int node, int weight) {
            this.node = node;
            this.weight = weight;
        }
    }

    static int N, M; // 도시 수, 버스 노선의 수
    static long[] dist; // 도시로 가는 시간
    static ArrayList<Node>[] list;
    static boolean hasCycle = false; // 음수 사이클이 없으면 false

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        list = new ArrayList[N+1];
        for (int i=1; i < list.length; ++i) {
            list[i] = new ArrayList<>();
        }

        for (int i=0; i<M; ++i) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            list[a].add(new Node(b, c));
        }

        dist = new long[N+1]; Arrays.fill(dist, Long.MAX_VALUE);
        bellmanFord(1); // 벨만-포드
        hasNegCycle(1); // 음의 사이클을 찾는 함수

        // 출력
        if (hasCycle) {
            System.out.println(-1); return;
        } else {
            for (int i = 2; i < N+1; ++i) {
                if (dist[i] == Long.MAX_VALUE) System.out.println(-1);
                else System.out.println(dist[i]);
            }
        }

    }

    public static void bellmanFord(int start) {
        dist[start] = 0; // 시작점을 0으로 하고 시작

        for (int x = 1; x < N; ++x) {
            for (int i = start; i < N+1; ++i) {
                for (Node next : list[i]) {
                    if (dist[i] == Long.MAX_VALUE) break;
                    if (dist[next.node] > dist[i] + next.weight) {
                        dist[next.node] = dist[i] + next.weight;
                    }
                }
            }
        }
    }

    public static void hasNegCycle(int start) {
        for (int i = start; i < N+1; ++i) {
            for (Node next : list[i]) {
                if (dist[i] == Long.MAX_VALUE) continue;
                if (dist[next.node] > dist[i] + next.weight) {
                    hasCycle = true; //음의 사이클이 존재
                    return;
                }
            }
        }
    }
}