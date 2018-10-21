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

def countAndSayHelper(s, k, i, sLength):
    if(i == sLength - 1):              #if end of string
        return(str(k) + s[i])
    elif(s[i] == s[i + 1]):           #if next char in string is equal to current char
        return(countAndSayHelper(s, k+1, i + 1, sLength))
    else:                             #if next char in string is diff to current char
        return(str(k) + s[i] + countAndSayHelper(s, 1, i + 1, sLength))
    

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        while(n > 1):
            sLength = len(s)
            s = countAndSayHelper(s, 1, 0, sLength)
            n -= 1
        return s


if __name__ == '__main__':
    n = int(sys.argv[1])
    print (Solution().countAndSay(n))