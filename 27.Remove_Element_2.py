#! usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json    

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        a, b = 1, 0
        while a <= len(nums):
            if nums[a-1] != val:
                nums[a-1], nums[b] = nums[b], nums[a-1]  # this one beats 99.76%
                b += 1
            a +=1
        return b 

if __name__ == '__main__':
    nums = json.loads(sys.argv[1])
    val = int(sys.argv[2])
    print (Solution().removeElement(nums, val))
            
            
        
                
                
                

            
            
            
            