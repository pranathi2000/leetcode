# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if (not p and q) or (not q and p):
            return False
        queueP = [p]
        queueQ = [q]

        while queueP and queueQ:
            pVal = queueP.pop(0)
            qVal = queueQ.pop(0)
            if pVal.val != qVal.val:
                return False
            if pVal.right and qVal.right:
                queueP.append(pVal.right)
                queueQ.append(qVal.right)
            elif (pVal.right == None and qVal.right != None) or (pVal.right != None and qVal.right == None):
                return False
            if pVal.left and qVal.left:
                queueP.append(pVal.left)
                queueQ.append(qVal.left)
            elif (pVal.left != None and qVal.left == None) or (pVal.left == None and qVal.left != None):
                return False


        if queueP or queueQ:
            return False
        return True
