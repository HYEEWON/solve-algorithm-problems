import java.io.*;
import java.util.*;

public class Main {
    public static class Gem implements Comparable<Gem> {
        int m;
        int v;
        public Gem (int m, int v) {
            this.m = m;
            this.v = v;
        }
        
        // 무게부터 정렬해야 됨
        @Override
        public int compareTo(Gem o) {
            if (this.m ==  o.m)
                return o.v - this.v;
            else
                return this.m - o.m;
        }
    }
    static int N, K; // 보석 수, 가방 수
    static int[] C; // 가방 최대 무게
    static Gem[] gems; // 무게, 가치
    static PriorityQueue<Integer> pq;
    static long answer = 0;
    
    public static void main(String []args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        
        C = new int[K];
        gems = new Gem[N];

        // 가격이 높은 것부터 저장
        pq = new PriorityQueue<>(Comparator.reverseOrder());
        
        for (int i=0; i<N; ++i) {
            st = new StringTokenizer(br.readLine());
            int m = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            gems[i] = new Gem(m, v);
        }
        
        Arrays.sort(gems);
        
        for (int i=0; i<K; ++i)
            C[i] = Integer.parseInt(br.readLine());
             
        Arrays.sort(C);

       
        for (int i=0, idx = 0; i<K; ++i) {
            while (idx < N && gems[idx].m <= C[i]) {
                pq.add(gems[idx].v);
                idx += 1;
            }

            // 가방 1개당 보석 1개 저장 가능
            if (!pq.isEmpty())
                answer += pq.poll();
        }
        
        bw.write(answer + "\n");
        bw.close();
        br.close();
    }
}