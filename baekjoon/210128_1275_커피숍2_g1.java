import java.io.*;
import java.util.*;

public class Main {
    static int[] arr; // 입력 배열, 리프 노드의 값
    static long[] tree;
    static int N = 0, Q = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        Q = Integer.parseInt(st.nextToken());

        arr = new int[N+1];
        tree = new long[N*4];

        st = new StringTokenizer(br.readLine());
        for (int i=1; i<=N; ++i) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        init(1, 1, N);

        for (int i=0; i<Q; ++i) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            long b = Long.parseLong(st.nextToken());

            if (x > y) System.out.println(query(1, 1, N, y, x));
            else System.out.println(query(1, 1, N, x, y));
            update(1, 1, N, a, b);
        }
    }

    public static long init(int node, int from, int to) {
        if (from == to) return tree[node] = arr[from]; // 리프노드 초기화

        int mid = (from+to) / 2;

        return tree[node] = init(node*2, from, mid)
                + init(node*2+1, mid+1, to);
    }

    public static long update(int node, int from, int to, int idx, long val) {
        if (from > idx || to < idx) return tree[node];
        if (from == to) return tree[node] = val;

        int mid = (from + to) / 2;

        return tree[node] = update(node*2, from, mid, idx, val)
                + update(node*2+1, mid+1, to, idx, val);
    }

    public static long query(int node, int from, int to, int srchFrom, int srchTo) {
        if (to < srchFrom || from > srchTo) return 0;
        if (from >= srchFrom && to <= srchTo) return tree[node];

        int mid = (from+to) / 2;
        return query(node*2, from, mid, srchFrom, srchTo)
                + query(node*2+1, mid+1, to, srchFrom, srchTo);
    }
}