import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static int[] array, sums;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        array = new int[N+1];
        sums = new int[N+1];
        st = new StringTokenizer(br.readLine());
        for (int i=1; i<=N; ++i) {
            array[i] = Integer.parseInt(st.nextToken());
        }


        for (int i=1; i<=N; ++i) {
            sums[i] = sums[i-1]+array[i];
        }

        for (int x=0; x<M; ++x) {
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());

            bw.write(sums[j] - sums[i-1]+"\n");
            bw.flush();
        }
        bw.close();
    }
}