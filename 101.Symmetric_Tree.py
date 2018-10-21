#! /usr/bin/python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.dfs_helper(root.left, root.right)
    
    def dfs_helper(self, n1, n2):
        if not n1 and not n2: return True
        if not n1 or not n2: return False
        if n1.val != n2.val: return False
        left = self.dfs_helper(n1.left, n2.right)
        right = self.dfs_helper(n1.right, n2.left)
        return left and right