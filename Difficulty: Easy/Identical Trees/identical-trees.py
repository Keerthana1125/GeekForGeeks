'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def inorderTraversal(self, root, arr):
        if not root:
            return arr
        self.inorderTraversal(root.left, arr)
        arr.append(root.data)
        self.inorderTraversal(root.right, arr)
        return arr

    def isIdentical(self, root1, root2):
        return self.inorderTraversal(root1, []) == self.inorderTraversal(root2, [])