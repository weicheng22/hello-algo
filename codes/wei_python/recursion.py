def recur(n:int) -> int:
    """递归"""
    if n == 1:
        return 1
    res = recur(n -1)
    return n + res

if __name__ == "__main__":
    print(recur(5))