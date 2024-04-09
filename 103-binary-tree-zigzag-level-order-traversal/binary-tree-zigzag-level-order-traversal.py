# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([[root, 0]])

        ret = []
        while q:
            node, height = q.popleft()
            
            if len(ret) == height:
                ret.append([node.val])
            else:
                ret[height].append(node.val)
            
            if node.left:
                q.append([node.left, height+1])
            if node.right:
                q.append([node.right, height+1])

        for i in range(len(ret)):
            if i %2 != 0:
                ret[i] = ret[i][::-1]

        return ret
