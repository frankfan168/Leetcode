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
        p1, p2 = 0, -1
        while p1 < len(nums):
            if nums[p1] != val:
                p2 += 1
                nums[p2], nums[p1] = nums[p1], nums[p2]    #change the location of p1 and p2
            p1 += 1
        return p2 + 1

if __name__ == '__main__':
    nums = json.loads(sys.argv[1])
    val = int(sys.argv[2])
    print (Solution().removeElement(nums, val))