// 세그먼트 트리

import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static int[] numbers;
    static long[] minTree, maxTree;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        numbers = new int[N+1];

        for (int i=1; i<N+1; ++i) {
            numbers[i] = Integer.parseInt(br.readLine());
        }

        minTree = new long[N*4];
        maxTree = new long[N*4];

        initMinTree(1, 1, N);
        initMaxTree(1, 1, N);

        StringBuilder sb = new StringBuilder();
        for (int i=0; i<M; ++i) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            sb.append(findMin(1, 1, N, a, b) + " " + findMax(1, 1, N, a, b) + "\n");
        }

        bw.write(sb.toString());
        bw.flush();
        br.close();
        bw.close();
    }

    public static long initMinTree(int node, int start, int end) {
        if (start == end)
            return minTree[node] = numbers[start];

        int mid = (start + end) / 2;
        return minTree[node] = Math.min(initMinTree(node*2, start, mid), initMinTree(node*2+1, mid+1, end));
    }

    public static long initMaxTree(int node, int start, int end) {
        if (start == end)
            return maxTree[node] = numbers[start];

        int mid = (start + end) / 2;
        return maxTree[node] = Math.max(initMaxTree(node*2, start, mid), initMaxTree(node*2+1, mid+1, end));
    }

    public static long findMin(int node, int start, int end, int left, int right) {
        if (left > end || right < start)
            return 1000000000;
        if (start >= left && end <= right)
            return minTree[node];

        int mid = (start + end) / 2;
        return Math.min(findMin(node*2, start, mid, left, right), findMin(node*2+1, mid+1, end, left, right));
    }

    public static long findMax(int node, int start, int end, int left, int right) {
        if (left > end || right < start)
            return 0;
        if (start >= left && end <= right)
            return maxTree[node];

        int mid = (start + end) / 2;
        return Math.max(findMax(node*2, start, mid, left, right), findMax(node*2+1, mid+1, end, left, right));
    }
}