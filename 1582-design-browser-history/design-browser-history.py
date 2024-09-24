class BrowserHistory:

    def __init__(self, homepage: str):
        self.urls = [homepage]
        self.current_position = 0
        self.size = 1

    def visit(self, url: str) -> None:
        if self.current_position+1 >= len(self.urls):
            self.urls.append(url)
        else:
            self.urls[self.current_position+1] = url
        self.current_position +=1
        self.size = self.current_position+1

    def back(self, steps: int) -> str:
        self.current_position = max(0,self.current_position-steps)
        return self.urls[self.current_position]

    def forward(self, steps: int) -> str:
        self.current_position = min(self.size-1, self.current_position+steps)
        return self.urls[self.current_position]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)