import random
import os
from typing import List

def load_word_list(filename: str = "words.txt") -> List[str]:
    """Load word list from a text file."""
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, filename)
        
        with open(file_path, 'r', encoding='utf-8') as file:
            words = [line.strip().lower() for line in file if line.strip()]
        
        # Filter to only 5-letter words
        five_letter_words = [word for word in words if len(word) == 5 and word.isalpha()]
        
        if not five_letter_words:
            raise ValueError("No valid 5-letter words found in word list")
            
        return five_letter_words
    except FileNotFoundError:
        # Fallback word list if file is missing
        print("⚠️  Using fallback word list")
        return ['apple', 'beach', 'crane', 'dance', 'earth', 'fairy', 'grape', 
                'house', 'igloo', 'jelly', 'koala', 'lemon', 'mango', 'night',
                'olive', 'peach', 'queen', 'radio', 'sunny', 'tiger', 'umbra',
                'vivid', 'whale', 'xenon', 'yacht', 'zebra', 'about', 'below',
                'crisp', 'dwarf', 'elbow', 'flint', 'globe', 'honey', 'inbox',
                'jumpy', 'kneel', 'lucky', 'mirth', 'noble', 'oxide', 'piano']

word_list = load_word_list()

class Colors:
    """ANSI color codes for terminal output."""
    GREEN = '\033[42m\033[97m'  # Green background, white text
    YELLOW = '\033[43m\033[30m' # Yellow background, black text
    GRAY = '\033[100m\033[97m'   # Gray background, white text
    RESET = '\033[0m'            # Reset all formatting

class WordleGame:
    WORD_LENGTH = 5
    MAX_ATTEMPTS = 6
    
    def __init__(self):
        self.secret_word = random.choice(word_list)
        self.attempts = []
    
    def get_feedback(self, guess: str) -> str:
        """Generate colored feedback for the guessed word"""
        feedback = []
        secret_temp = list(self.secret_word)
        
        # First pass: check correct positions (green)
        for i in range(self.WORD_LENGTH):
            if guess[i] == secret_temp[i]:
                feedback.append(f"{Colors.GREEN} {guess[i].upper()} {Colors.RESET}")
                secret_temp[i] = None
            else:
                feedback.append("")
        
        # Second pass: check remaining letters (yellow/gray)
        for i in range(self.WORD_LENGTH):
            if not feedback[i]:
                if guess[i] in secret_temp:
                    feedback[i] = f"{Colors.YELLOW} {guess[i].upper()} {Colors.RESET}"
                    secret_temp[secret_temp.index(guess[i])] = None
                else:
                    feedback[i] = f"{Colors.GRAY} {guess[i].upper()} {Colors.RESET}"
        
        return " ".join(feedback)
    
    def play(self):
        print("\nWelcome to Wordle!")
        print(f"Guess the {self.WORD_LENGTH}-letter word. You have {self.MAX_ATTEMPTS} tries.\n")
        
        while len(self.attempts) < self.MAX_ATTEMPTS:
            # Show previous attempts
            for attempt in self.attempts:
                print(attempt)
            
            # Get new guess
            guess = input(f"Attempt {len(self.attempts)+1}/{self.MAX_ATTEMPTS}: ").lower()
            
            if len(guess) != self.WORD_LENGTH or not guess.isalpha():
                print(f"Please enter a {self.WORD_LENGTH}-letter word\n")
                continue
                
            feedback = self.get_feedback(guess)
            self.attempts.append(feedback)
            print()  # Blank line for spacing
            
            if guess == self.secret_word:
                print(f"🎉 Correct! The word was {self.secret_word.upper()}")
                print(f"Solved in {len(self.attempts)} tries!")
                return
        
        print(f"💔 Game over! The word was: {self.secret_word.upper()}")

def main():
    while True:
        game = WordleGame()
        game.play()
        
        if input("\nPlay again? (y/n): ").lower() != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
