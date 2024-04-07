# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        preorder = [3, 9, 20, 15, 7]
                    ^

        inorder = [9, 3, 15, 20, 7]
                      ^
                
                  9


        '''
        if not inorder:
            return None
        
        val = preorder.pop(0)
        node = TreeNode(val)

        index = inorder.index(val)

        node.left = self.buildTree(preorder, inorder[:index])
        node.right = self.buildTree(preorder, inorder[index+1:])

        return node