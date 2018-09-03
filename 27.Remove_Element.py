#!usr/bin/python
# -*- coding: utf-8 -*

import sys
import json

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in nums[:]:
            if i == val:
                nums.remove(val)
        return nums, len(nums)

if __name__ == '__main__':
    nums = json.loads(sys.argv[1])
    val = int(sys.argv[2])
    print (Solution().removeElement(nums, val))