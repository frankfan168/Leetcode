#! usr/bin/python
# -*- coding: utf-8 -*-

'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
'''

import sys

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) < 1:
            return 0
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
            

if __name__ == '__main__':
    haystack = str(sys.argv[1])
    needle = str(sys.argv[2])
    print (Solution().strStr(haystack, needle)) 
        
                