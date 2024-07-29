import java.util.HashMap;
class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        HashMap<String, Integer> wantMap = new HashMap<>(); 

        for (int i = 0; i < want.length; i++) {
            wantMap.put(want[i], number[i]);
        }
        
        int answer = 0;
        // discount 배열을 10일씩 구간으로 나누어 검사
        for (int j = 0; j <= discount.length - 10; j++) {
            // 각 구간마다 원본 wantMap을 복사
            HashMap<String, Integer> tempMap = new HashMap<>();
            
            // 현재 구간에서 아이템의 수를 줄임
            for (int k = j; k < j + 10; k++) {
                 if (wantMap.containsKey(discount[k])) {
                    tempMap.put(discount[k], tempMap.getOrDefault(discount[k], 0) + 1);
                }
            }
            
            if (tempMap.equals(wantMap))
                answer++;
        }
        return answer;
    }
}