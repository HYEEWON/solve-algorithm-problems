import java.io.*;
import java.util.*;

public class Main{
    static int N, M, K;
    static int size;
    static int[] arr;
    static long[] tree;
    
    public static void main(String[] args) throws Exception {
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		arr = new int[N+1];
		for (int i=1; i<N+1; ++i)
		    arr[i] = Integer.parseInt(br.readLine());
		
	    size = 1 << (int)(Math.ceil(Math.log(N) / Math.log(2)));
	    tree = new long[size*2];
	    Arrays.fill(tree, 1);
	    init();
	    //System.out.println(Arrays.toString(tree));
		for (int i=0; i<M+K; ++i) {
		    st = new StringTokenizer(br.readLine());
		    int a = Integer.parseInt(st.nextToken());
		    int b = Integer.parseInt(st.nextToken());
		    int c = Integer.parseInt(st.nextToken());
		    
		    if (a == 1)
		        update(b-1, c);
		    else
		        sb.append(query(b-1, c-1) + "\n");
		       
		    //System.out.println(Arrays.toString(tree));
		}
		bw.write(sb.toString());
		bw.close();
		br.close();
    }
    
    public static void init() {
		for(int i = 0; i < N; i++)
			tree[size+i] = arr[i+1];
		
		for(int i = size - 1; i > 0; i--) 
			tree[i] = (tree[i << 1] * tree[i << 1 | 1]) % 1000000007;
	}
	
    public static void update(int idx, long val) {
        int i = idx + size;
        
        tree[i] = val;
        i >>= 1;
        
        while (i>=1) {
            tree[i] = (tree[i<<1] * tree[i<<1|1]) % 1000000007;
            i >>= 1;
        }
    }
    
    public static long query(int left, int right) {
        left += size;
        right += size;
        
        long result = 1;
        while (left < right) {
            if ((left&1) > 0)
                result = (result * tree[left++]) % 1000000007;
            if ((right&1) == 0)
                result = (result * tree[right--]) % 1000000007;
            left >>= 1;
            right >>= 1;
        }
        if (left == right)
            result = (result * tree[left]) % 1000000007;
        return result;
    }
}