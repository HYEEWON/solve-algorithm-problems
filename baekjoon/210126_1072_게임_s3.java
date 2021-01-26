import java.io.*;
import java.util.*;

public class Main {
    static Long X = 0L, Y = 0L;
    static Long Z;
    static Long answer = 1000000001L;

    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try {
            StringTokenizer st = new StringTokenizer(br.readLine());
            X = Long.parseLong(st.nextToken());
            Y = Long.parseLong(st.nextToken());
        } catch(IOException e) {}

        Z = (Y * 100) / X;
        if (Z == 100 || Z == 99) { //99는 올라갈 수 없음
            System.out.println(-1);
            return;
        }

        answer = X;
        Long start = 1L, end = X;
        Long mid = 0L, tmpZ = 0L;
        while (start<=end) {
            mid = ((start + end) / 2);
            tmpZ = ((Y+mid) * 100) / (X+mid);
            if (tmpZ != Z) {
                end = mid - 1;
                answer = Math.min(answer, mid);
            }
            else {
                start = mid + 1;
            }
        }
        System.out.println(answer);
        return;
    }
}