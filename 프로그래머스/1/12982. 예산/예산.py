#오름차순
def solution(d, budget):
    answer = 0
    d.sort()
    for de in d:
        budget -= de
        if budget >= 0:
            answer += 1
        else:
            break
    return answer