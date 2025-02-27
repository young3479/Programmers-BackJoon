import java.util.*;

class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        //System.out.print(Arrays.toString(numbers));
        answer = Arrays.stream(numbers).sum();
        answer = answer / numbers.length;
        return answer;
    }
}