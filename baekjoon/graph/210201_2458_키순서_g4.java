import java.io.*;
import java.util.*;

public class Main {
    static final int MAX = 501;
    static Queue<Integer> q = new LinkedList<>();
    static ArrayList<Integer>[][] list;
    static int N, M;
    static int answer = 0;
    static boolean[] visit;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        list = new ArrayList[2][MAX];
        for(int i=0; i<2; i++){
            for(int j=0; j<N+1; j++) {
                list[i][j] = new ArrayList<Integer>();
            }
        }

        while (true) {
            String str =br.readLine();
            if (str == null || str.length() == 0) break;

            st = new StringTokenizer(str);
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            list[0][a].add(b); // 정방향
            list[1][b].add(a); // 역방향향
        }
        for(int i=1; i<=N; i++) {
            visit = new boolean[N+1];
            int big = dfs(0, i); // 정방향 순회로 센 노드 수
            int small = dfs(1, i); // 역방향 순회로 센 노드 수
            if (big + small - 1 == N) answer += 1; // '-1'은 자기 자신
        }

        System.out.println(answer);
    }

    public static int dfs(int mode, int node) {
        int cnt = 1;
        visit[node] = true;

        for (int n:list[mode][node]) {
            if (!visit[n]) cnt += dfs(mode, n);
        }
        return cnt;
    }
}
