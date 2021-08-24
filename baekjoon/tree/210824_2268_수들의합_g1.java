// 세그먼트 트리

import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static long[] tree;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        tree = new long[N*4];

        StringBuilder sb = new StringBuilder();
        for (int i=0; i<M; ++i) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            if (a == 0) {
                if (b > c) {
                    int temp = b;
                    b = c;
                    c = temp;
                }
                sb.append(query(1, 1, N, b, c) + "\n");
            }
            else {
                update(1, 1, N, b, c);
            }
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }

    public static long update(int node, int from, int to, int idx, int val) {
        if (idx < from || idx > to)
            return tree[node];
        if (from == to)
            return tree[node] = val;

        int mid = (from + to) / 2;
        return tree[node] = update(node*2, from, mid, idx, val) + update(node*2+1, mid+1, to, idx, val);
    }

    public static long query(int node, int from, int to, int srchFrom, int srchTo) {
        if (from > srchTo || to < srchFrom)
            return 0;
        if (from >= srchFrom && to <= srchTo) return tree[node];

        int mid = (from+to) / 2;

        return query(node*2, from, mid, srchFrom, srchTo) + query(node*2+1, mid+1, to, srchFrom, srchTo);
    }
}