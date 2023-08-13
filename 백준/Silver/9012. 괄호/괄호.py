T = int(input())
for _ in range(T):
    stack = []
    isVPS = True
    for char in input():
        if char == '(':
            stack.append(char) #여는 괄호 들어왔을 때 append
        else:
            if len(stack) > 0: #stack이 비어있는데 빼려고 하면 오류가 나버림
                stack.pop() #닫는 괄호 들어 왔을 때 stack의 상단의 값과 매칭하여 pop
            else:
                isVPS = False
                break
    if len(stack) > 0: #len(stack > 0)과 stack은 같은 표현
        isVPS = False
    print('YES' if isVPS else 'NO')
        
