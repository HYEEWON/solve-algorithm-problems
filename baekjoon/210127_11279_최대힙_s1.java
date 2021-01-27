import java.io.*;
import java.util.*;

public class Main {
    static PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
    static int N = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        for (int i=0; i<N; ++i) {
            int x = Integer.parseInt(br.readLine());
            if (x==0) {
                if (maxHeap.size()<=0) System.out.println(0);
                else System.out.println(maxHeap.poll());
            }
            else {
                maxHeap.offer(x);
            }
        }
    }
}
