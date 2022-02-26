import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int N = 0;
    static String n = null;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; ++i) {
            n = br.readLine();
            int flag = 0;
            int idx = 2;
            long nocycle = 0, cur = 0;
            int[] cnt = new int[2];

            while (idx < n.length()) {
                if (n.charAt(idx) == '(') {
                    flag = 1;
                    nocycle = cur;
                } else if (n.charAt(idx) != ')'){
                    cnt[flag]++;
                    cur = cur*10 + n.charAt(idx)-'0';
                }
                idx++;
            }

            long child = cur - nocycle;
            long parent = 0;
            for (int j = 0; j < cnt[1]; j++) {
                parent = parent * 10 + 9;
            }
            if (parent == 0) parent = 1;
            for (int j = 0; j < cnt[0]; j++)
            {
                parent = parent * 10;
            }
            //cout << parent << " " << child << endl;
            long gcd =GCD(parent, child);
            //cout << "gcd : " << gcd << endl;
            System.out.println(child / gcd + "/" + parent / gcd);
        }
    }

    public static long GCD(long a, long b) {
        long r = 0;
        while (b!=0) {
            r = a % b;
            a = b;
            b = r;
        }
        return a;
    }
}