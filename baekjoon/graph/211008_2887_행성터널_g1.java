// MST
// 좌표가 100000개까지 가능하므로 단일 FOR문으로 그래프를 그려야 함
// x, y, z 축에 대해 각각 정렬하여 그래프를 구함

import java.io.*;
import java.util.*;

public class Main {
    public static class Node {
        int x, y, z;
        int index;

        public Node(int x, int y, int z, int index) {
            this.x = x;
            this.y = y;
            this.z = z;
            this.index = index;
        }
    }

    public static class Item implements Comparable<Item> {
        int start;
        int end;
        int cost;

        public Item(int start, int end, int cost) {
            this.start = start;
            this.end = end;
            this.cost = cost;
        }
        @Override
        public int compareTo(Item o) {
            return Integer.compare(this.cost, o.cost);
        }
    }

    static int N;
    static Node[] sortX, sortY, sortZ;
    static PriorityQueue<Item> graph;
    static int[] parents;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        parents = new int[N+1];
        sortX = new Node[N];
        sortY = new Node[N];
        sortZ = new Node[N];

        for (int i=0; i<N; ++i) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int z = Integer.parseInt(st.nextToken());
            sortX[i] = new Node(x, y, z, i+1);
            sortY[i] = new Node(x, y, z, i+1);
            sortZ[i] = new Node(x, y, z, i+1);

            parents[i+1] = i+1;
        }

        Arrays.sort(sortX, (o1, o2) -> o1.x - o2.x);
        Arrays.sort(sortY, (o1, o2) -> o1.y - o2.y);
        Arrays.sort(sortZ, (o1, o2) -> o1.z - o2.z);

        graph = new PriorityQueue<>();
        for (int i=0; i<N-1; ++i) {
            // 주석도 가능
            /*graph.add(new Item(sortX[i].index, sortX[i+1].index, Math.abs(sortX[i].x - sortX[i+1].x)));
            graph.add(new Item(sortY[i].index, sortY[i+1].index, Math.abs(sortY[i].y - sortY[i+1].y)));
            graph.add(new Item(sortZ[i].index, sortZ[i+1].index, Math.abs(sortZ[i].z - sortZ[i+1].z)));*/
            graph.add(new Item(sortX[i].index, sortX[i+1].index, Math.min(Math.abs(sortX[i].x - sortX[i+1].x),
                    Math.min(Math.abs(sortX[i].y - sortX[i+1].y), Math.abs(sortX[i].z - sortX[i+1].z)))));
            graph.add(new Item(sortY[i].index, sortY[i+1].index, Math.min(Math.abs(sortY[i].x - sortY[i+1].x),
                    Math.min(Math.abs(sortY[i].y - sortY[i+1].y), Math.abs(sortY[i].z - sortY[i+1].z)))));
            graph.add(new Item(sortZ[i].index, sortZ[i+1].index, Math.min(Math.abs(sortZ[i].x - sortZ[i+1].x),
                    Math.min(Math.abs(sortZ[i].y - sortZ[i+1].y), Math.abs(sortZ[i].z - sortZ[i+1].z)))));
        }

        long answer = 0;
        while (!graph.isEmpty()) {
            Item cur = graph.poll();

            int p1 = find(cur.start);
            int p2 = find(cur.end);

            if (p1 == p2)
                continue;

            parents[p2] = p1;
            answer += cur.cost;
        }

        bw.write(String.valueOf(answer));
        bw.close();
        br.close();
    }

    public static int find(int x) {
        if (parents[x] == x)
            return x;
        else
            return parents[x] = find(parents[x]);
    }
}
