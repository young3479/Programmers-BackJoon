def solution(brown, yellow):
    total = brown + yellow
    for b in range(1, total + 1):
        quotient, remainder = divmod(total, b)
        if remainder == 0:
            a = quotient
            if a >= b and (2 * a) + (2 * b) == brown + 4:
                return [a, b]

