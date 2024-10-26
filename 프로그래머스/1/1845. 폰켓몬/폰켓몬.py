def solution(nums):
    n = len(nums)//2 #총 기회
    nums = set(nums)
    sn = len(nums) #다 다른 포켓몬 개수
    answer = 0
    if n <= sn:
        answer = n
    else:
        answer = sn
    return answer