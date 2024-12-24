import tkinter as tk
from tkinter import messagebox
import random
import pygame

# Initialize pygame mixer for sound
pygame.mixer.init()

#List of Game questions
questions = {
    "Name a country in Europe": [
        {"answer": "Germany", "score": 71},
        {"answer": "France", "score": 78},
        {"answer": "Italy", "score": 77},
        {"answer": "United Kingdom", "score": 72},
        {"answer": "Spain", "score": 70},
        {"answer": "Netherlands", "score": 55},
        {"answer": "Sweden", "score": 52},
        {"answer": "Russia", "score": 48},
        {"answer": "Denmark", "score": 46},
        {"answer": "Switzerland", "score": 45},
        {"answer": "Ireland", "score": 43},
        {"answer": "Norway", "score": 41},
        {"answer": "Poland", "score": 39},
        {"answer": "Portugal", "score": 38},
        {"answer": "Czech Republic", "score": 25},
        {"answer": "Hungary", "score": 34},
        {"answer": "Romania", "score": 32},
        {"answer": "Belgium", "score": 30},
        {"answer": "Finland", "score": 30},
        {"answer": "Greece", "score": 39},
        {"answer": "Bulgaria", "score": 8},
        {"answer": "Croatia", "score": 17},
        {"answer": "Austria", "score": 16},
        {"answer": "Belarus", "score": 5},
        {"answer": "Latvia", "score": 3},
        {"answer": "Slovakia", "score": 2},
        {"answer": "Serbia", "score": 10},
        {"answer": "Slovenia", "score": 9},
        {"answer": "Cyprus", "score": 7},
        {"answer": "Estonia", "score": 4},
        {"answer": "Iceland", "score": 13},
        {"answer": "Bosnia & Herzegovina", "score": 1},
        {"answer": "Luxembourg", "score": 10},
        {"answer": "Malta", "score": 0},  # Pointless answer
        {"answer": "Andorra", "score": 0},  # Pointless answer
        {"answer": "San Marino", "score": 0},  # Pointless answer
        {"answer": "Georgia", "score": 2},
        {"answer": "Monaco", "score": 1},
        {"answer": "Kosovo", "score": 0},  # Pointless answer
    ],
    "Name a U.S. state capital": [
        {"answer": "Montgomery", "score": 30},
        {"answer": "Juneau", "score": 35},
        {"answer": "Phoenix", "score": 63},
        {"answer": "Little Rock", "score": 25},
        {"answer": "Sacramento", "score": 67},
        {"answer": "Denver", "score": 73},
        {"answer": "Hartford", "score": 13},
        {"answer": "Dover", "score": 22},
        {"answer": "Tallahassee", "score": 33},
        {"answer": "Atlanta", "score": 61},
        {"answer": "Honolulu", "score": 47},
        {"answer": "Boise", "score": 27},
        {"answer": "Springfield", "score": 45},
        {"answer": "Indianapolis", "score": 53},
        {"answer": "Des Moines", "score": 26},
        {"answer": "Topeka", "score": 18},
        {"answer": "Frankfort", "score": 6},
        {"answer": "Baton Rouge", "score": 22},
        {"answer": "Augusta", "score": 14},
        {"answer": "Annapolis", "score": 12},
        {"answer": "Boston", "score": 56},
        {"answer": "Lansing", "score": 32},
        {"answer": "Saint Paul", "score": 22},
        {"answer": "Jackson", "score": 0},
        {"answer": "Jefferson City", "score": 29},
        {"answer": "Helena", "score": 20},
        {"answer": "Lincoln", "score": 5},
        {"answer": "Carson City", "score": 11},
        {"answer": "Concord", "score": 18},
        {"answer": "Trenton", "score": 14},
        {"answer": "Santa Fe", "score": 42},
        {"answer": "Albany", "score": 2},
        {"answer": "Raleigh", "score": 49},
        {"answer": "Bismarck", "score": 19},
        {"answer": "Columbus", "score": 59},
        {"answer": "Oklahoma City", "score": 37},
        {"answer": "Salem", "score": 23},
        {"answer": "Harrisburg", "score": 35},
        {"answer": "Providence", "score": 23},
        {"answer": "Columbia", "score": 17},
        {"answer": "Pierre", "score": 15},
        {"answer": "Nashville", "score": 51},
        {"answer": "Austin", "score": 70},
        {"answer": "Salt Lake City", "score": 39},
        {"answer": "Montpelier", "score": 0},  # Pointless answer
        {"answer": "Richmond", "score": 41},
        {"answer": "Olympia", "score": 10},
        {"answer": "Charleston", "score": 16},
        {"answer": "Madison", "score": 56},
        {"answer": "Cheyenne", "score": 1},
    ],
    "Name a common fish that Brits eat or catch": [
        {"answer": "Cod", "score": 74},
        {"answer": "Haddock", "score": 62},
        {"answer": "Salmon", "score": 70},
        {"answer": "Mackerel", "score": 48},
        {"answer": "Plaice", "score": 35},
        {"answer": "Tuna", "score": 62},
        {"answer": "Bass", "score": 60},
        {"answer": "Trout", "score": 58},
        {"answer": "Herring", "score": 55},
        {"answer": "Sardines", "score": 53},
        {"answer": "Pollock", "score": 52},
        {"answer": "Whiting", "score": 20},
        {"answer": "Pike", "score": 48},
        {"answer": "Bream", "score": 16},
        {"answer": "Carp", "score": 44},
        {"answer": "Perch", "score": 42},
        {"answer": "Eel", "score": 40},
        {"answer": "Flounder", "score": 38},
        {"answer": "Sprats", "score": 0},
        {"answer": "Zander", "score": 4},
        {"answer": "Ling", "score": 2},
        {"answer": "John Dory", "score": 0},
        {"answer": "Monkfish", "score": 8},
        {"answer": "Skate", "score": 17},
        {"answer": "Turbot", "score": 6},
        {"answer": "Smoothhound", "score": 4},
        {"answer": "Catfish", "score": 43},
        {"answer": "Conger Eel", "score": 22},
        {"answer": "Garfish", "score": 21},
        {"answer": "Brill", "score": 20},
        {"answer": "Dogfish", "score": 18},
        {"answer": "Codling", "score": 16},
        {"answer": "Sole", "score": 14},
        {"answer": "Wrasse", "score": 1},
        {"answer": "Mullet", "score": 10},
        {"answer": "Rudd", "score": 0},  # Pointless answer
        {"answer": "Gurnard", "score": 0},  # Pointless answer
        {"answer": "Dab", "score": 0},  # Pointless answer
    ]
}

