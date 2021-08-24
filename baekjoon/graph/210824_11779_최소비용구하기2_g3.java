// 다익스트라
// 경로: 현재 지점 바로 직전의 지점을 저장하는 배열을 사용해 구함
// 마지막 지점부터 스택에 넣고 pop으로 꺼내 경로를 찾음

import java.io.*;
import java.util.*;

public class Main {
    public static class Bus implements Comparable<Bus>{
        int end;
        int cost;

        public Bus(int end, int cost) {
            this.end = end;
            this.cost = cost;
        }

        @Override
        public int compareTo(Bus o) {
            return cost - o.cost;
        }
    }

    static ArrayList<Bus> busList[];
    static int startCity, endCity;
    static int[] dist;

    static int[] path; // path[i]: 노드 i 직전에 방문한 노드
    static Stack<Integer> visitCity = new Stack<>();
    static int cntVisit = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        busList = new ArrayList[n+1];
        for(int i = 1 ; i <= n; i++){
            busList[i] = new ArrayList<>();
        }


        for (int i=0; i<m; ++i) {
            st = new StringTokenizer(br.readLine());

            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());

            busList[start].add(new Bus(end, cost));
        }

        st = new StringTokenizer(br.readLine());
        startCity = Integer.parseInt(st.nextToken());
        endCity = Integer.parseInt(st.nextToken());

        dist = new int[n+1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        path = new int[n+1];

        dijkstra(n);
        findPath();

        StringBuilder sb = new StringBuilder();
        while(!visitCity.isEmpty()){
            sb.append(visitCity.pop() + " ");
        }

        bw.write(dist[endCity] + "\n");
        bw.write(cntVisit + "\n");
        bw.write(sb.toString() + "\n");

        bw.close();
        br.close();
    }

    public static void dijkstra(int n){
        PriorityQueue<Bus> pq = new PriorityQueue<>();
        boolean check[] = new boolean[n + 1];

        pq.add(new Bus(startCity, 0));
        dist[startCity] = 0;

        while(!pq.isEmpty()){
            Bus curBus = pq.poll();
            int cur = curBus.end;

            if(check[cur] == true) continue;
            check[cur] = true;

            for(Bus bus : busList[cur]){
                if(dist[bus.end] > dist[cur] + bus.cost){
                    dist[bus.end] = dist[cur] + bus.cost;
                    pq.add(new Bus(bus.end, dist[bus.end]));

                    path[bus.end] = cur;
                }
            }
        }
    }

    public static void findPath() {
        int cur = endCity;
        while (cur != 0) {
            visitCity.push(cur);
            cntVisit++;
            cur = path[cur];
        }
    }
}