# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.list = []
        self.p = 0

        def dfs(node: TreeNode) -> None:
            if not node:
                return
            
            dfs(node.left)
            self.list.append(node.val)
            dfs(node.right)
        
        dfs(root)


    def next(self) -> int:
        tmp = self.list[self.p]
        self.p += 1
        return tmp
        

    def hasNext(self) -> bool:
        if self.p <= len(self.list)-1:
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()