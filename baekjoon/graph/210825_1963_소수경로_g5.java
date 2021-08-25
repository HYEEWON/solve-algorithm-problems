import java.io.*;
import java.util.*;

public class Main {

    public static class Prime {
        int n;
        int cnt;
        public Prime(int n, int cnt) {
            this.n = n;
            this.cnt = cnt;
        }
    }

    static boolean[] prime; // 소수: true
    static Queue<Prime> q;
    static int answer = Integer.MAX_VALUE;
    static boolean[] visit;

    static int[] d = {1000, 100, 10, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        isPrime(9999);

        int T = Integer.parseInt(br.readLine());

        for (int t=0; t<T; ++t) {
            answer = Integer.MAX_VALUE;

            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());

            visit = new boolean[10000];

            bfs(A, B);

            System.out.println(answer);
        }
    }
    public static void bfs(int A, int B) {
        q = new LinkedList<>();

        q.add(new Prime(A, 0));
        visit[A] = true;

        while (!q.isEmpty()) {
            Prime cur = q.poll();

            if (cur.n == B) {
                answer = Math.min(answer, cur.cnt);
                return;
            }

            for (int i=0; i < 4; ++i) {
                int left = cur.n / d[i] / 10; // 바꿀 수의 왼쪽
                int right = cur.n % d[i]; // 바꿀 수의 오른쪽

                for (int n=0; n < 10; ++n) {
                    if (i==0 && n == 0)
                        continue;

                    int next = (left * d[i] * 10) + (n * d[i]) + right;
                    if (!visit[next] && prime[next]) {
                        q.add(new Prime(next, cur.cnt+1));
                        visit[next] = true;
                    }
                }
            }
        }
    }

    public static void isPrime(int x) {
        prime = new boolean[x+1];
        for (int i=2; i<x+1; ++i)
            prime[i]= true;

        for (int i=2; i<x+1; ++i) {
            if (prime[i] == false)
                continue;

            for (int j=2*i; j<=x; j += i) {
                prime[j]= false;
            }
        }
    }
}
