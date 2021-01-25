import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
    static int[][] city;
    static ArrayList<Position> chickens = new ArrayList<>();
    static ArrayList<Position> houses = new ArrayList<>();
    static int[] select;
    static int N = 0, M = 0;
    static int totalMinDist = 0;

    static class Position {
        int x;
        int y;
        public Position(int y, int x){
            this.y = y;
            this.x = x;
        }
    }

    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try {
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            city = new int[N][N];
            for (int i=0; i<N; ++i) {
                st = new StringTokenizer(br.readLine());
                for (int j=0; j<N; ++j) {
                    city[i][j] = Integer.parseInt(st.nextToken());
                    if (city[i][j] == 1) houses.add(new Position(i, j));
                    else if (city[i][j] == 2) chickens.add(new Position(i, j));
                }
            }
        } catch (IOException e) { }
        select = new int[chickens.size()];
        for (int i=0; i<select.length; ++i) {
            select[i] = 0;
        }

        backtracking(0, 0);

        System.out.println(totalMinDist);
        return;
    }

    public static void backtracking(int idx, int cnt) {
        if (cnt == M) { //종료조건
            calcDist(); //거리 계산
            return;
        }
        for (int i=idx; i<select.length; ++i) {
            if (select[i] == 0){
                select[i] = 1;
                backtracking(i, cnt+1);
                select[i] = 0;
            }
        }
    }

    public static void calcDist() {
        int total = 0;
        for (Position house : houses) {
            int minDist = N*N;
            for (int i=0; i< select.length; ++i) {
                if (select[i] == 0) continue;
                minDist = Math.min(minDist, Math.abs(house.x-chickens.get(i).x)+Math.abs(house.y-chickens.get(i).y));
            }
            total += minDist;
        }
        if (totalMinDist == 0) totalMinDist = total;
        totalMinDist = Math.min(totalMinDist, total);
    }
}