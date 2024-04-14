class BrowserHistory:
    '''
    homepage -> google -> naver -> bloomberg
                           ^      
    '''
    def __init__(self, homepage: str):
        # homepage, google
        self.backward_stack = [homepage]

        # bloomberg, naver
        self.forward_stack = []

    def visit(self, url: str) -> None:
        self.backward_stack.append(url)
        self.forward_stack = []
        
    def back(self, steps: int) -> str:
        while len(self.backward_stack) > 1 and steps > 0:
            steps -= 1
            tmp = self.backward_stack.pop()
            self.forward_stack.append(tmp)
        return self.backward_stack[-1]
    
    def forward(self, steps: int) -> str:
        while self.forward_stack and steps > 0:
            steps -= 1
            tmp = self.forward_stack.pop()
            self.backward_stack.append(tmp)
        return self.backward_stack[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)