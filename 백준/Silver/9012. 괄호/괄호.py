T = int(input()) #입력 개수 나타내는 정수 T
for _ in range(T): #T번 반복
    stk = [] #스택 설정
    isVPS = True
    for ch in input(): #문자를 input()이 되는동안 반복문
        if ch == '(': #(이면 append
            stk.append(ch) #(를 stk에 삽입
        else: #)이면 pop (단, 스택이 비어있지 않아야 함)
            if len(stk) > 0:
                stk.pop()
            else:
                isVPS = False
                break
    if len(stk) > 0:
        isVPS = False
    print('YES' if isVPS else 'NO')