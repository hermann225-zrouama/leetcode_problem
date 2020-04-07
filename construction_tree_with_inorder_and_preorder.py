class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        n = len(preorder)
        
        if n == 0:
            return None
        elif n == 1:
            return TreeNode(preorder[0])
        else:
            root = TreeNode(preorder[0])
            pos = inorder.index(preorder[0])
            root.left = self.buildTree(preorder[1:pos+1],inorder[:pos])
            root.right = self.buildTree(preorder[pos+1:],inorder[pos+1:])
            return root
