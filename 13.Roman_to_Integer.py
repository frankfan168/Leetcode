#!user/bin/python
# -*- coding: utf-8 -*

import sys
import json
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        maps = {'I': 1, 'V' : 5, 'X' : 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        results = 0
        for i in range(len(s)-1):
            if maps[s[i+1]] > maps[s[i]]:
                results = results - maps[s[i]]
            else:
                results = results + maps[s[i]]
        return results + maps[s[-1]]

if __name__ == '__main__':
    s = json.loads(sys.argv[1])
    print (Solution().romanToInt(s))