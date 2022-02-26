// 인덱스 트리
// i번째 이후의 숫자를 카운트 = 구간 합
// 1. 처음에 트리의 모든 리프를 1로 Update
// 2. 가장 큰 수부터 배열에 넣음 = 리프를 0으로 Update
// 3. 반복

import java.io.*;
import java.util.*;

public class Main {
    static int N, offset;
    static int[] inversion_sequence, array;
    static int[] tree;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        inversion_sequence = new int[N+1];

        array = new int[N+1];
        offset = 1 << (int)(Math.ceil(Math.log(N) / Math.log(2)));
        tree = new int[offset*2];

        st = new StringTokenizer(br.readLine());
        for (int i=1; i<N+1; ++i) {
            inversion_sequence[i] = Integer.parseInt(st.nextToken());
            update(i-1, 1);
        }

        int index = 0;
        for (int i=N; i>0; --i) {
            int start = 1;
            int end = N;

            while (start<=end) {
                int mid = (start+end)/2;
                if (query(mid-1, N-1) > inversion_sequence[i]) {
                    index = mid;
                    start = mid + 1;
                }
                else {
                    end = mid - 1;
                }
            }
            array[index] = i;
            update(index-1, -1);
        }

        for (int i=1; i<N+1; ++i) {
            sb.append(array[i] + " ");
        }
        bw.write(sb.toString());
        bw.close();
        br.close();
    }

    public static int query(int left, int right) {
        left += offset;
        right += offset;
        int result = 0;
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

    public static void update(int idx, int val) {
        int i = idx + offset;
        tree[i] += val;
        i >>= 1;

        while (i>=1) {
            tree[i] = tree[i<<1] + tree[i<<1 | 1];
            i >>= 1;
        }
    }
}