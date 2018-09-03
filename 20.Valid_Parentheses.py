#!usr/bin/python
# -*- coding: utf-8 -*

import sys

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        maps = {'(':')', '[':']', '{':'}'}
        for i in s:
            if i in maps.keys():
                stack.append(maps[i])
            elif stack == [] or stack.pop() != i:
                return False
        return not stack

if __name__ == '__main__':
    s = sys.argv[1]
    print (type(s))
    print (Solution().isValid(s))    

#Run: python 20.Valid_Parentheses.py "()"            