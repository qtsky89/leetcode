class FreqStack:
    def __init__(self):
        self.cnt: dict[int, int] = {}
        self.max_cnt: int = 0
        self.stacks: dict[int, list[int]] = {}
        

    def push(self, val: int) -> None:
        if val in self.cnt:
            self.cnt[val] += 1
        else:
            self.cnt[val] = 1
        
        if self.cnt[val] in self.stacks:
            self.stacks[self.cnt[val]].append(val)
        else:
            self.stacks[self.cnt[val]] = [val]
        
        self.max_cnt = max(self.max_cnt, self.cnt[val])

    def pop(self) -> int:
        tmp = self.stacks[self.max_cnt].pop()

        if not self.stacks[self.max_cnt]:
            del self.stacks[self.max_cnt]
            self.max_cnt -= 1
        self.cnt[tmp] -=1
        if self.cnt[tmp] == 0:
            del self.cnt[tmp]
        
        return tmp
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()