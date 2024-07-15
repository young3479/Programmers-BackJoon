class Solution {
    public int solution(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;
        
        int f0 = 0;
        int f1 = 1;
        int answer = 0;

        // F(2)부터 F(n)까지 계산
        for (int i = 2; i <= n; i++) {
            answer = (f0 + f1) % 1234567;  
            f0 = f1;  
            f1 = answer;  
        }

        // n번째 피보나치 수의 모듈로 1234567 결과 반환
        return answer;
    }
}