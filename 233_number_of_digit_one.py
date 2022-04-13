"""
233. Number of Digit One
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.


Example 1:

Input: n = 13
Output: 6
Example 2:

Input: n = 0
Output: 0
"""

def one(num):
    i = 0
    ones = 0
    right_multiplier = 1
    right_remainder = 0
    while num:
        remainder = num % 10
        num = num // 10
        ones += num * right_multiplier

        if remainder==1 and i>0:
            ones += right_remainder + 1
        elif remainder>1:
            ones += right_multiplier

        i += 1
        right_remainder = remainder * right_multiplier + right_remainder
        right_multiplier *= 10
    return ones


print(one(13))
print(one(99))
print(one(6789))
print(one(6189))
print(one(6089))
