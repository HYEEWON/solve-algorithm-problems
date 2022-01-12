import java.io.*;

public class Main {
	static int N;
	static int[] stairs, answer;
	public static void main(String[] args)  throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		N = Integer.parseInt(br.readLine());

        stairs = new int[N+1];
        answer = new int[N+1];

        for (int i=1; i<N+1; ++i) {
            stairs[i] = Integer.parseInt(br.readLine());
        }

        answer[1] = stairs[1];
        
        if (N > 1)
        	answer[2] = stairs[1] + stairs[2];
        
        for (int i=3; i<=N; ++i)
        	answer[i]= Math.max(answer[i-2]+stairs[i], answer[i-3]+stairs[i-1]+stairs[i]);
        
        bw.write(answer[N] + "\n");
        
        br.close();
        bw.close();
	}
}
