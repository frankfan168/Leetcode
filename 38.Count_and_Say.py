#! /usr/bin/python
# -*- coding: utf-8 -*-

'''
The following are the terms from n=1 to n=10 of the count-and-say sequence:
 1.     1
 2.     11
 3.     21
 4.     1211
 5.     111221 
 6.     312211
 7.     13112221
 8.     1113213211
 9.     31131211131221
10.     13211311123113112211
'''

import sys

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        prev = "1"
        res = ""
        for i in range(1, n):
            count = 1
            for j in range(len(prev)-1):
                if prev[j] == prev[j+1]:
                    count += 1
                else:
                    res += str(count) + prev[j]
                    count = 1
            res += str(count) + prev[-1]
            prev = res
            res = ""
        return prev

if __name__ == '__main__':
    n = int(sys.argv[1])
    print (Solution().countAndSay(n))