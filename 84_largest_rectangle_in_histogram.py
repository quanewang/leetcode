"""
84. Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:

Input: heights = [2,4]
Output: 4
"""

def histogram(a):
    max_area = 0
    h = []
    for i in range(0, len(a)):
        if not h:
            h.insert(0, (i, a[i]))
        elif h[0][1]==a[i]:
            pass
        elif h[0][1] < a[i]:
            h.insert(0, (i, a[i]))
        else:
            last_i = h[0][0]
            while h and h[0][1] > a[i]:
              top = h.pop(0)
              area = (i-top[0]) * top[1]
              max_area = max(area, max_area)
              last_i = top[0]
            if not h or h[0][1]!=a[i]:
                h.insert(0, (last_i, a[i]))

    while h:
        top = h.pop(0)
        max_area = max(max_area, (len(a)-top[0])*top[1])
    return max_area


print(histogram([2,1,5,6,2,3]))
print(histogram([2,4]))