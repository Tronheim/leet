class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = [root.left, root.right]
        
        while queue:
            node = queue.pop(0)
            sym_node = queue.pop(0)

            if not node and not sym_node:
                continue
            if not node or not sym_node or node.val != sym_node.val:
                return False
            
            queue.append(node.left)
            queue.append(sym_node.right)
            queue.append(node.right)
            queue.append(sym_node.left)

        return True