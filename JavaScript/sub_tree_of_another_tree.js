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
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
var isSubtree = function(root, subRoot) {
    if(!subRoot) return true;
if(!root) return false;
if(isSameTree(root, subRoot) ) return true;
return isSubtree(root.right, subRoot) || isSubtree(root.left, subRoot)
};

var isSameTree = function(p, q) {
    if(!q && !p) return true;
if((!q || !p) || (q.val !== p.val)) return false;
return isSameTree(p.right, q.right) && isSameTree(p.left, q.left);



};