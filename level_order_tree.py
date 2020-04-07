# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        
        if root == None:
            return result
        
        queue = []
        queue.append(root)
        
        while queue:
            level_size = len(queue)
            level = []
            for i in range(0, level_size):
                node = queue.pop(0)
                level.append(node.val)
                
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            
            result.append(level)
                                    
        
        return result
