# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        preorder = 3, 9, 20, 15, 7
                   ^

        inorder =  9, 3, 15, 20, 7
                      ^
        '''

        if not inorder:
            return None
        
        val = preorder.pop(0)
        root = TreeNode(val)

        index = inorder.index(val)

        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index+1:])

        return root