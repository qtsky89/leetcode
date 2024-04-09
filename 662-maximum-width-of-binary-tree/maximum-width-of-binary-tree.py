# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([[root, 0, 0]])

        ret = []
        while q:
            item, level, index = q.popleft()
            if level == len(ret):
                ret.append([index])
            else:
                ret[level].append(index)
            
            if item.left:
                q.append([item.left, level+1, index*2])
            if item.right:
                q.append([item.right, level+1, index*2+1])
        
        max_width = 0
        for li in ret:
            if li:
                max_width = max(max_width, li[-1] - li[0]+1)
        return max_width
        