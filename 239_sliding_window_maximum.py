"""
239. Sliding Window Maximum
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.



Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
Example 3:

Input: nums = [1,-1], k = 1
Output: [1,-1]
Example 4:

Input: nums = [9,11], k = 2
Output: [11]
Example 5:

Input: nums = [4,-2], k = 2
Output: [4]

"""


import heapq
class MaxHeap:

    def __init__(self):
        self.h = []

    def push(self, a):
        heapq.heappush(self.h, a * (-1))

    def pop(self):
        a = heapq.heappop(self.h)
        return a * (-1)

    def peek(self):
        if not self.h:
            return None
        a = self.pop()
        self.push(a)
        return a


def sliding(a, k):
    result = []
    h1 = MaxHeap()
    h2 = MaxHeap()
    for i in range(k):
        h1.push(a[i])
    top = h1.peek()
    result.append(top)
    for i in range(1, len(a)-k+1):
        top = h1.peek()
        if top==a[i-1]:
            h1.pop()
        else:
            h2.push(a[i-1])
        h1.push(a[i+k-1])

        top1 = h1.peek()
        top2 = h2.peek()
        while top1 is not None and top2 is not None and top1==top2:
            h1.pop()
            h2.pop()
            top1 = h1.peek()
            top2 = h2.peek()

        top = h1.peek()
        result.append(top)

    return result

print(sliding([1,3,-1,-3,5,3,6,7], 3))



