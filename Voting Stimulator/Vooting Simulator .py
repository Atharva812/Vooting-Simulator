import tkinter as tk
from tkinter import messagebox
import pygame
import threading
import random
import math

class VotingSimulator:
    def __init__(self, master):
        self.master = master
        self.master.title("Voting Simulator")
        self.master.geometry("400x300")

        self.candidates = ["Narendra Modi (Boss)", "Rahul Gandhi (pappu)", "Sharad Pawar (Tatya)"]
        self.votes = []

        pygame.init()
        pygame.mixer.init()

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

        if count > 0:
            if self.votes.count(candidate) > len(self.votes) // 2:
                winner_message = f"The winner is {candidate} with {self.votes.count(candidate)} votes!"
            else:
                winner_message = "No candidate has a majority of votes."
        else:
            winner_message = "No candidate has a majority of votes."

        messagebox.showinfo("Winner", winner_message)

      
        if "No candidate has a majority of votes." not in winner_message:
            threading.Thread(target=self.play_fireworks, args=(candidate,), daemon=True).start()

    def play_fireworks(self, winner):
        pygame.mixer.music.load("C:\\Users\\athar\\OneDrive - MSFT\\Desktop\\CODES\\Mini Project\\Voting Stimulator\\firework.mp3")  
        pygame.mixer.music.play()

        pygame.display.set_caption("Pygame Winner Display")
        screen = pygame.display.set_mode((800, 600))

        font = pygame.font.Font(None, 36)
        text = font.render(f"The winner is {winner}!", True, (255, 255, 255))
        text_rect = text.get_rect(center=(400, 300))

        clock = pygame.time.Clock()

        fireworks = []

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((0, 0, 0))
            screen.blit(text, text_rect)

            for firework in fireworks:
                firework.draw(screen)
                firework.update()

            if random.random() < 0.05:
                fireworks.append(Firework())

            fireworks = [firework for firework in fireworks if not firework.done]

            pygame.display.flip()
            clock.tick(30)

        pygame.quit()

class Spark:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (random.randint(200, 255), random.randint(0, 50), 0)
        self.radius = 2
        self.velocity = random.uniform(1, 3)
        self.angle = random.uniform(0, 2 * 3.14159)
        self.done = False

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def update(self):
        self.x += self.velocity * 2 * 3.14159 * random.uniform(0.8, 1.2) * 0.1 * math.cos(self.angle)
        self.y += self.velocity * 2 * 3.14159 * random.uniform(0.8, 1.2) * 0.1 * math.sin(self.angle)
        self.radius -= 0.05
        if self.radius <= 0:
            self.done = True

class Firework:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = 600
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.radius = 5
        self.velocity = random.uniform(5, 10)
        self.sparks = [Spark(self.x, self.y) for _ in range(random.randint(50, 100))]
        self.done = False

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        for spark in self.sparks:
            spark.draw(screen)

    def update(self):
        self.y -= self.velocity
        self.radius += 1
        if self.y < 300:
            self.sparks = [Spark(self.x, self.y) for _ in range(random.randint(50, 100))]
            self.done = True
        for spark in self.sparks:
            spark.update()

if __name__ == "__main__":
    root = tk.Tk()
    app = VotingSimulator(root)
    root.mainloop()
