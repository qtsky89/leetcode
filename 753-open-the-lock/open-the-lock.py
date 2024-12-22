from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)

        q = deque([["0000", 0]])
        while q:
            current_lock, count = q.popleft()
            if current_lock in visited:
                continue

            if current_lock == target:
                return count
            
            visited.add(current_lock)
            
            # first one 0
            for i in range(4):
                new_up = (int(current_lock[i]) + 1) % 10
                new_up_digits = current_lock[:i] + str(new_up) + current_lock[i+1:]
                if new_up_digits not in visited:
                    q.append([new_up_digits, count+1])

                new_down = int(current_lock[i]) - 1
                if new_down < 0:
                    new_down += 10
                new_down_ditigts = current_lock[:i] + str(new_down) + current_lock[i+1:]

                if new_down_ditigts not in visited:
                    q.append([new_down_ditigts, count+1])

        return -1