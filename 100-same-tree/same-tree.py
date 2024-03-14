# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            if not p and not q:
                return True
            return False

        queue = [(p, q)]
        while queue:
            node_p, node_q = queue.pop(0)
            if node_p.val != node_q.val:
                return False

            if node_p.left and node_q.left:
                queue.append((node_p.left, node_q.left))
            if node_p.left and not node_q.left:
                return False
            if not node_p.left and node_q.left:
                return False
            if node_p.right and node_q.right:
                queue.append((node_p.right, node_q.right))
            if node_p.right and not node_q.right:
                return False
            if not node_p.right and node_q.right:
                return False
        return True
        
        return True
