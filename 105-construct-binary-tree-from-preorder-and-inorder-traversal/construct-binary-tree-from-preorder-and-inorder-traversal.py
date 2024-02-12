# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        preorder
        inorder
        '''

        if not inorder:
            return None
        
        # root = 3
        root = TreeNode(preorder.pop(0))

        # inorder = [9] 3 [15 20 7]
                        
        i=0
        while i <= len(inorder)-1:
            if inorder[i] == root.val:
                break
            i+=1
        
        root.left = self.buildTree(preorder, inorder[:i])
        root.right = self.buildTree(preorder, inorder[i+1:])

        return root
        