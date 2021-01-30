import java.io.*;
import java.util.*;
//투포인터
public class Main {
    static long T = 0;
    static int n = 0, m = 0;
    static Long[] A;
    static Long[] B;
    static long answer = 0;

    static ArrayList<Long> subA = new ArrayList<>();
    static ArrayList<Long> subB = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        T = Long.parseLong(br.readLine());

        n = Integer.parseInt(br.readLine());
        A = new Long[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; ++i){
            A[i] = Long.parseLong(st.nextToken());
        }

        m = Integer.parseInt(br.readLine());
        B = new Long[m];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<m; ++i) {
            B[i] = Long.parseLong(st.nextToken());
        }

        br.close();

        for (int i=0; i<n; ++i){ //A의 모든 부분합
            long sum = 0;
            for (int j=i; j<n; ++j){
                sum += A[j];
                subA.add(sum);
            }
        }

        for (int i=0; i<m; ++i){
            long sum = 0;
            for (int j=i; j<m; ++j){
                sum += B[j];
                subB.add(sum);
            }
        }

        Collections.sort(subA);
        Collections.sort(subB);

        int start = 0, end = subB.size()-1;
        while (start < subA.size() && end >= 0){
            if (subA.get(start)+subB.get(end) > T) end--;
            else if (subA.get(start)+subB.get(end) < T) start++;
            else { // 부분 합이 같은 것이 여러 개 존재 가능
                long tmp = subA.get(start);
                long cnt1 = 0, cnt2 = 0;
                while (start < subA.size() && tmp == subA.get(start)) {
                    ++cnt1;
                    ++start;
                }
                tmp = subB.get(end);
                while (end >= 0 && tmp == subB.get(end)) {
                    ++cnt2;
                    --end;
                }
                answer += (cnt1*cnt2);
            }
        }
        System.out.println(answer);
    }
}