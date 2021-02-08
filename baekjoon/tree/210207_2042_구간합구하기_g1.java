import java.io.*;
import java.util.*;

public class Main {
	static int N, M, K;
	static long[] array;
	static long[] tree;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken()); // 수의 변경이 일어나는 횟수
        K = Integer.parseInt(st.nextToken()); // 구간의 합을 구하는 횟수
        
        array = new long[N+1];
        for (int i=1; i<=N; ++i) {
            array[i] = Long.parseLong(br.readLine());
        }
        
		tree = new long[N*4];
		init(1, 1, N);
		
		for (int i = 0; i < M+K; ++i) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			long c = Long.parseLong(st.nextToken());
			if (a == 1) update(1, 1, N, b, c);
			else System.out.println(query(1, 1, N, b, c));
		}
	}
	
	public static long init(int node, int from, int to) {
		if (from == to) return tree[node] = array[from];
		int mid = (from+to) / 2;
		
		return tree[node] = init(node*2, from, mid) + init(node*2+1, mid+1, to);
	}
	
	public static long update(int node, int from, int to, int idx, long val) {
		if (from > idx || to < idx) return tree[node];
		if (from == to) return tree[node] = val;
		int mid = (from+to) / 2;
		
		return tree[node] = update(node*2, from, mid, idx, val) + update(node*2+1, mid+1, to, idx, val);
	}
	
	public static long query(int node, int from, int to, int srchFrom, long srchTo) {
		if (from > srchTo || to < srchFrom) return 0;
		if (from >= srchFrom && to <= srchTo) return tree[node];
		
		int mid = (from+to) / 2;
		
		return query(node*2, from, mid, srchFrom, srchTo) + query(node*2+1, mid+1, to, srchFrom, srchTo);
	}
}