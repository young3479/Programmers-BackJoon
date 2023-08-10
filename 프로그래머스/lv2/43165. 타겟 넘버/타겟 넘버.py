def solution(numbers, target):
    answer = 0
    current_sums = [0] #현재까지 가능한 숫자합 저장
    for num in numbers: #배열 하나씩 순회
        tmp = [] #현재 숫자(num)을 처리한 후 가능한 숫자 합을 임시로 저장
        for i in current_sums: #tmp에 num을 더하거나 뺀 결과로 가능한 모든 숫자합을 저장
            tmp.append(i + num)
            tmp.append(i - num)
        current_sums = tmp #tmp값을 current_sums로 갱신
    for sum in current_sums: #저장된 current_sums값에서 
        if sum == target: #합이 타겟넘버와 같은지 확인
            answer += 1 #같으면 answer 증가
    return answer
