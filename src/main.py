import os
class UI:
    def __init__(self, p1, p2):
        self.ours = p1
        self.other = p2
        self.messages = []
    def ResetUI(self):
        os.run("cls")
        print(f"{self.ours.Name}")
def main() -> None:
    print("Welcome to the Pokemon game!")

if __name__ == "__main__":
    main()