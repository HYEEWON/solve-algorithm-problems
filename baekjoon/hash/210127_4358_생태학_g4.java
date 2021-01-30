import java.io.*;
import java.util.*;

public class Main {
    static TreeMap<String, Integer> countTree = new TreeMap<>();
    static int cnt = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String str =br.readLine();
            if (str == null || str.length() == 0) break;
            countTree.put(str, countTree.getOrDefault(str, 0)+1);
            cnt++;
        }

        String[] keys = countTree.keySet().toArray(new String[0]);
        for (String key: keys) {
            double ratio = (double) countTree.get(key) * 100 / cnt;
            System.out.println(key+" "+String.format("%.4f", ratio));
        }
    }
}
