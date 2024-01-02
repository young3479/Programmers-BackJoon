def solution(n):
    answer = 0
    num = sorted(str(n), reverse = True)
    answer = int(''.join(num))
    return answer