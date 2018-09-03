#!usr/bin/python
# -*- coding: utf-8 -*

import sys
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """     
        if x < 0:                       # if number is negative, it should be False. Since -121 will become 321-.
            return False
        x = str(x)                      
        for i in range(len(x)):         
            if x[i] == x[len(x)-1-i]:   # no matter the length is odd or even
                continue
            return False
        return True

if __name__ == '__main__':
    x = int(sys.argv[1])
    print (Solution().isPalindrome(x))
    


        
            
        