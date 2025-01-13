class UnionFind:
    def __init__(self, k: int) -> None:
        self.parent = [i for i in range(k)]
        self.rank = [1] * k
    
    # find parent
    def find(self, x: int) -> int:
        while x != self.parent[x]:
            x = self.parent[x]
        return x
    
    # union
    def union(self, x1: int, x2: int) -> bool:
        p1, p2 = self.find(x1), self.find(x2)

        # already union
        if p1 == p2:
            return False

        rank1, rank2 = self.rank[p1], self.rank[p2]

        if rank1 < rank2:
            self.rank[p2] += self.rank[p1]
            self.parent[p1] = p2
        else:
            self.rank[p1] += self.rank[p2]
            self.parent[p2] = p1

        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        '''
        {
            "johnsmith@mail.com": 0,
            "john_newyork@mail.com": 0,
            "johnsmith@mail.com": 0,
            "john00@mail.com": 1,
            "mary@mail.com": 2,
            "johnnybravo@mail.com" : 3
        }

        '''

        uf = UnionFind(len(accounts))

        email_map: dict[str, int] = {}

        for index, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_map:
                    uf.union(email_map[email], index)
                else:
                    email_map[email] = index
        
        for email, index in email_map.items():
            email_map[email] = uf.find(index)
        
        '''
        {
            'johnsmith@mail.com': 0,
            'john_newyork@mail.com': 0,
            'john00@mail.com': 0,
            'mary@mail.com': 2,
            'johnnybravo@mail.com': 3
        }
        '''

        ret: defaultdict[int, list] = defaultdict(list)

        for email, index in email_map.items():
            ret[index].append(email)
        
        '''
        {
            0: [johnsmith@mail.com, john_newyork@mail.com, john00@mail.com]
            2: [mary@mail.com]
            3: [johnnybravo@mail.com]
        }

        '''

        filtered_ret = []

        for key, value in ret.items():
            value.sort()

            tmp = []
            tmp.append(accounts[key][0])
            tmp += value

            filtered_ret.append(tmp)
        
        return filtered_ret











        

        