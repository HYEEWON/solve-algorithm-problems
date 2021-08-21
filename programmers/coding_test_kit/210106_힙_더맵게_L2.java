import java.util.Collections;
import java.util.PriorityQueue;

public class 힙_더맵게_L2_210106 {
    public static int solution(int[] scoville, int K) {
        int answer = 0;
        // 최소 힙
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        // 최대 힙
        //PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int s : pq) System.out.println(s);
        while (pq.peek() <= K){
            if (pq.size() < 2) return -1;
            int newInt = pq.poll() + 2 * pq.poll();
            pq.offer(newInt);
            answer++;
        }
        return answer;
    }

    public static void main(String[] args) {
        int [] scoville = {1, 2, 3, 9, 10, 12};
        int K = 7;
        System.out.println(solution(scoville, K));
    }
}
