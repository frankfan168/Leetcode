#! usr/bin/python
# -*- coding: utf-8 -*-

'''
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
'''

import sys
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0                            # it is a basic usage of binary search
        right = x
        while left <= right:
            mid = (left + right) // 2
            square = mid ** 2
            if square == x:
                return mid
            elif square > x:
                right = mid -1
            else:
                left = mid + 1
        return right
        

if __name__ == '__main__':
    x = int(sys.argv[1])
    print (Solution().mySqrt(x))