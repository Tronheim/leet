class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []

        if not root:
            return levels
        
        queue = [root]
        while queue:
            values = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if node:
                    values.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

            if values:
                levels.append(values)
            else:
                levels.append([])
        return levels
