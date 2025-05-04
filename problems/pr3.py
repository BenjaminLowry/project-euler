
def solution() -> int:
    n = 600851475143
    f = 2
    while n != 1:
        if n % f == 0:
            n = n / f
        else:
            f += 1
    return f
