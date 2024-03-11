import os
class UI:
    def __init__(self, p1, p2):
        self.ours = p1
        self.other = p2
        self.messages = []
    def ResetUI(self):
        os.run("cls")
        print(str(self.ours))
        print(str(self.other))
        print() 
        for x in self.messages:
            print(x)
        self.messages = []
    def addMessage(self, add):
        self.messages += add
def main() -> None:
    
if __name__ == "__main__":
    main()