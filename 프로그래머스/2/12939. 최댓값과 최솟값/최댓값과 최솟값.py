def solution(s):
    s1 = list(map(int, s.split())) #s를 공백 기준 잘라서 int형 리스트
    minnum = min(s1) #가장 작은 수
    maxnum = max(s1) #가장 큰 수
    return f"{minnum} {maxnum}"