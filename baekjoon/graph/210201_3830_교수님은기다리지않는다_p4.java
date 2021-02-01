import java.io.*;
import java.util.StringTokenizer;

public class Main { //유니온 파인드
    static final int MAX = 100001;
    static int N, M;
    static int[] diff = new int[MAX];
    static int[] parent = new int[MAX];
    static int[] rank = new int[MAX];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        while (true) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            if (N == 0 && M == 0) return;
            for(int i = 0 ; i < MAX;++i) {
                parent[i] = i; diff[i] = 0; rank[i] = 1;
            }

            int a, b, w;
            for (int i = 0; i < M; ++i) {
                st = new StringTokenizer(br.readLine());
                String op = st.nextToken();
                // b가 a보다 w 만큼 무겁다.
                a = Integer.parseInt(st.nextToken());
                b = Integer.parseInt(st.nextToken());
                
                if (op.equals("!")) {
                    w = Integer.parseInt(st.nextToken());
                    union(a, b, w);
                }
                else {
                    if (find(a) == find(b)) System.out.println(diff[b]-diff[a]);
                    else System.out.println("UNKNOWN");
                }
            }
        }
    }

    public static int find(int x) {
        if (parent[x] == x) return x;
        int y = find(parent[x]);
        diff[x] += diff[parent[x]];
        return parent[x] = y;
    }

    public static void union(int x, int y, int w) {
        int xx = find(x);
        int yy = find(y);
        if (xx == yy) return;
        if (rank[xx] > rank[yy]) { // y를 x에 추가
            parent[yy] = xx;
            diff[yy] -= (diff[y] - diff[x] - w);
            rank[xx] += rank[yy];
            rank[yy] = 1;
        } else {
            parent[xx] = yy;
            diff[xx] += (diff[y] - diff[x] - w);
            rank[yy] += rank[xx];
            rank[xx] = 1;
        }
    }
}