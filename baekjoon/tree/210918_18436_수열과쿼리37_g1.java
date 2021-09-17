import java.io.*;
import java.util.*;

public class Main {
    static int N, M, offset;
    static int[] A;
    static int a, index, x, l, r;
    static int[] tree;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());

        A = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; ++i)
            A[i] = Integer.parseInt(st.nextToken());

        M = Integer.parseInt(br.readLine());

        offset = 1 << (int)(Math.ceil(Math.log(N) / Math.log(2)));
        tree = new int[offset*2];
        
        init(tree, 0);

        for (int i = 1; i < M + 1; ++i) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());

            if (a == 1) {
                index = Integer.parseInt(st.nextToken());
                x = Integer.parseInt(st.nextToken());
                if (A[index-1] % 2 != 0 && x%2 == 0)
                    update(tree, index-1, 1);
                else if (A[index-1] % 2 == 0 && x%2 != 0)
                    update(tree, index-1, -1);
                A[index-1] = x;
            }
            else if (a == 2) {
                l = Integer.parseInt(st.nextToken());
                r = Integer.parseInt(st.nextToken());
                sb.append(query(tree, l-1, r-1) + "\n");
            }
            else {
                l = Integer.parseInt(st.nextToken());
                r = Integer.parseInt(st.nextToken());
                sb.append((r-l+1-query(tree, l-1, r-1)) + "\n");
            }
        }
        bw.write(sb.toString());
        bw.close();
        br.close();
    }

    public static void init(int[]tree, int mod) {
        for (int i=0; i<N; ++i) {
            if (A[i]%2 == mod)
                tree[i+offset] = 1;
        }
        for (int i=offset-1; i>=1; --i)
            tree[i] = tree[i<<1] + tree[i<<1 | 1];
    }

    public static void update(int[]tree, int idx, int val) {
        idx += offset;
        tree[idx] += val;

        idx >>= 1;
        while (idx>=1) {
            tree[idx] = tree[idx<<1] + tree[idx<<1 | 1];
            idx >>= 1;
        }
    }

    public static int query(int[]tree, int left, int right) {
        int result = 0;
        left += offset;
        right += offset;

        while (left < right) {
            if ((left&1) > 0)
                result += tree[left++];
            if ((right&1) == 0)
                result += tree[right--];
            left >>= 1;
            right >>= 1;
        }
        if (left == right)
            result += tree[left];
        return result;
    }
}