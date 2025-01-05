#회의 일정 저장
N = int(input())
nums = []
for i in range(N):
    a, b = map(int, input().split())
    nums.append((a, b))

#시작시간 순 정렬 (회의시간이 긴 경우 최대한 많이 선택 못함)
#nums.sort(key=lambda x: min(x))
#print(nums)

#종료시간 순 정렬
nums.sort(key=lambda x: (x[1], x[0]))

count = 1
end = nums[0][1]
for i in range(1, N):
    if nums[i][0] >= end:
        end = nums[i][1]
        count += 1

print(count)