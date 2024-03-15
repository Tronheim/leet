class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []

        if not root:
            return levels

        queue = [root]
        order = True
        while queue:
            values = []
            temp = queue[:]
            queue = []

            for i in range(len(temp)):
                node = temp.pop(0)
                if node:
                    values.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)



            if values:
                if order:
                    levels.append(values)
                else:
                    levels.append(list(reversed(values)))
            else:
                levels.append([])

            order = not order

        return levels