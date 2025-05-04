def solution() -> int:
    f_i = 1
    f_j = 2
    evens = [2]
    while True:
        n = f_j + f_i
        if n > 4_000_000:
            return sum(evens)
        if n % 2 == 0:
            evens.append(n)
        f_i = f_j
        f_j = n
