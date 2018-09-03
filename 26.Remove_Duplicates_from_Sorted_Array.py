#!usr/bin/python
# -*- coding: utf-8 -*


import sys
import json

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        pos = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[pos] = nums[i]
                pos += 1
        return pos

if __name__ == '__main__':
     nums = json.loads(sys.argv[1])            
     print (nums[:Solution().removeDuplicates(nums)])    #print out nums list with length pos