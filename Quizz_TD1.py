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
        self.score = 0
        self.current_level = 1

    def ask_question(self, level):
        question = random.choice(self.questions[level])
        print(f"\nLevel {level} Question:")
        print(question["question"])
        
        # Display multiple choice options
        for i, option in enumerate(question["options"], 1):
            print(f"{i}. {option}")
        
        attempts = 2
        while attempts > 0:
            try:
                choice = int(input("\nEnter your choice (1-4): "))
                
                answer = question["options"][choice - 1]
                if answer == question["correct_answer"]:
                    print("Correct! 🎉")
                    return True
                else:
                    attempts -= 1
                    if attempts > 0:
                        print(f"Incorrect. Here's a hint: {question['hint']}")
                        print(f"You have {attempts} attempt left.")
                    else:
                        print(f"Sorry, the correct answer was: {question['correct_answer']}")
                        return False
            except ValueError:
                print("Please enter a valid number between 1 and 4")

    def play(self):
        print("Welcome to the Multiple Choice Progressive Quiz Game!")
        print("Rules:")
        print("- There are 5 levels of increasing difficulty")
        print("- Each question has 4 possible answers")
        print("- You get 2 attempts per question, with a hint after the first attempt")
        print("- You need to answer correctly to advance to the next level")
        
        while self.current_level <= 5:
            print(f"\n=== Level {self.current_level} ===")
            if self.ask_question(self.current_level):
                self.score += self.current_level * 100
                if self.current_level < 5:
                    print(f"Congratulations! Moving to level {self.current_level + 1}")
                self.current_level += 1
            else:
                retry = input("Would you like to try again? (yes/no): ").lower()
                if retry != 'yes':
                    break

        print(f"\nGame Over! Final score: {self.score}")
        if self.current_level > 5:
            print("Congratulations! You've completed all levels! 🏆")
        else:
            print(f"You reached level {self.current_level}")

# Run the game
if __name__ == "__main__":
    game = QuizGame()
    game.play()