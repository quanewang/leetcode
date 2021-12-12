"""
42. Trapping Rain Water
Hard

15450

220

Add to List

Share
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.



Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
"""


def trap(a):
    height_i = 0
    height = 0
    for i in range(len(a)):
        if height<a[i]:
            height = a[i]
            height_i = i
    total = 0
    current_height = 0
    for i in range(0, height_i):
        if a[i]>current_height:
            current_height = a[i]
        total += min(current_height, height) - a[i]

    current_height = 0
    for i in range(len(a)-1, height_i, -1):
        if a[i]>current_height:
            current_height = a[i]
        total += min(current_height, height) - a[i]

    return total



print(trap([4,2,0,3,2,5]))
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))