class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_dict = {val: idx for idx, val in enumerate(inorder)}
        preorder_iter = iter(preorder)

        def helper(left, right):
            if left > right:
                return None

            root_val = next(preorder_iter)
            root = TreeNode(root_val)

            idx = inorder_dict[root_val]
            root.left = helper(left, idx - 1)
            root.right = helper(idx + 1, right)

            return root

        return helper(0, len(inorder) - 1)