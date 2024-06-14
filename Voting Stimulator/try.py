import tkinter as tk
from tkinter import messagebox

class VotingSimulator:
    def __init__(self, master):
        self.master = master
        self.master.title("Voting Simulator")
        self.master.geometry("400x300")

        self.candidates = ["Narendra Modi (Boss)", "Rahul Gandhi (pappu)", "Sharad Pawar (Tataya)"]
        self.votes = []

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Select Your Candidate:").pack()

        self.selected_candidate = tk.StringVar(self.master)
        self.selected_candidate.set(self.candidates[0])  

        for candidate in self.candidates:
            tk.Radiobutton(
                self.master,
                text=candidate,
                variable=self.selected_candidate,
                value=candidate,
            ).pack()

        tk.Button(self.master, text="Vote", command=self.cast_vote).pack()
        tk.Button(self.master, text="Declare Winner", command=self.declare_winner).pack()

    def cast_vote(self):
        selected_candidate = self.selected_candidate.get()
        self.votes.append(selected_candidate)
        messagebox.showinfo("Success", f"You voted for {selected_candidate}!")

    def declare_winner(self):
        if not self.votes:
            messagebox.showwarning("No Votes", "No votes cast yet.")
            return

        candidate = self.find_majority_candidate()

        if candidate:
            winner_message = f"The winner is {candidate} with {self.votes.count(candidate)} votes!"
        else:
            winner_message = "No candidate has a majority of votes."

        messagebox.showinfo("Winner", winner_message)

    def find_majority_candidate(self):
        candidate = None
        count = 0

        for vote in self.votes:
            if count == 0:
                candidate = vote
                count = 1
            elif vote == candidate:
                count += 1
            else:
                count -= 1

        if count > 0 and self.votes.count(candidate) > len(self.votes) // 2:
            return candidate
        else:
            return None

if __name__ == "__main__":
    root = tk.Tk()
    app = VotingSimulator(root)
    root.mainloop()
