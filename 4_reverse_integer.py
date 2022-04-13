"""
https://leetcode.com/problems/reverse-integer/
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            return -1 * self.reverse(-1*x)
        y = 0
        while x:
            y = y*10 + x%10
            x= x/10
            if y>pow(2, 31)-1:
                return 0
        return y