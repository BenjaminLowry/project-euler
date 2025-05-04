def solution() -> int:
    n = 20
    while True:
        if all([n % i == 0 for i in range(20, 1, -1)]):
            return n
        n += 20
