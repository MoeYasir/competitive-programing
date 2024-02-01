/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function(root) {
    var maxRight;
    var maxLeft;
    var maxLength = 0;
    if(!root) return 0;
    
    maxRight = maxDepth(root.right);
        maxLeft = maxDepth(root.left);

    maxLength = Math.max(maxLeft, maxRight) + 1;
    
    
    
    return maxLength;
};

//pass right and left to maxDepth
// minCount -- maxCount =>