import java.util.*;

public class 실패율_L2_210118 {
    public static int[] solution(int N, int[] stages) {
        float[][] answer = new float[N][2];
        Integer[] st = Arrays.stream(stages).boxed().toArray(Integer[]::new);
        int total = st.length;

        for (int n=1; n<=N; ++n) {
            answer[n-1][0] = n;
            int count = 0;
            for (int j=0; j< stages.length; ++j){
                if (stages[j] == n) count++;
            }
            if (total != 0) answer[n - 1][1] = (float) count / total;
            else answer[n - 1][1] = 0;
            total -= count;
        }
        Arrays.sort(answer, new Comparator<float[]>() {
            @Override
            public int compare(float[] o1, float[] o2) {
                if (o2[1] > o1[1]) return 1;
                else if (o2[1] == o1[1]) return 0;
                else return -1;
            }
        });
        int[] ret = new int[N];
        for (int i = 0; i < N; ++i) {
            ret[i] = (int)answer[i][0];
        }
        return ret;
    }

    public static void main(String[] args) {
        int N=5;
        int[] stages = {2, 1, 2, 6, 2, 4, 3, 3};
        System.out.println(Arrays.toString(solution(N, stages)));
    }
}
