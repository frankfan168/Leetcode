#! /usr/bin/python
# -*- coding: utf-8 -*-

'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
'''

import sys

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s.strip()) == 0:
            return 0
        return len(s.split()[-1])
        
if __name__ == '__main__':
    s = str(sys.argv[1])
    print (Solution().lengthOfLastWord(s))