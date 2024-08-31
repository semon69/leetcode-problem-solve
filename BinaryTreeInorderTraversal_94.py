# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        result = []
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            
            result.append(node.val)
            
            dfs(node.right)

        dfs(root)
        return result

# Example usage:
# The code below is for testing and not part of the online judge submission.
if __name__ == "__main__":
    # Construct the example tree for testing
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(6)
    root.left.right.right = TreeNode(7)
    root.right.right.left = TreeNode(9)

    # Creating an instance of Solution to call the method
    solution = Solution()
    output = solution.inorderTraversal(root)
    print(output)  # Expected Output: [4, 2, 6, 5, 7, 1, 3, 9, 8]
