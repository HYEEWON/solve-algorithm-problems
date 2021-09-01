import java.io.*;
import java.util.*;

public class Main {
    static long[] fibo;
    static int P;
    static long Q;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        StringBuffer sb = new StringBuffer();

        fibo = new long[10000];
        fibo[0] = 1; fibo[1] = 1;

        int T = Integer.parseInt(br.readLine());
        for (int t=1; t<T+1; ++t) {
            st = new StringTokenizer(br.readLine());
            P = Integer.parseInt(st.nextToken());
            Q = Long.parseLong(st.nextToken());

            for (int i=2; i<P; ++i) {
                fibo[i] = fibo[i-1] % Q + fibo[i-2] % Q;
            }

            sb.append("Case #" + t + ": " + (fibo[P-1] % Q) + "\n");
        }
        bw.write(sb.toString());
        bw.close();
        br.close();
    }
}
