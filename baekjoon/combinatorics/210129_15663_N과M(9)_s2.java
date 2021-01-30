import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static int numbers[];
    static int visited[];
    static LinkedHashSet<String> set = new LinkedHashSet<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        numbers = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; ++i) {
            numbers[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(numbers);
        visited = new int[N];

        for (int i = 0; i < N; ++i) {
            visited[i] = 1;
            backTracking(i, 1, Integer.toString(numbers[i])+" ");
            visited[i] = 0;
        }

        for (String s: set) {
            System.out.println(s);
        }
    }

    static void backTracking(int idx, int cnt, String str) {
        if (cnt == M) {
            set.add(str);
            return;
        }
        for (int i = 0; i < N; ++i) {
            if (visited[i] == 0) {
                visited[i] = 1;
                backTracking(i, cnt+1, str+Integer.toString(numbers[i])+" ");
                visited[i] = 0;
            }
        }
    }
}