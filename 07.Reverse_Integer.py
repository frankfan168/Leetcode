#!usr/bin/python
# -*- coding: utf-8 -*

import sys
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        y = abs(x)                         # the reason to have absolute value of x is: if x < 0, in the end y //=10 will become -1, not 0
        while y != 0:
            pop = y % 10                   # take the last digit of y each time
            y //= 10                       # exact division of y
            rev = rev * 10 + pop           # reverse the order
        if x >= 0 and rev <= 2**31-1:
            return rev
        elif x < 0 and (-rev) >= -2**31:
            return -rev
        else:
            return 0


if __name__ == '__main__':
    x = int(sys.argv[1])                   # take first argument as int
    print (Solution().reverse(x))
    