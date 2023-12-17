def recur(n: int) -> int:
    """recursion function"""
    # the base case
    if n == 1:
        return 1
    # the recursive case
    else:
        res = recur(n - 1)
        return n + res


def tail_recur(n: int, res: int = 0) -> int:
    """tail recursion function"""
    # the base case
    if n == 0:
        return res
    # the recursive case
    else:
        return tail_recur(n - 1, n + res)


if __name__ == "__main__":
    n = 5
    print(f"\nThe results of recursion function res = {recur(n)}")

    print(f'\nThe results of tail recursion function res = {tail_recur(n)}')
