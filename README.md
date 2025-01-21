# Quizz_TD1-Lucas-Blanchet-DIA2: Progressive Multiple Choice Quiz Game

A Python-based quiz game that challenges players with increasingly difficult questions across 5 levels. Each question comes with multiple choice answers and helpful hints.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites

You need to have Python installed on your computer. The game is compatible with Python 3.x versions.



## Installing

1. Clone the repository

git clone https://github.com/yourusername/progressive-quiz-game.git

2. Navigate to the project directory

cd progressive-quiz-game

3. Run the game

python quiz_game.py

## How to play

1. Start the game
2. Answer multiple-choice questions by entering numbers 1-4
3. If wrong, you get a hint and second attempt
4. Progress through 5 levels of increasing difficulty
5. Score points based on your level (Level 1 = 100pts, Level 2 = 200pts, etc.)

## Example Output
Here's what the game looks like when you play it:

```plaintext
Welcome to the Multiple Choice Progressive Quiz Game!
Rules:
- There are 5 levels of increasing difficulty
- Each question has 4 possible answers
- You get 3 total lives per question, with a hint after a failed attempt.
- You need to answer correctly to advance to the next level

How many players? (1 or 2): 1

=== Player 1's Turn (Level 1) ===

Player 1, Level 1 Question:
What is the capital of France?
1. London
2. Berlin
3. Madrid
4. Paris

Enter your choice (1-4): 4
Correct! 🎉 You earned 100 points.\`\`\`


Here's what the game looks like when you finish it:

```plaintext
Congratulations Player 1, you've completed all levels! 🏆

Game Over! Final Scores:
Player 1: 1500 points

Thank you for playing! Hope you enjoyed the game!\`\`\`


## Question Format Test

{  
    "question": "Your question here?",  
    "options": ["Option 1", "Option 2", "Option 3", "Option 4"],  
    "correct_answer": "Correct option here",  
    "hint": "Hint for the question"  
}



## Deployment

This is a standalone Python application that can be run directly from the command line.


## Authors

* **Lucas Blanchet** 


## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
