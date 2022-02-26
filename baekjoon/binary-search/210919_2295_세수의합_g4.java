// x + y+ z = k, x + y = k - z
// 양쪽을 두 개로 나누어 계산

// 이분 탐색 풀이
import java.io.*;
import java.util.*;

public class Main {
    static int N, answer=0;
    static int[] U;
    static HashSet<Long> sum = new HashSet<>();
    static List sortSum;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        U = new int[N+1];
        for (int i=1; i<N+1; ++i)
            U[i] = Integer.parseInt(br.readLine());

        Arrays.sort(U);

        for (int i=1; i<U.length; ++i) {
            for (int z=i; z<U.length; ++z) {
                long tmp = U[i]+U[z];
                sum.add(tmp);
            }
        }

        sortSum = new ArrayList(sum);
        Collections.sort(sortSum);
        
        for (int i=U.length-1; i>0; --i) {
            for (int z=1; z<i; ++z) {
                if (U[i] > U[z] && binarySearch(U[i]-U[z])) {
                    answer = U[i];
                    bw.write(String.valueOf(answer)+"\n");
                    bw.close();
                    br.close();
                    return;
                }
            }
        }
    }

    public static boolean binarySearch(long result) {
        int start = 0; int end = sortSum.size()-1;

        while (start <= end) {
            int mid = (start + end) / 2;

            if ((long)sortSum.get(mid) == result)
                return true;
            else if ((long)sortSum.get(mid) > result)
                end = mid - 1;
            else
                start = mid + 1;
        }
        return false;
    }
}

// 완전탐색 풀이
import java.io.*;
import java.util.*;

public class Main {
    static int N, answer=0;
    static int[] U;
    static HashSet<Long> sum = new HashSet<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        U = new int[N+1];
        for (int i=1; i<N+1; ++i)
            U[i] = Integer.parseInt(br.readLine());

        Arrays.sort(U);
        // x + y+ z = k, x + y = k - z
        for (int i=1; i<U.length; ++i) {
            for (int z=1; z<U.length; ++z) {
                long tmp = U[i]+U[z];
                sum.add(tmp);
            }
        }
        boolean flag = true;
        for (int i=U.length-1; i>0; --i) {
            for (int z=1; z<U.length; ++z) {
                long tmp = U[i]-U[z];
                if (U[i] > U[z] && sum.contains(tmp)) {
                    answer = U[i];
                    flag = false;
                    break;
                }
            }
            if (!flag)
                break;
        }
        bw.write(String.valueOf(answer)+"\n");
        bw.close();
        br.close();
    }
}
