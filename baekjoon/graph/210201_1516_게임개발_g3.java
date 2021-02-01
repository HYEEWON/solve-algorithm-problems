// 위상 정렬
import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static Queue<Integer> q = new LinkedList<>();
    static int[] inDegree;
    static ArrayList<Integer>[] adjList;
    static int[] answer;
    static int[] time;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());;

        N = Integer.parseInt(st.nextToken());

        inDegree = new int[N+1];
        adjList = new ArrayList[N+1]; // 먼저 짓는 건물 -> 나중에 짓는 건물
        time = new int[N+1];
        answer = new int[N+1];

        for(int i=0; i<N+1; i++){
            adjList[i] = new ArrayList<Integer>();
        }
        for (int i = 1; i < N+1; ++i) {
            st = new StringTokenizer(br.readLine());
            time[i] = Integer.parseInt(st.nextToken());
            while (true) {
                int x = Integer.parseInt(st.nextToken());
                if (x == -1) break;
                inDegree[i]++;
                adjList[x].add(i);
            }
        }

        for (int i = 1; i < N+1; ++i) {
            if (inDegree[i] == 0) {
                q.add(i); answer[i] = time[i];
            }
        }

        while(!q.isEmpty()) {
            int front = q.poll();
            for (int i : adjList[front]) {
                // 모든 건물이 필수로 지어져야 건축 가능
                // 예시: A(10초), B(20초)를 먼저 짓고 C(10초)를 지어야 함
                // C는 B를 지은 20초 후에 지을 수 있음 -> MAX 사용
                answer[i] = Math.max(answer[i], answer[front]+time[i]);
                if ((--inDegree[i]) == 0) q.add(i);
            }
        }

        for (int i = 1; i <= N; i++) {
            System.out.println(answer[i]);
        }
    }
}