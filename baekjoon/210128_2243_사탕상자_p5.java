import java.io.*;
import java.util.*;

public class Main {
    static int MAX_N = 100000;
    static int treeSize = 2097152;
    static int offset = 1048576;

    static int[] tree = new int[treeSize];
    static int N = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());

        for (int i=0; i<N; ++i) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            if (A == 1) {
                int f = findKth(B);
                System.out.println(f);

                update(f, -1);
            }
            else {
                int C = Integer.parseInt(st.nextToken());
                update(B, C);
            }
        }
    }

    public static void update(int idx, int cnt) {
        idx += offset;

        while (idx > 0) {
            tree[idx] += cnt;
            idx /= 2;
        }
    }

    public static int findKth(int kth) {
        int idx = 1, left, right;

        while (idx < offset) {
            left = idx*2; right = left+1;
            if (tree[left] >= kth) idx = left;
            else {
                kth -=tree[left]; idx = right;
            }
        }
        return idx - offset;
    }
}