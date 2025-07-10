import random

class PigGame:
    def __init__(self):
        self.max_score = 100
        self.players = 0
        self.scores = []
    
    def roll(self):
        """Roll a dice and return the result."""
        return random.randint(1, 6)
    
    def get_player_count(self):
        """Get the number of players for the game."""
        while True:
            try:
                players = input("Enter number of players (2-4): ").strip()
                if players.isdigit():
                    players = int(players)
                    if 2 <= players <= 4:
                        return players
                    else:
                        print("Please enter a number between 2 and 4.")
                else:
                    print("Invalid input. Please enter a number between 2 and 4.")
            except KeyboardInterrupt:
                print("\nGame cancelled.")
                return None
    
    def play(self):
        """Main game loop."""
        print("\nWelcome to Pig!")
        print("First player to reach 100 points wins!")
        print("Roll dice to accumulate points, but if you roll a 1, you lose all points for that turn!\n")
        
        # Get number of players
        self.players = self.get_player_count()
        if self.players is None:
            return
        
        print(f"Starting Pig game with {self.players} player(s)...\n")
        
        # Initialize scores
        self.scores = [0] * self.players
        
        # Main game loop
        while max(self.scores) < self.max_score:
            for player in range(self.players):
                print(f"\nPlayer {player + 1}'s turn (Current score: {self.scores[player]}):")
                turn_score = 0
                
                while True:
                    try:
                        roll_result = self.roll()
                        print(f"Rolled: {roll_result}")
                        
                        if roll_result == 1:
                            print("Rolled a 1! Turn score is lost.")
                            turn_score = 0
                            break
                        else:
                            turn_score += roll_result
                            print(f"Turn score: {turn_score}")
                            
                            # Check if player would win with current turn score
                            if self.scores[player] + turn_score >= self.max_score:
                                print(f"You can win by holding! Total would be: {self.scores[player] + turn_score}")
                            
                            choice = input("Roll again (r) or hold (h)? ").strip().lower()
                            if choice == 'h':
                                break
                            elif choice != 'r':
                                print("Invalid choice. Please enter 'r' to roll or 'h' to hold.")
                    except KeyboardInterrupt:
                        print("\nGame cancelled.")
                        return
                
                self.scores[player] += turn_score
                print(f"Player {player + 1} total score: {self.scores[player]}")
                
                # Check for winner
                if self.scores[player] >= self.max_score:
                    self.show_final_results()
                    return
        
        self.show_final_results()
    
    def show_final_results(self):
        """Display final scores and winner."""
        print("\n" + "="*30)
        print("🎯 FINAL SCORES")
        print("="*30)
        for player in range(self.players):
            print(f"Player {player + 1}: {self.scores[player]}")
        
        winner = self.scores.index(max(self.scores)) + 1
        print(f"\n🎉 Player {winner} wins the game! 🎉")
        print("="*30)

def main():
    """Standalone main function for running Pig directly."""
    while True:
        game = PigGame()
        game.play()
        
        if input("\nPlay again? (y/n): ").lower() != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()