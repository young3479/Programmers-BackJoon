# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
input = sys.stdin.readline
T = int(input())
answer = []
for i in range (T):
	a, cal, b = input().split()
	a = int(a)
	b = int(b)
	if cal == '+':
		result = a + b
	elif cal == '-':
		result = a - b
	elif cal == '/':
		result = a // b
	elif cal == '*':
		result = a * b
	else:
		print("올바르지 않은 계산식 입니다.")
		continue
	answer.append(result)
sum_answer = sum(answer)
print(sum_answer)