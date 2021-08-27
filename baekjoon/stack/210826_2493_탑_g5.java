import java.io.*;
import java.util.*;

public class Main {
    public static class Top {
        int n;
        int idx;
        public Top(int n, int idx) {
            this.n = n;
            this.idx = idx;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        int[] top = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; ++i) {
            top[i] = Integer.parseInt(st.nextToken());
        }

        Stack<Top> stack = new Stack<>();

        int i = 1;
        sb.append(0 + " ");
        stack.push(new Top(top[0], 0));

        while (!stack.isEmpty() && i<n) {
            Top now = stack.pop();
            if (now.n < top[i]) {
                if (!stack.isEmpty())
                    continue;
                sb.append(0 + " ");
                stack.push(new Top(top[i], i));
            }
            else if (now.n == top[i]) {
                sb.append((now.idx + 1) + " ");
                stack.push(new Top(top[i], i));
            }
            else {
                sb.append((now.idx + 1) + " ");
                stack.push(new Top(now.n, now.idx));
                stack.push(new Top(top[i], i));
            }
            i += 1;
        }

        bw.write(sb.toString());
        bw.close();
        br.close();
    }
}