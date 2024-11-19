# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        temp = deque([root])
        result = []
        while temp:
            size = len(temp)
            for i in range(size):
                curr = temp.popleft()
                if i == size-1:
                    result.append(curr.val)
                if curr.left:
                    temp.append(curr.left)
                if curr.right:
                    temp.append(curr.right)
        return result
        
