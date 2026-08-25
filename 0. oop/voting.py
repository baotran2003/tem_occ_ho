class Voting:
    def __init__(self):
        self.votes: dict[str, int] = {
            "Bao": 0,
            "Hung": 0,
            "Quang": 0,
            "Long": 0,
        }

    def vote(self, candidate: str):
        if candidate in self.votes:
            self.votes[candidate] += 1
            print("Vote recorded successfully !")
        else:
            print("Invalid Candidate")

    def show_votes(self):
        print("\n----------Vote Count----------")
        for candidate, count in self.votes.items():
            print(candidate, "---", count)

    def winner(self):
        winner = max(self.votes, key=self.votes.get)
        print(f"\nThe winner is: {winner} with {self.votes[winner]} votes!")

if __name__ == "__main__":
    voting: Voting = Voting()

    while True:
        print("\n----------Online Voting System----------")
        print("1. Vote\n2. Show votes\n3. Show Winner\n4. Exit")

        try:
            choice: int = int(input("Enter your choice: "))
            if choice == 1:
                print("\n Candidates")
                i: int = 1
                for candidate in voting.votes:
                    print(i, "-", candidate)
                    i += 1
                candidate: str = input("Enter candidate name: ")
                voting.vote(candidate)

            elif choice == 2:
                voting.show_votes()
            elif choice == 3:
                voting.winner()
            elif choice == 4:
                print("Voting Ended !")
                break
            else:
                print("Invalid choice")

        except ValueError:
            print("Invalid input !")
            continue