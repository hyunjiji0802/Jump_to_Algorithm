def solution(n):
    for i in range(2, n + 1):
        if n % i == 1:
            return i
    else:
        return n