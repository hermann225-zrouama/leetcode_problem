//Definition for a binary tree node.
 function TreeNode(val) {
     this.val = val;
     this.left = this.right = null;
}
 
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var inorderTraversal = function(root,nodes = []) {
    if (root && root.left){
        inorderTraversal(root.left,nodes)
    }
    if(root != null){
        nodes.push(root.val)
    }
    if(root && root.right){
        inorderTraversal(root.right,nodes)
    }
    
    return nodes
};
