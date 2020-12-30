# program to calculate solutions to the following puzzle:

# a x b - c = 5
# e / f + g = 7
# h + i - j = 9

# where a...j are 1...9. numbers can be moved around but not repeated.

times = 0


def solve_for(a):
    global times

    if len(a) == 9:
        times += 1
        # print(a)
        if a[0] * a[1] - a[2] == 5 and \
            a[3] / a[4] + a[5] == 7 and \
            a[6] + a[7] - a[8] == 9:
            print(f"One possible solution:")
            print(f"    {a[0]} * {a[1]} - {a[2]} = 5")
            print(f"    {a[3]} / {a[4]} + {a[5]} = 7")
            print(f"    {a[6]} + {a[7]} - {a[8]} = 9")
        return

    # if not there yet, move to the next
    # collect which numbers are not in the array, try them in sequence
    for x in range(1, 10):
        if x in a:
            continue
        a.append(x)
        solve_for(a)
        a.remove(x)



solve_for([])
print(f"Total {times} combinations")
