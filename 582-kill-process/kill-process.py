class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        '''
        pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5
                    ^                 ^ 
                            index= 2 
           pid ppid
        0   1   3
        1   3   0
        2  10   5
        3   5   3


        {
            0 : [3]
            1 : []
            3 : [1]
            10 : []
            5 : [10]
        }
        '''

        hash_map = {}
        
        for p, pp in zip(pid, ppid):
            if pp in hash_map:
                hash_map[pp].append(p)
            else:
                hash_map[pp] = [p]
        
        q = deque([kill])

        ret = []
        while q:
            item = q.popleft()
            ret.append(item)

            if item in hash_map:
                for new_item in hash_map[item]:
                    q.append(new_item)
        return ret
        
        


        
        return ret

        