class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        res = []
        ans = []

        def dfs(node, ans, sums):

            if node is None:
                return

            sums += node.val
            ans.append(node.val)

            if sums == targetSum and node.left is None and node.right is None:
                res.append(ans.copy())
                ans.pop()
                return

            if node.left is None and node.right is None:
                ans.pop()
                return

            dfs(node.left, ans, sums)
            dfs(node.right, ans, sums)

            ans.pop()

        dfs(root, ans, 0)

        return res