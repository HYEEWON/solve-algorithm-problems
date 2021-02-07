import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] array;
    static ArrayList<Integer> answer = new ArrayList<>();
    static int[] index;
    static int count = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        N = Integer.parseInt(br.readLine());
        array = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; ++i) {
            array[i] = Integer.parseInt(st.nextToken());
        }

        answer.add(array[0]);
        index = new int[N];
        index[0] = 0;

        for (int i=1; i<N; ++i) {
            if (array[i] > answer.get(answer.size()-1)) {
                answer.add(array[i]); index[i] = answer.size()-1;
            }
            else {
                int idx = binarySearch(array[i]);
                answer.set(idx, array[i]);
                index[i] = idx;
           }
        }

        count = answer.size();
        bw.write(count+"\n");
        bw.flush();

        count -= 1;
        for (int i = array.length-1; i>=0; --i) {
            if (index[i] == count) {
                answer.set(count, array[i]);
                count--; continue;
            }

        }
        for (int i=0; i<answer.size(); ++i) {
            bw.write(answer.get(i)+" "); bw.flush();
        }
        bw.close();
        br.close();
    }

    public static int binarySearch(int n) {
        int start = 0; int end = answer.size()-1;
        int mid = 0;
        while (start <= end) {
            mid = (start + end) / 2;
            if (mid == 0 && answer.get(mid) >= n) return mid;
            else if (answer.get(mid) >= n && answer.get(mid-1) < n) return mid;
            if (answer.get(mid) > n) end = mid - 1;
            else start = mid + 1;
        }
        return mid;
    }
}