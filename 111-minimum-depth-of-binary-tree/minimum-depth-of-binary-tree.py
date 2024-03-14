class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        level = 0

        if not root:
            return level
        else:
            queue = [root]
            while queue:
                level += 1
                for i in range(len(queue)):
                    node = queue.pop(0)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    if not node.left and not node.right:
                        return level
        
        return level