# Function to play sound
def play_sound(file_path):
    try:
        sound = pygame.mixer.Sound(file_path)
        sound.play()
    except pygame.error as e:
        print(f"Error playing sound: {e}")

class PointlessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("A Pointless Family Holiday Game")
        self.root.geometry("1000x600")

        self.teams = []
        self.current_question = None
        self.current_answers = []
        self.current_team = 0
        self.team_scores = {}
        self.jackpot = 100
        self.in_countdown = False
        self.turn_order = []
        self.round = 1
        self.submitted_answers = []  # Track submitted answers for the current question

        # Leaderboard frame
        self.leaderboard_frame = tk.Frame(self.root, width=300, height=600, bg="lightgray")
        self.leaderboard_frame.pack(side="right", fill="y")

        self.setup_game()

    def setup_game(self):
        self.clear_window()
        self.turn_order = []
        self.round = 1
        tk.Label(self.root, text="Welcome to A Pointless Holiday Game!", font=("Helvetica", 32), anchor="center").pack(pady=20)
        tk.Label(self.root, text="Enter number of teams:", font=("Helvetica", 16)).pack()
        self.team_entry = tk.Entry(self.root)
        self.team_entry.pack(pady=10)
        tk.Button(self.root, text="Start Game", command=self.start_game, font=("Helvetica", 14)).pack(pady=20)

    def start_game(self):
        num_teams = self.team_entry.get()
        if not num_teams.isdigit() or int(num_teams) <= 0:
            messagebox.showerror("Invalid Input", "Please enter a valid number of teams.")
            return

        self.teams = [f"Team {i+1}" for i in range(int(num_teams))]
        self.team_scores = {team: 0 for team in self.teams}
        self.turn_order = self.teams[:]
        self.update_leaderboard()
        self.next_question()

    def next_question(self):
        if len(questions) == 0 or len(self.teams) == 1:
            self.show_results()
            return

        self.current_question, self.current_answers = random.choice(list(questions.items()))
        del questions[self.current_question]
        self.submitted_answers = []  # Reset submitted answers for the new question
        self.round = 1
        self.show_question()

    def show_question(self):
        self.clear_window()

        # Calculate dynamic points needed
        scores = list(self.team_scores.values())
        points_needed = None if all(score == 0 for score in scores) else max(scores) - self.team_scores[self.turn_order[self.current_team]]

        question_label = tk.Label(self.root, text=f"Question for {self.turn_order[self.current_team]}:", font=("Helvetica", 20))
        question_label.pack(pady=10)

        tk.Label(self.root, text=self.current_question, font=("Helvetica", 24), anchor="center").pack(pady=20)
        if points_needed is not None and points_needed > 0:
            tk.Label(self.root, text=f"Points needed to remain not last: {points_needed} points", fg="red", font=("Helvetica", 14)).pack(pady=5)
        tk.Label(self.root, text=f"Pointless Jackpot ${self.jackpot} USD", fg="green", font=("Helvetica", 16)).pack(pady=5)

        tk.Label(self.root, text="Enter your answer:", font=("Helvetica", 16)).pack(pady=10)
        self.answer_entry = tk.Entry(self.root)
        self.answer_entry.pack(pady=10)

        tk.Button(self.root, text="Submit", command=self.check_answer, font=("Helvetica", 14)).pack(pady=20)

        # Display submitted answers at the bottom
        submitted_answers_frame = tk.Frame(self.root, height=100)
        submitted_answers_frame.pack(side="bottom", fill="x", pady=20)

        tk.Label(submitted_answers_frame, text="Submitted Answers:", font=("Helvetica", 14, "bold")).pack(anchor="w")
        for answer in self.submitted_answers:
            tk.Label(submitted_answers_frame, text=answer, font=("Helvetica", 12)).pack(anchor="w", padx=10)

    def check_answer(self):
        answer = self.answer_entry.get().strip().lower()
        if answer in self.submitted_answers:
            messagebox.showinfo("Duplicate Answer", "This answer has already been submitted.")
            return

        self.submitted_answers.append(answer)
        found = False

        for ans in self.current_answers:
            if ans["answer"].lower() == answer:
                self.show_score_countdown(ans["score"])
                if ans["score"] == 0:
                    #messagebox.showinfo("Pointless!", f"{self.turn_order[self.current_team]} found a Pointless answer!")
                    self.jackpot += 100
                else:
                    self.team_scores[self.turn_order[self.current_team]] += ans["score"]
                found = True
                break

        if not found:
            self.show_incorrect_feedback()
            self.team_scores[self.turn_order[self.current_team]] += 100

        self.update_leaderboard()

    def show_incorrect_feedback(self):
        popup = tk.Toplevel(self.root)
        popup.title("Wrong Answer")
        popup.geometry("800x200")
        tk.Label(popup, text="❌ 100 points!", font=("Helvetica", 70), fg="red").pack(pady=20)

        def close_popup():
            popup.destroy()
            self.transition_to_next_team()

        popup.after(1500, close_popup)

    def show_score_countdown(self, final_score):
        """Displays and animates the score countdown."""
        self.in_countdown = True  # Prevent other actions during countdown

        # Clear all widgets except the leaderboard
        for widget in self.root.winfo_children():
            if widget != self.leaderboard_frame:
                widget.destroy()

        # Center the countdown vertically and horizontally
        countdown_frame = tk.Frame(self.root)
        countdown_frame.place(relx=0.5, rely=0.5, anchor="center")  # Centered

        # Countdown Label
        countdown_label = tk.Label(countdown_frame, text="Score:", font=("Helvetica", 48))
        countdown_label.pack(pady=20)

        # Animated score
        score_var = tk.IntVar(value=100)  # Start countdown at 100
        countdown_value = tk.Label(countdown_frame, textvariable=score_var, font=("Helvetica", 240), fg="red")
        countdown_value.pack(pady=10)

        def update_color(score):
            """Change text color dynamically based on score."""
            if score > 60:
                return "red"
            elif score > 30:
                return "orange"
            else:
                return "green"

        def countdown():
            current_score = score_var.get()
            if current_score > final_score:
                score_var.set(current_score - 1)
                countdown_value.config(fg=update_color(current_score))
                self.root.after(50, countdown)  # Smooth countdown animation
            else:
                self.in_countdown = False
                self.root.after(2000, self.transition_to_next_team)  # Delay for 2 seconds

        countdown()

    def transition_to_next_team(self):
        """Handles moving to the next team's turn or progressing to the next round/question."""
        if len(self.turn_order) <= 1:  # If only one team is left, end the game
            self.show_results()
            return

        self.current_team += 1

        # If the current team exceeds the number of teams, handle round transitions
        if self.current_team >= len(self.turn_order):
            if self.round == 1:  # Move to the second round of the same question
                self.turn_order = [team for team, _ in sorted(self.team_scores.items(), key=lambda x: x[1])]
                self.current_team = 0  # Start from the first team
                self.round = 2  # Second round
            else:  # Eliminate team and proceed to the next question
                self.eliminate_team()
                return

        # Ensure the game transitions to the next question or team
        self.show_question()

    def update_leaderboard(self):
        for widget in self.leaderboard_frame.winfo_children():
            widget.destroy()

        tk.Label(self.leaderboard_frame, text="Leaderboard", font=("Helvetica", 18, "bold")).pack(pady=10)

        sorted_scores = sorted(self.team_scores.items(), key=lambda x: x[1])
        for team, score in sorted_scores:
            tk.Label(self.leaderboard_frame, text=f"{team}: {score} points", font=("Helvetica", 16)).pack(pady=5)

    def eliminate_team(self):
        scores = list(self.team_scores.values())
        highest_score = max(scores)
        team_to_eliminate = [team for team, score in self.team_scores.items() if score == highest_score][0]

        messagebox.showinfo("Elimination", f"{team_to_eliminate} has been eliminated!")
        del self.team_scores[team_to_eliminate]
        self.teams.remove(team_to_eliminate)

        if len(self.teams) <= 1:
            self.show_results()
        else:
            self.turn_order = self.teams
            self.current_team = 0
            self.next_question()

    def show_results(self):
        self.clear_window()
        tk.Label(self.root, text="Final Scores", font=("Helvetica", 20)).pack(pady=10)

        sorted_scores = sorted(self.team_scores.items(), key=lambda x: x[1])
        for team, score in sorted_scores:
            tk.Label(self.root, text=f"{team}: {score} points", font=("Helvetica", 16)).pack()

        tk.Label(self.root, text=f"Winner: {sorted_scores[0][0]}!", font=("Helvetica", 24, "bold")).pack(pady=20)
        tk.Button(self.root, text="Play Again", command=self.setup_game, font=("Helvetica", 16)).pack(pady=20)

    def clear_window(self):
        if self.in_countdown:
            return
        for widget in self.root.winfo_children():
            if widget != self.leaderboard_frame:
                widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = PointlessGame(root)
    root.mainloop()
