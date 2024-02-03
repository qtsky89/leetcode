# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _maxvalue(self, root: TreeNode) -> int:
        if root and root.right:
            return self._maxvalue(root.right)
        else:
            return root.val
    
    def _minvalue(self, root: TreeNode) -> int:
        if root and root.left:
            return self._minvalue(root.left)
        else:
            return root.val
        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        '''
            5
        3      6
    2     4        7

        case1. if that node has no child, just delete it!
        case2. if that node has only left child, swap left child's max value to that node
        case3. if that node has right child, swap right child's min value to that node
        case4. if that node has both childs, do that case2 or case3.
        '''

        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # case1. if that node has no child, just delete it!
            if not root.left and not root.right:
                return None
            # case2. if that node has only left child, swap left child's max value to that node
            elif root.left:
                root.val = self._maxvalue(root.left)
                root.left = self.deleteNode(root.left, root.val)
            else:
                root.val = self._minvalue(root.right)
                root.right = self.deleteNode(root.right, root.val)

        return root
