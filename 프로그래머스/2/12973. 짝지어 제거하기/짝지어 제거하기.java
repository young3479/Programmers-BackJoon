import java.util.ArrayDeque;
class Solution {
    public int solution(String s) {
        ArrayDeque<Character> stack = new ArrayDeque<>();
        char[] ch = s.toCharArray();
        
        for (char a : ch){
            if (!stack.isEmpty() && stack.peek() == a){
                stack.pop();
            } else {
                stack.push(a);
            }
        }
        return stack.isEmpty() ? 1 : 0;
    }
}