from collections import deque

N = int(input())
dq = deque()
for i in range(1, N+1): #1부터 N+1까지
    dq.append(i)
while len(dq) > 1: 
    dq.popleft() #맨 앞에 있는 값을 빼서 버림
    dq.append(dq.popleft()) #맨 앞에 있는 값을 dq 마지막에 추가        
print(dq[0]) #마지막 dq의 값을 출력