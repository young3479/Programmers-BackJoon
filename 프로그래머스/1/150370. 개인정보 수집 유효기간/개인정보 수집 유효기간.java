import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        // terms저장할 해시맵 생성
        Map<String, Integer> termsMap = new HashMap<>();
        
        // 오늘 날짜를 LocalDate 형식으로 변환
        LocalDate todayDate = LocalDate.parse(today, DateTimeFormatter.ofPattern("yyyy.MM.dd"));
        
        //파괴해야할 개인정보 번호
        List<Integer> end = new ArrayList<>();

        // 약관과 기간을 해시맵에 저장
        for (String term : terms) {
            String[] type = term.split("\\s"); // type[0]은 약관 종류, type[1]은 유효기간
            termsMap.put(type[0], Integer.parseInt(type[1])); // 약관 종류와 유효기간을 매핑
        }
        
        // 비교해야 할 개인정보들
        for (int i = 0; i < privacies.length; i++) {
            String[] personal = privacies[i].split("\\s"); // personal[0]은 가입 날짜, personal[1]은 약관 종류
            // 개인정보 약관의 유효기간을 해시맵에서 찾기
            if (termsMap.containsKey(personal[1])) {
                int months = termsMap.get(personal[1]);
                //personal[0]을 날짜로 파싱
                LocalDate personalDate = LocalDate.parse(personal[0], DateTimeFormatter.ofPattern("yyyy.MM.dd"));
                LocalDate endDate = personalDate.plusMonths(months).minusDays(1);

                // 유효기간이 지났는지 확인
                if (endDate.isBefore(todayDate)) {
                    end.add(i + 1); // 인덱스니까 +1
                }
            }
        }

        int[] answer = end.stream().mapToInt(Integer::intValue).toArray();
        return answer;
    }
}
