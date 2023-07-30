# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # key: level, value: []
        ret = defaultdict(list)

        q = deque([[root, 0]])

        while q:
            item, cur_level = q.popleft()

            if not item:
                continue
            
            ret[cur_level].append(item.val)

            if item.left:
                q.append([item.left, cur_level+1])
            
            if item.right:
                q.append([item.right, cur_level+1])
        

        ret_list = []

        for k in sorted(ret.keys()):
            ret_list.append(ret[k][-1])
        

        return ret_list

        