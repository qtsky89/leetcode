from collections import defaultdict

class Solution:
    def killProcess(self, pids: List[int], ppids: List[int], kill: int) -> List[int]:
        '''
        index pid  ppid (parent)
        0      1    3
        1      3    0
        2     10    5
        3      5    3
        
        {
            3 : [1]
            0 : [3]
            5 : [10]
            3 : [5]
        }
        '''

        hash_map = defaultdict(list)
        for ppid, pid in zip(ppids, pids):
            hash_map[ppid].append(pid)
        
        ret = []

        def dfs(current_pid: int):
            ret.append(current_pid)

            for new_pid in hash_map[current_pid]:
                dfs(new_pid)
        
        dfs(kill)

        return ret

        