def func1(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    else:
        memo[n] = func1(n-1, memo) + func1(n-2, memo)
        return memo[n]
