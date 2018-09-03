#!usr/bin/python
# -*- coding: utf-8 -*


import sys
import json
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack = []
        while l1 != None:
            stack.append(l1.val)
            l1 = l1.next
        while l2 != None:
            stack.append(l2.val)
            l2 = l2.next
        return sorted(stack)
