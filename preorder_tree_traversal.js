//Definition for a binary tree node.
 function TreeNode(val) {
     this.val = val;
     this.left = this.right = null;
}
 
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var preorderTraversal = function(root,nodes = []) {
    if(root!=null){
        nodes.push(root.val)
    }
    if (root && root.left){
        preorderTraversal(root.left,nodes)
    }
    
    if(root && root.right){
        preorderTraversal(root.right,nodes)
    }
    
    return nodes
};
