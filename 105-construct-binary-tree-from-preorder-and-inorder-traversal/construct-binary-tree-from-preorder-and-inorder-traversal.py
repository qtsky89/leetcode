# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        example1.
        '''

        if not inorder:
            return None

        # root
        node = TreeNode(preorder.pop(0))

        # find that value in inorder
        index = 0
        for i in range(len(inorder)):
            if inorder[i] == node.val:
                index = i
                break

        node.left = self.buildTree(preorder, inorder[:index])
        node.right = self.buildTree(preorder, inorder[index+1:])

        return node

        