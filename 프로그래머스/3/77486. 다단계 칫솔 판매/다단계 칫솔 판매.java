import java.util.HashMap;

public class Solution {

    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        // 판매원 이름과 추천인 이름 담을 해시맵
        HashMap<String, String> parent = new HashMap<>();
        for (int i = 0; i < enroll.length; i++) {
            parent.put(enroll[i], referral[i]);
        }
        // 자신의 총 판매 금액 담을 해시맵
        HashMap<String, Integer> total = new HashMap<>();

        //seller 배열과 amount 배열을 이용하여 이익 분배
        for (int i = 0; i < seller.length; i++) {
            String curName = seller[i]; // 현재 판매자 
            int money = amount[i] * 100; // 판매자가 판매한 총 금액 계산
            while (money > 0 && !curName.equals("-")) { //추천인(부모) 더 없을때까지 반복
                // 현재 판매자가 받을 금액 계산(10%를 제외한 금액)
                total.put(curName, total.getOrDefault(curName, 0) + money - (money / 10));
                curName = parent.get(curName); // 부모로 curName 갱신
                money /= 10; // 부모 돈 갱신(10퍼)
            }
        }

        // enroll 배열의 모든 노드에 대해 해당하는 이익을 배열로 반환
        int[] answer = new int[enroll.length];
        for (int i = 0; i < enroll.length; i++) {
            answer[i] = total.getOrDefault(enroll[i], 0);
        }
        return answer;
    }

}