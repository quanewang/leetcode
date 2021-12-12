"""
416. Partition Equal Subset Sum
Medium

6282

102

Add to List

Share
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.



Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""


def partition(a, i=0, p=[]):
    if i>=len(a):
        return check(a, p)
    r1 = partition(a, i+1, p)
    if r1:
        return r1
    else:
        p.append(a[i])
        r2 = partition(a, i+1, p)
        p.remove(a[i])
        return r2


def check(a, p):
    total = 0
    for x in a:
        total += x
    p_total = 0
    for x in p:
        p_total += x
    if total == p_total + p_total:
        print(p)
        return True
    return False


print(partition([1, 5, 11, 5]))