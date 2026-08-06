# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        
        #Creates the partition needed to identify the nodes that
        #belong to left and right subtrees
        mid = inorder.index(preorder[0])

        #everything until mid belongs to the left subtree
        #we take the preorder subarray accordingly
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])

        #everything after the mid index belongs to the right subtree
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root




            
