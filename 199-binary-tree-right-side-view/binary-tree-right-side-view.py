# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # key: level, value: []
        ret = {}

        q = deque([[root, 0]])

        while q:
            item, cur_level = q.popleft()

            if cur_level in ret:            
                ret[cur_level].append(item.val)
            else:
                print(item, cur_level)
                ret[cur_level] = [item.val]

            if item.left:
                q.append([item.left, cur_level+1])
            
            if item.right:
                q.append([item.right, cur_level+1])
        

        ret_list = []

        for k in sorted(ret.keys()):
            ret_list.append(ret[k][-1])
        

        return ret_list

        