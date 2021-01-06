import java.util.*;

public class 오픈채팅방_L2_210106 {
    public static ArrayList<String> solution(String[] record) {
        ArrayList<String> answer = new ArrayList<>();
        Vector<String[]> v = new Vector <>();
        HashMap<String, String> map = new HashMap<>();

        for (int i = 0; i < record.length; ++i) {
            String[] s = record[i].split(" ");
            v.add(s);
            if (s.length > 2) map.put(s[1], s[2]);
        }

        for(String[] s : v){
            if (s[0].equals("Enter")) answer.add(map.get(s[1])+"님이 들어왔습니다.");
            else if (s[0].equals("Leave")) answer.add(map.get(s[1])+"님이 나갔습니다.");
        }
        return answer;
    }

    public static void main(String[] args) {
        String[] record = {"Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"};
        System.out.println(solution(record));
    }
}
