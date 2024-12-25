from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        '''
        0000
        '''

        # visited = {"0201", "0101", "0102", "1212", "2002"}
        visited = set(deadends)
        q = deque([('0000', 0)])

        while q:
            # item = '0000'
            item, count = q.popleft()

            if item in visited:
                continue

            visited.add(item)

            if item == target:
                return count

            # item[i] =>9 => 0
            # i = 0
            for i in range(len(item)):
                # t = 1
                t = str((int(item[i]) + 1) % 10)

                # tmp = 1000
                tmp = item[:i] + t +item[i+1:]

                if tmp not in visited:
                    q.append((tmp, count+1))

                # t = 1
                t = int(item[i])-1
                if t < 0:
                    t += 10

                # tmp = 1000
                tmp = item[:i] + str(t) +item[i+1:]

                if tmp not in visited:
                    q.append((tmp, count+1))
        return -1
            


            

            