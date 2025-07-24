def memo(fn):
    o = {}  # Cache dictionary

    def cb(n):
        if n not in o:
            o[n] = fn(n)  # Calls the memoized version of fib
        return o[n]  # Returns the cached value
    
    return cb

def fib(n: int):
    if n == 0:
        return 0  # Base case for fib(0)
    if n == 1:
        return 1  # Base case for fib(1)
    return memo_fib(n - 1) + memo_fib(n - 2)  # Use the memoized function here

memo_fib = memo(fib)  # Create memoized version
r = memo_fib(900)  # Now this will work correctly
print('Result for fib(900):', r)  # Output the result

def memoized_fib(n: int, cache={0: 0, 1: 1}) -> int:
    if n not in cache:
        cache[n] = memoized_fib(n - 1, cache) + memoized_fib(n - 2, cache)  # Store in cache
    return cache[n]  # Return the cached value

