def solution(s):
    stack = []
    for i in s: # s 길이만큼 for문 돌기
        if i == '(':# i가 ( 이면
            stack.append(i) # 스택에 push하기
        else: # i가 )이면 pop (단, empty가 아니어야함)
            if not stack: # empty이면 false
                return False
            stack.pop() # 스택에서 pop하기
    if stack: # 스택이 empty가 아니면 false
        return False
    return True