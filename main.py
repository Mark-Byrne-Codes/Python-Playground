import random
import os
from typing import List, Tuple
from enum import Enum

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
        print("⚠️  Warning: words.txt not found, using fallback word list")
        return ['which', 'their', 'would', 'there', 'could', 'other', 'about', 
                'great', 'these', 'after', 'first', 'never', 'where', 'those',
                'shall', 'being', 'might', 'every', 'think', 'under', 'found',
                'still', 'while', 'again', 'place', 'young', 'years', 'three',
                'right', 'house', 'whole', 'world', 'thing', 'night', 'going',
                'heard', 'heart', 'among', 'asked', 'small', 'woman', 'whose',
                'quite', 'words', 'given', 'taken', 'hands', 'until', 'since', 'light']

# Load word list at module level
word_list = load_word_list()

# ANSI color codes
class Colors:
    """ANSI color codes for terminal output."""
    # Background colors
    GREEN_BG = '\033[42m'    # Green background
    YELLOW_BG = '\033[43m'   # Yellow background  
    RED_BG = '\033[41m'      # Red background
    
    # Text colors
    WHITE = '\033[97m'       # White text
    BLACK = '\033[30m'       # Black text
    GRAY = '\033[90m'        # Gray text for borders
    
    # Reset
    RESET = '\033[0m'        # Reset all formatting


class Difficulty(Enum):
    EASY = 1
    HARD = 2
    SUPER_HARD = 3


class WordleGame:
    print(word_list)


def main():
    """Entry point for the game."""
    game = WordleGame()


if __name__ == "__main__":
    main()








