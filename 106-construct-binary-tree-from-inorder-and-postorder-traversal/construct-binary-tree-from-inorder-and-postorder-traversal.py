class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_dict = {val: idx for idx, val in enumerate(inorder)}
        postorder.reverse()
        postorder_iter = iter(postorder)

        def helper(left, right):
            if left > right:
                return None

            root_val = next(postorder_iter)
            root = TreeNode(root_val)

            idx = inorder_dict[root_val]
            root.right = helper(idx + 1, right)
            root.left = helper(left, idx - 1)

            return root

        return helper(0, len(inorder) - 1)