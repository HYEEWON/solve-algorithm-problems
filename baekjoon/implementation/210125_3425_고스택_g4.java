import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.*;
public class Main {

    static ArrayList<String> operations = new ArrayList<>();
    static ArrayList<Long> numbers = new ArrayList<>();

    static Stack<Long> stack = new Stack<>();
    static int N = 0;

    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            try {
                while (true) {
                    String op = null;
                    long num = 0;
                    op = br.readLine();
                    if (op.equals("QUIT")) return;
                    else if (op.equals("END")) {
                        N = Integer.parseInt(br.readLine());
                        break;
                    }
                    else if(op.equals("")){
                        operations.clear();
                        numbers.clear();
                        stack.clear();
                        System.out.println();
                        continue;
                    }
                    if (op.length() > 3) {
                        String[] s = op.split(" ");
                        op = s[0];
                        num = Integer.parseInt(s[1]);
                    }
                    operations.add(op);
                    numbers.add(num);
                }
            } catch (IOException e) {}
            for(int i = 0; i < N; ++i) {
                long n = 0;
                try {
                    n = Integer.parseInt(br.readLine());
                } catch (IOException e) {}
                stack.add(n);
                int result = calculation();
                if (result == -1 || stack.size() != 1) System.out.println("ERROR");
                else System.out.println(stack.peek());
                stack.clear();
            }

        }

    }

    public static Integer calculation() {
        for (int i = 0; i < operations.size(); ++i) {
            String op = operations.get(i);
            long first = 0, second = 0;

            if (op.equals("NUM")) {
                stack.push(numbers.get(i));
                continue;
            } else if (op.equals("DUP")) {
                stack.push(stack.peek());
                continue;
            } else if (op.equals("POP")) {
                if (stack.size() < 1) return -1;
                stack.pop();
                continue;
            } else if (op.equals("INV")) {
                if (stack.size() < 1) return -1;
                long top = stack.pop();
                stack.push(-top);
                continue;
            } else if (op.equals("SWP")) {
                first = stack.pop();
                second = stack.pop();
                stack.push(first);
                stack.push(second);
                continue;
            }

            if (stack.size() < 2) return -1;
            first = stack.pop();
            second = stack.pop();
            long result = 0;
            if (op.equals("ADD")) {
                result = first + second;
            } else if (op.equals("SUB")) {
                result = second - first;
            } else if (op.equals("MUL")) {
                result = first * second;
            } else if (op.equals("DIV")) {
                if (first == 0) return -1;
                result = Math.abs(second) / Math.abs(first);
                int cnt = 0;
                if (first < 0) cnt++;
                if (second<0) cnt++;
                if (cnt==1) result = -result;
            } else if (op.equals("MOD")) {
                if (first == 0) return -1;
                result = Math.abs(second) % Math.abs(first);
                if (second<0) result = -result;
            }

            if (result > 1000000000 || result < -1000000000)
                return -1;
            stack.push(result);
        }
        return 1;
    }
}
