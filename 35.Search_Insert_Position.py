#! usr/bin/python
# -*- coding: utf-8 -*-

'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
'''

import sys
import json

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        for i in nums:
            if i >= target:
                return count
            else: 
                count += 1
        return len(nums)

if __name__ == '__main__':
    nums = json.loads(sys.argv[1])
    target = int(sys.argv[2])
    print (Solution().searchInsert(nums, target))