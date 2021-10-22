
# typical textbook version
def fib1(n):
    if n == 0:
        return 0;
    if n == 1 or n == 2:
        return 1;
    return fib1(n-1) + fib1(n-2)


# memoization, calculating backwards, but skipping for numbers already calculated
fib2_memo = {}
def fib2(n):
    global fib2_memo
    if n in fib2_memo:
        return fib2_memo[n]

    if n == 0:
        f = 0
    elif n == 1 or n == 2:
        f = 1
    else:
        f = fib2(n-1) + fib2(n-2)

    fib2_memo[n] = f
    return f

# forward caclulation, O(n)
def fib3(n):
    steps = {}
    for step in range(n):
        if step == 0:
            steps[step] = 0
        elif step in [1,2]:
            steps[step] = 1
        else:
            steps[step] = steps[step-1] + steps[step-2]
    return steps[n-1] + steps[n-2]



# in this first version, anything beyond 35 seems to take many seconds, more than 10-15.
for f in [5, 10, 20, 30, 35]:
    print(f"Fib1({f}) is " + str(fib1(f)))

for f in [5, 10, 20, 30, 35, 40, 50, 75, 100]:
    print(f"Fib2({f}) is " + str(fib2(f)))

for f in [5, 10, 20, 30, 35, 40, 50, 75, 100]:
    print(f"Fib3({f}) is " + str(fib3(f)))


