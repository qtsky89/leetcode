# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def smallest_node(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        '''
        1. if couldn't find,      => return base one => done

        2. find one, no childeren => just remove the target => 
        3. find one, one children => remove and children should be that position
        4. find one, two children => remove and one of children should be that position (prefer left one)
        '''

        if not root:
            return None
        
        if root.val == key:
            # 2. find one, no childeren => just remove the target => 
            if not root.left and not root.right:
                return None
            # 3. find one, one children => remove and children should be that position
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            # 4. find one, two children => remove and one of children should be that position (prefer right one)
            else:
                smallest_node = self.smallest_node(root.right)
                root.val = smallest_node.val
                root.right = self.deleteNode(root.right, smallest_node.val)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        
        return root


