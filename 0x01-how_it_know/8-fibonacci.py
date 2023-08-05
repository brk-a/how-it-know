'''
implement using recursion

fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
fib(n) = fib (n-1) + fib(n-2)
fib(0) = 0 and fib(1) = fib(2) = 1
'''

# ============ method 1: recursion ============================================= #

def fib(n):
    """ get the nth number in the sequence"""
    if n<0:
        print("n must be greater than or equal to zero")
        return
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    return fib(n-1) + fib(n-2)

arr = [-1, 0, 1, 3, 5, 10, 20, 100 ]

print(f"uncomment lines 25 and 26 to experience the inefficiency of recursion")
# for i in arr:
#     print(f"n = {i}: fib({i}) = {fib(i)}")

# ============ method 2: memoisation ============================================ #

def fibMemo(n, memo={}):
    """ get the nth number in the sequence"""
    if n in memo.keys():
        return memo[n]
    if n<0:
        print("n must be greater than or equal to zero")
        return
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    memo[n] = fibMemo(n-1, memo) + fibMemo(n-2, memo)
    return memo[n]

print(f"Using memoisation...")
for i in arr:
    print(f"n = {i}: fibMemo({i}) = {fibMemo(i)}")

# ============ method 3: tabulation ============================================ #

def fibTab(n):
    """ get the nth number in the sequence"""
    if n<0:
        print("n must be greater than or equal to zero")
        return
    if n==0:
        return 0
    if n==1:
        return 1
    if n>=2:
        table = [0 for i in range(n+1)]
        table[1] = 1

        for i in range(2, n+1):
            table[i] = table[i-1] +  table[i-2]

    return table[n]

print(f"Using tabulation...")
for i in arr:
    print(f"n = {i}: fibTab({i}) = {fibTab(i)}")
    