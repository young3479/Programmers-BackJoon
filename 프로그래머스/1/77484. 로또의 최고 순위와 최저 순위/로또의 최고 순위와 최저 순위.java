class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int max, min = 0;
		int zeroCount = 0;
		
		for (int lotto : lottos) {
			if (lotto == 0) {
				zeroCount++;  // 0일 zeroCount 증가
			} else { //lotto번호가 0이 아닐 때 
				for (int num : win_nums) { 
					if (lotto == num) {
						min++; //당첨 번호와 다면 min 증가 
						break;  
					}
				}
			}
		}
		max = min + zeroCount;
        // 등수 계산을 직접 메소드 안에서 처리
        int maxRank = (max == 0) ? 6 : 7 - max;
        int minRank = (min == 0) ? 6 : 7 - min;

        return new int[] {maxRank, minRank};
    }
}