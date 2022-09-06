import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.StringTokenizer;

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

        int before = 0;
        for (int i = 0; i < N; ++i) {
            visited[i] = 1;
            before = numbers[i];
            backTracking(i, 1, Integer.toString(numbers[i])+" ", before);
            visited[i] = 0;
        }

        for (String s: set) {
            System.out.println(s);
        }
    }

    static void backTracking(int idx, int cnt, String str, int before) {
        if (cnt == M) {
            set.add(str);
            return;
        }
        for (int i = 0; i < N; ++i) {
            if (numbers[i] < before) continue;
            if (visited[i] == 0) {
                visited[i] = 1;
                backTracking(i, cnt+1, str+Integer.toString(numbers[i])+" ", numbers[i]);
                visited[i] = 0;
            }
        }
    }
}