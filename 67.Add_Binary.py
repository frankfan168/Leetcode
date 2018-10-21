#! usr/bin/python
# -*- coding:utf-8 -*-

'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
'''

import sys

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return str(bin(int(a, 2) + int(b, 2)))[2:]   # exclude the first two string '0b'
        
if __name__ == '__main__':
    a = str(sys.argv[1])
    b = str(sys.argv[2])
    print (Solution().addBinary(a, b))