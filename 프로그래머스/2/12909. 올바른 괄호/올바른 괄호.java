import java.util.ArrayDeque;
class Solution {
    boolean solution(String s) {
        ArrayDeque<Character> stack = new ArrayDeque<>();
        char[] ch = s.toCharArray();
        
        for (char a : ch){
            if(a == '('){
                stack.push(a);
            } else {
                if(stack.isEmpty()){
                    return false;
                }
                stack.pop();
            }
        }
        return stack.isEmpty();
    }
}