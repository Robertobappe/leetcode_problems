class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None

        root.right, root.left = root.left, root.right
        self.invertTree(root.right)
        self.invertTree(root.left)

        return root


root1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
root2 = TreeNode(2, TreeNode(1), TreeNode(3))

for i in [root1, root2]:
    s = Solution()
    print(s.invertTree(i))
