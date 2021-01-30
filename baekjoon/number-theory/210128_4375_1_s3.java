import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String str = br.readLine();
            if (str == null || str.length() == 0) break;
            int n = Integer.parseInt(str);

            int tmp = 1; int cnt = 1;
            while (true) {
                if (tmp % n == 0) {
                    System.out.println(cnt);
                    break;
                }
                else {
                        tmp = (tmp*10) % n + 1;
                        cnt ++;
                }
            }
        }

    }
}
