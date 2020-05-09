def fib_rec(n):
    if n == 1 or n == 2:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)


def fib_dynmc(n, memo={}):
    if n == 1 or n == 2:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fib_dynmc(n-1, memo) + fib_dynmc(n-2, memo)
        memo[n] = result
        return result


#print("Rec Fib => ", fib_rec(15))
#print("Dyn Fib => ", fib_dynmc(15))
