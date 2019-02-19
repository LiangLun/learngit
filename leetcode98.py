# Validate Binary Search Tree

class Solution(object):
    def isValidBST(self, root):
        isValid(root, minval, maxval)
    def isValid(self, root, minval = None, maxval = None):
        if not root:
            return True
        if minval != None and root.val <= minval:
            return False
        if maxval != None and root.val >= maxval:
            return False
        return isValid(root.left, minval, root.val) and isValid(root.right, root.val, maxval)

class Solution(object):
    def isValidBST(self, root, lessThan = float('inf'), largerThan = float('-inf')):
        if not root:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            return False
        return self.isValidBST(root.left, min(lessThan, root.val), largerThan) and \
               self.isValidBST(root.right, lessThan, max(root.val, largerThan))
