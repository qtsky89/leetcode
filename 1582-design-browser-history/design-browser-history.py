'''
    leetcode.com -> google.com -> facebook.com -> youtube.com 
       ^
'''

class LinkedList:
    def __init__(self, val: str) -> None:
        self.val = val
        self.prev: LinkedList|None = None
        self.next: LinkedList|None = None
        
class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = LinkedList(homepage)
        self.p = self.head
        
    def visit(self, url: str) -> None:
        tmp = LinkedList(url)
        
        self.p.next = tmp
        tmp.prev = self.p

        self.p = self.p.next
        
    def back(self, steps: int) -> str:
        while self.p.prev and steps > 0:
            steps -= 1
            self.p = self.p.prev
        return self.p.val
        
    def forward(self, steps: int) -> str:
        while self.p.next and steps > 0:
            steps -= 1
            self.p = self.p.next
        return self.p.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)