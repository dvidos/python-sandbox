# from here: https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/3jEPRo5PDvx#
# Dynamic Programming
# the idea is to solve recursively, 
# then with memoization (i.e. store results of already solved sub-problems), 
# then tabulation (i.e. from the bottom up)

# current problem: 
# Given a set of positive numbers, find if we can partition it into two subsets 
# such that the sum of elements in both the subsets is equal.

# Input: {1, 2, 3, 4}
# Output: True
# Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}


def can_v2_try(nums, target, s, index):
    if index >= len(nums):
        return False

    print(f"   can_v2_try(set={s}, index={index})")

    # try adding the starting num in the sum
    total = sum(s)
    if total == target:
        return True

    # if sum is smaller, include and recurse deeper
    if total + nums[index] <= target:
        s.append(nums[index])
        got_it = can_v2_try(nums, target, s, index + 1)
        s.remove(nums[index])
        if got_it:
            return True
    
    # else, skip this nubmer, and continue recursing
    return can_v2_try(nums, target, s, index + 1)
    
def can_v2(nums):
    s = sum(nums)
    if s % 2:
        return False
    target = s / 2
    print(f"  Looking for {target}")
    return can_v2_try(nums, target, [], 0)

def can_partition(nums):
    # return can_recursively(nums, [], 0, [], 0, 0)
    return can_v2(nums)

def test(nums, expected):
    print(f"Testing {nums}...")
    result = can_partition(nums)
    if result == expected:
        print("Correct!")
    else:
        print(f"Failed, expected {expected}, gotten {result}")

test([1, 2, 3, 4], True)
test([1, 1, 3, 4, 7], True)
test([2, 3, 4, 6], False)
test([2, 3, 9, 6], False)


# correct implementation, but very bloated.
def can_recursively_v1(nums, set1, sum1, set2, sum2, index):

    # solve for finish
    if index >= len(nums):
        return False

    # solve for base cases
    if sum1 + nums[index] == sum2 and index == len(nums) - 1: 
        set1.append(nums[index])
        sum1 += nums[index]
        print(f"Found it: set1={set1}, set2={set2}");
        return True
    if sum2 + nums[index] == sum1 and index == len(nums) - 1: 
        set2.append(nums[index])
        sum2 += nums[index]
        print(f"Found it: set1={set1}, set2={set2}");
        return True

    # try one way, then the other
    set1.append(nums[index])
    sum1 += nums[index]
    print(f"    Trying: {set1}, {set2}")
    if can_recursively(nums, set1, sum1, set2, sum2, index + 1):
        return True
    set1.remove(nums[index])
    sum1 -= nums[index]
    
    # then the other
    set2.append(nums[index])
    sum2 += nums[index]
    print(f"    Trying: {set1}, {set2}")
    if can_recursively(nums, set1, sum1, set2, sum2, index + 1):
        return True
    set2.remove(nums[index])
    sum2 -= nums[index]

    # all these attempts failed
    return False



