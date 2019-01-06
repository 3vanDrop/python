"""@fibonacci.py
*******************************************************************************
@Description:

        - Fibonacci sequence:

        Return value from Fibonacci seq from a given position 'n' - f(n)

@Author:
        -- 3van --

*******************************************************************************
"""

memo = {}
def fib_memo(n):
    """
    Memoized solution
    """
    if n == 0: return 0
    if n in memo.keys():
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:

        result = fib_memo(n-1) + fib_memo(n-2)
    memo[n] = result

    return result

def fib_bottom_up(n):
    """
    Bottom up solution
    """
    if n in [1,2]:
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]
