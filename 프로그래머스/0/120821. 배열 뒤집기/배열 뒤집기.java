class Solution {
    public int[] solution(int[] num_list) {
        // 1. 값이 존재하는 배열과 새로 넣으려는 배열을 선언
        int[] result = new int[num_list.length];

        // 2. arr를 앞뒤로 뒤집음
        for (int i = num_list.length; i > 0; i--) {
            result[num_list.length - i] = num_list[i - 1];
        }
        return result;
    }
}