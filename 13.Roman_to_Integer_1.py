#! usr/bin/python
# -*- coding: utf-8 -*-

import sys

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        maps = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}       # ' ' is a must to add, be careful
        for i in range(len(s)-1):
             if maps[s[i]] >= maps[s[i+1]]:
                 sum += maps[s[i]]
             else:
                 sum -= maps[s[i]]
        return (sum + maps[s[-1]])

if __name__ == '__main__':
    s = str(sys.argv[1])
    print (Solution().romanToInt(s))
        
        
        

            
            
            
            