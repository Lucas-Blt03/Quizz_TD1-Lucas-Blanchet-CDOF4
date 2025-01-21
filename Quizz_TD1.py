import random

class QuizGame:
    def __init__(self):
        self.questions = {
            1: [
                {
                    "question": "What is 5 + 7?",
                    "options": ["10", "11", "12", "13"],
                    "correct_answer": "12",
                    "hint": "Count up from 5"
                },
                {
                    "question": "What is the capital of France?",
                    "options": ["London", "Berlin", "Madrid", "Paris"],
                    "correct_answer": "Paris",
                    "hint": "Think of the Eiffel Tower"
                }
            ],
            2: [
                {
                    "question": "What is 15 × 8?",
                    "options": ["110", "120", "130", "140"],
                    "correct_answer": "120",
                    "hint": "Break it down: (10 × 8) + (5 × 8)"
                },
                {
                    "question": "Which planet is known as the Red Planet?",
                    "options": ["Venus", "Mars", "Jupiter", "Saturn"],
                    "correct_answer": "Mars",
                    "hint": "Named after the Roman god of war"
                }
            ],
            3: [
                {
                    "question": "What is the square root of 144?",
                    "options": ["10", "11", "12", "13"],
                    "correct_answer": "12",
                    "hint": "Think of a number that multiplied by itself equals 144"
                },
                {
                    "question": "Who wrote 'Romeo and Juliet'?",
                    "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
                    "correct_answer": "William Shakespeare",
                    "hint": "Famous English playwright from the 16th century"
                }
            ],
            4: [
                {
                    "question": "Which of these is the chemical equation for photosynthesis?",
                    "options": [
                        "H2O → H2 + O2",
                        "6CO2 + 6H2O → C6H12O6 + 6O2",
                        "CH4 + 2O2 → CO2 + 2H2O",
                        "N2 + 3H2 → 2NH3"
                    ],
                    "correct_answer": "6CO2 + 6H2O → C6H12O6 + 6O2",
                    "hint": "Involves carbon dioxide, water, glucose, and oxygen"
                },
                {
                    "question": "When did quantum mechanics begin with Planck's quantum theory?",
                    "options": ["1885", "1900", "1915", "1925"],
                    "correct_answer": "1900",
                    "hint": "Turn of the 20th century"
                }
            ],
            5: [
                {
                    "question": "Which is Schrödinger's equation for a free particle?",
                    "options": [
                        "E = mc²",
                        "iℏ∂ψ/∂t = -(ℏ²/2m)∇²ψ",
                        "F = ma",
                        "PV = nRT"
                    ],
                    "correct_answer": "iℏ∂ψ/∂t = -(ℏ²/2m)∇²ψ",
                    "hint": "Involves the reduced Planck constant and the Laplacian"
                },
                {
                    "question": "What is the correct statement of the Riemann hypothesis?",
                    "options": [
                        "All even numbers are the sum of two primes",
                        "All non-trivial zeros of the Riemann zeta function have a real part equal to 1/2",
                        "There are infinitely many twin primes",
                        "Every even integer greater than 2 can be written as the sum of two primes"
                    ],
                    "correct_answer": "All non-trivial zeros of the Riemann zeta function have a real part equal to 1/2",
                    "hint": "Related to prime numbers and complex analysis"
                }
            ]
        }
        self.scores = {}
        self.lives = 3  # Default lives per player
        self.used_questions = {level: [] for level in self.questions}  # Track used questions per level

    def ask_question(self, player, level):
        # Ensure unique question per player by tracking used questions
        available_questions = [q for q in self.questions[level] if q not in self.used_questions[level]]
        if not available_questions:
            print(f"No more unique questions available for level {level}. Skipping...")
            return False

        question = random.choice(available_questions)
        self.used_questions[level].append(question)

        print(f"\n{player}, Level {level} Question:")
        print(question["question"])

        # Display multiple choice options
        for i, option in enumerate(question["options"], 1):
            print(f"{i}. {option}")

        remaining_lives = self.lives
        while remaining_lives > 0:
            try:
                choice = int(input("\nEnter your choice (1-4): "))
                answer = question["options"][choice - 1]
                if answer == question["correct_answer"]:
                    points = level * 100 - (self.lives - remaining_lives) * 10  # Deduct 10 points per lost life
                    self.scores[player] += max(0, points)  # Ensure score doesn't go negative
                    print(f"Correct! 🎉 You earned {points} points.")
                    return True
                else:
                    remaining_lives -= 1
                    if remaining_lives > 0:
                        print(f"Incorrect. Here's a hint: {question['hint']}")
                        print(f"You have {remaining_lives} lives left.")
                    else:
                        print(f"Sorry, the correct answer was: {question['correct_answer']}")
                        return False
            except (IndexError, ValueError):
                print("Please enter a valid number between 1 and 4")

    def play(self):
        print("Welcome to the Multiple Choice Progressive Quiz Game!")
        print("Rules:")
        print("- There are 5 levels of increasing difficulty")
        print("- Each question has 4 possible answers")
        print(f"- You get {self.lives} total lives per question, with a hint after a failed attempt.")
        print("- You need to answer correctly to advance to the next level")

        # Determine the number of players
        num_players = 0
        while num_players not in [1, 2]:
            try:
                num_players = int(input("\nHow many players? (1 or 2): "))
            except ValueError:
                print("Please enter 1 or 2.")

        players = []
        if num_players == 1:
            players = ["Player 1"]
        else:
            players = [
                input("Enter the name of Player 1: "),
                input("Enter the name of Player 2: ")
            ]

        # Initialize scores for players
        self.scores = {player: 0 for player in players}
        levels_completed = {player: 1 for player in players}

        while any(level <= 5 for level in levels_completed.values()):
            for player in players:
                if levels_completed[player] <= 5:
                    print(f"\n=== {player}'s Turn (Level {levels_completed[player]}) ===")
                    if self.ask_question(player, levels_completed[player]):
                        levels_completed[player] += 1
                        if levels_completed[player] > 5:
                            print(f"Congratulations {player}, you've completed all levels! 🏆")
                    else:
                        print(f"{player}, you failed Level {levels_completed[player]}.")
                        levels_completed[player] = 6  # Mark as failed

        print("\nGame Over! Final Scores:")
        for player, score in self.scores.items():
            print(f"{player}: {score} points")

        # Determine the winner
        if len(players) > 1:
            winner = max(self.scores, key=self.scores.get)
            max_score = self.scores[winner]
            tied_players = [player for player, score in self.scores.items() if score == max_score]

            if len(tied_players) > 1:
                print("\nIt's a tie! 🎉 The winners are:")
                for player in tied_players:
                    print(f"- {player}")
                print("Well played, everyone!")
            else:
                print(f"\nAnd the winner is... 🏆 {winner} 🏆 with {max_score} points! Congratulations!")
        else:
            print("\nThank you for playing! Hope you enjoyed the game!")

# Run the game
if __name__ == "__main__":
    game = QuizGame()
    game.play()
