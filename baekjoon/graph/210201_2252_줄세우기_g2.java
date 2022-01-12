// 위상정렬
import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static Queue<Integer> q = new LinkedList<>();
    static int[] inDegree;
    static ArrayList<Integer>[] adjList;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());;

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        
        // 키가 작은 사람 -> 키가 큰 사람
        inDegree = new int[N+1];
        adjList = new ArrayList[N+1];
        for(int i=0; i<N+1; i++){
            adjList[i] = new ArrayList<Integer>();
        }
        for (int i = 0; i < M; ++i) {
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            inDegree[b]++;
            adjList[a].add(b);
        }

        for (int i = 1; i < N+1; ++i) {
            if (inDegree[i] == 0) q.add(i);
        }
    
        while(!q.isEmpty()) {
            int front = q.poll();
            System.out.print(front+" ");
            for (int i : adjList[front]) {
                if ((--inDegree[i]) == 0) q.add(i);
            }
        }
    }
}
