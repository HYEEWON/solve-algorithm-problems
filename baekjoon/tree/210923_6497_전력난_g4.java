// 최소 신장 트리

import java.io.*;
import java.util.*;

public class Main {
    public static class Edge implements Comparable<Edge> {
        int start;
        int end;
        int cost;
        
        public Edge (int start, int end, int cost) {
            this.start = start;
            this.end = end;
            this.cost = cost;
        }
        
        @Override
        public int compareTo(Edge o) {
            return Integer.compare(this.cost, o.cost);
        }
    }
    
    static int M, N, x, y, z;
    static ArrayList<Edge> tree;
    static int[] parents;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
         
        st = new StringTokenizer(br.readLine());            
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
         
        while (M != 0 && N != 0) {
            int totalSum = 0, sumCost = 0;
            tree = new ArrayList<>();
            for (int i=0; i<N; ++i) {
                st = new StringTokenizer(br.readLine());            
                x = Integer.parseInt(st.nextToken());
                y = Integer.parseInt(st.nextToken());
                z = Integer.parseInt(st.nextToken());
                
                tree.add(new Edge(x, y, z));
                totalSum += z;
            }
            
            Collections.sort(tree);
            
            parents = new int[M];
            for (int i=0; i<M; ++i) {
                parents[i] = i;
            }
            
            for (Edge edge : tree) {
                int s = find(edge.start);
                int e = find(edge.end);
                
                if (s == e)
                    continue;
                parents[e] = s;
                sumCost += edge.cost;
            }
            
            sb.append((totalSum - sumCost) + "\n");
                
            st = new StringTokenizer(br.readLine());            
            M = Integer.parseInt(st.nextToken());
            N = Integer.parseInt(st.nextToken());
        }
        bw.write(sb.toString());
        bw.close();
        br.close();
    }
    
    public static int find(int node) {
        if (parents[node] == node)
            return node;
        else
            return parents[node] = find(parents[node]);
    }
}