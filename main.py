import sys
import os

# Add the 'games' directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
games_dir = os.path.join(current_dir, "games")
sys.path.insert(0, games_dir)

# Try importing with error handling
try:
    from Wordle import WordleGame
    from Pig import PigGame
    from Superpower import SuperpowerGame
    print("✅ Successfully imported WordleGame, PigGame, and SuperpowerGame")
except ImportError as e:
    print(f"❌ Import error: {e}")
    print(f"Games directory: {games_dir}")
    print(f"Games directory exists: {os.path.exists(games_dir)}")
    if os.path.exists(games_dir):
        print(f"Files in games directory: {os.listdir(games_dir)}")
    sys.exit(1)

def main_menu():
    while True:
        print("\n" + "="*40)
        print("🎮 MAIN GAME SELECTION MENU")
        print("="*40)
        print("1 - Play Wordle")
        print("2 - Play Pig")
        print("3 - Superpower Generator")
        print("Q - Quit")
        print("="*40)

        choice = input("Enter your choice: ").strip().lower()

        if choice == '1':
            print("\nStarting Wordle...")
            try:
                wordle_game = WordleGame()
                wordle_game.play()
                print("\nReturning to main menu.")
            except Exception as e:
                print(f"❌ Error starting Wordle: {e}")
        elif choice == '2':
            print("\nStarting Pig...")
            try:
                pig_game = PigGame()
                pig_game.play()
                print("\nReturning to main menu.")
            except Exception as e:
                print(f"❌ Error starting Pig: {e}")
        elif choice == '3':
            print("\nStarting Superpower Generator...")
            try:
                superpower_game = SuperpowerGame()
                superpower_game.play()
                print("\nReturning to main menu.")
            except Exception as e:
                print(f"❌ Error starting Superpower Generator: {e}")
        elif choice == 'q':
            print("\n👋 Thanks for playing! Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()