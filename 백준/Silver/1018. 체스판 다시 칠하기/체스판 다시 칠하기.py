N, M = map(int, input().split())

map = []

for i in range(N):
    row = list(input())  # 한 줄 입력을 한 글자씩 리스트로 변환
    map.append(row)

min_count = float('inf')

for start_row in range(N - 7):  # 가능한 시작 행
    for start_col in range(M - 7):  # 가능한 시작 열
        count1 = 0  # 시작점이 'W'일 때
        count2 = 0  # 시작점이 'B'일 때

        # 8x8 영역 탐색
        for i in range(start_row, start_row + 8):
            for j in range(start_col, start_col + 8):
                if (i + j) % 2 == 0:  # 짝수 칸
                    if map[i][j] != 'W':  # 'W'가 아니면 색칠 필요
                        count1 += 1
                    if map[i][j] != 'B':  # 'B'가 아니면 색칠 필요
                        count2 += 1
                else:  # 홀수 칸
                    if map[i][j] != 'B':  # 'B'가 아니면 색칠 필요
                        count1 += 1
                    if map[i][j] != 'W':  # 'W'가 아니면 색칠 필요
                        count2 += 1

        # 최소값 갱신
        min_count = min(min_count, count1, count2)

print(min_count)
