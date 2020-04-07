class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
Ce problème peut être facilement résolu en utilisant une méthode récursive.
Étant donné les listes inorder et postorder de l'arbre, ie inorder[1..n]et postorder[1..n], postorder[n]devrait être la valeur de la racine, alors nous trouvons la position de postorder[n] dans inorder[1..n]. Supposons que la position est i, alors postorder[1..i-1]et inorder[1..i-1]sont les listes post-ordre et in-ordre de l'arbre gauche de la racine et postorder[i..n-1]et inorder[i+1..n]sont les listes post-ordre et in-ordre de l'arbre droit de la racine. Nous pouvons donc construire l'arbre récursivement.
"""

class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        n = len(inorder)
        if n == 0:
            return None
        elif n == 1:
            return TreeNode(postorder[-1])
        else:
            root = TreeNode(postorder[-1])
            mid_inorder = inorder.index(postorder[-1])
            root.left = self.buildTree(inorder[:mid_inorder], postorder[:mid_inorder])
            root.right = self.buildTree(inorder[mid_inorder+1:], postorder[mid_inorder:-1])
            return root
            
            