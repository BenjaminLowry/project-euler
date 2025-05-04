def solution() -> int:
    products = [i * j for i in range(100, 1000) for j in range(100, 1000) if i <= j]
    products.sort()
    products.reverse()
    for p in products:
        if num_is_palindrome(p):
            return p


def num_is_palindrome(n: int) -> bool:
    n_s = str(n)
    l = len(n_s)
    chars = [c for c in n_s]
    chars2 = chars.copy()
    chars2.reverse()
    return chars == chars2
