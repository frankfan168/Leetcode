#!/usr/bin/env python
# -*- coding: utf-8 -*

import sys
import json
import ast

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        maps = {}                              # Create one Dictionary to store key and value
        for i in range(len(nums)):
            if nums[i] in maps:         
                return maps[nums[i]], i        # as long as counterpart can be found in the dictionary, the previous position value is 1st output
            else:
                maps[target - nums[i]] = i     # Store the counterpart as key, the current position as value 
        return -1, -1 


if __name__ == '__main__':
#    nums = ast.literal_eval(sys.argv[1])      # one way to take a whole list as argument
     nums = json.loads(sys.argv[1])            # an elegant way to take a whole list as argument
#    nums = list(sys.argv[1])                  # Wrong! output is ['[', '2', ',', '7', ',', '1', '1', ',', '1', '5', ']']
     target = int(sys.argv[2])                  # take argument as 'int' instead of 'str'
     print (Solution().twoSum(nums, target))