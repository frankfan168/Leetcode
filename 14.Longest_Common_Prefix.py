#!usr/bin/python
# -*- coding: utf-8 -*

import sys
import json
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:                               #if strs is blank
            return ""
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):          #sample: [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest

if __name__ == '__main__':
    strs = json.loads(sys.argv[1])
    print (Solution().longestCommonPrefix(strs))

#Run CMD: python 14.Longest_Common_Prefix.py \[\"flower\",\"flow\",\"flight\"\]
#regarding the input, '\' must be added as an escape character
    