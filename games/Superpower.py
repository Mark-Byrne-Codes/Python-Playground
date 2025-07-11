import random

class SuperpowerGame:
    def __init__(self):
        # Word Pools
        self.prefixes = [
            "Shadow", "Solar", "Arcane", "Quantum", "Neon", "Void", "Iron", "Crystal",
            "Phoenix", "Titan", "Storm", "Cosmic", "Inferno", "Frost", "Toxic", "Sonic",
            "Gravity", "Psy", "Bio", "Cyber", "Mystic", "Nova", "Omega", "Alpha"
        ]
        
        self.suffixes = [
            "Blast", "Form", "Control", "Strike", "Vision", "Armor", "Flight", "Surge",
            "Grasp", "Shield", "Wave", "Beam", "Cloak", "Fist", "Whip", "Field", "Aura",
            "Pulse", "Burst", "Step", "Leap", "Gaze", "Touch", "Voice"
        ]
        
        self.power_types = [
            "Elemental", "Physical", "Mental", "Energy", "Dimensional", "Biological",
            "Technological", "Mystical", "Temporal", "Spatial"
        ]
        
        self.intensities = {
            "Weak": 30, 
            "Moderate": 40, 
            "Strong": 20, 
            "Extreme": 8, 
            "Omega": 2
        }
        self.intensity_choices = [i for i, w in self.intensities.items() for _ in range(w)]
        
        # Description components
        self.actions = [
            "generate", "manipulate", "absorb", "project", "transform into", "summon",
            "control", "create", "teleport", "phase through", "enhance", "weaken",
            "heal", "corrode", "illuminate", "conceal", "accelerate", "slow",
            "disintegrate", "reconstruct", "amplify", "nullify", "duplicate", "merge with"
        ]
        
        self.targets = [
            "matter", "energy", "light", "darkness", "time", "space", "thoughts", "emotions",
            "metal", "fire", "ice", "electricity", "sound", "gravity", "life force", "memories",
            "shadows", "radiation", "plasma", "kinetic force", "potential energy", "organic material",
            "data", "dimensional barriers"
        ]
        
        self.effects = [
            "explosive bursts", "precise beams", "protective fields", "healing waves",
            "corrosive clouds", "illusions", "force constructs", "temporal distortions",
            "spatial warps", "mental pulses", "biological mutations", "technological overrides",
            "elemental storms", "gravitational pulls", "sonic vibrations", "psychic projections"
        ]
        
        self.limitations = [
            "limited by energy reserves", "affected by certain materials", "requires concentration",
            "has a cooldown period", "drains stamina", "works better at night", "more potent in sunlight",
            "weaker against opposite elements", "range limited", "requires line of sight",
            "affected by electromagnetic fields", "less effective on living targets"
        ]
    
    def generate_superpower(self):
        """
        Generates a random superpower with name, intensity, type, and description.
        """
        # Generate power
        name = f"{random.choice(self.prefixes)} {random.choice(self.suffixes)}"
        intensity = random.choice(self.intensity_choices)
        power_type = random.choice(self.power_types)
        
        # Generate description
        description = (
            f"Allows the user to {random.choice(self.actions)} {random.choice(self.targets)}, "
            f"creating {random.choice(self.effects)}. "
        )
        
        # Add intensity-specific details
        if intensity == "Weak":
            description += f"This power is {random.choice(['basic', 'simple'])} and {random.choice(self.limitations)}."
        elif intensity == "Moderate":
            description += f"This power is {random.choice(['versatile', 'reliable'])} but {random.choice(self.limitations)}."
        elif intensity == "Strong":
            description += f"This {random.choice(['advanced', 'potent'])} power can affect {random.choice(['large areas', 'multiple targets'])}."
        elif intensity == "Extreme":
            description += f"This {random.choice(['devastating', 'reality-warping'])} power can {random.choice(['alter landscapes', 'affect cities'])}."
        else:  # Omega
            description += f"This {random.choice(['cosmic', 'godlike'])} power can {random.choice(['reshape reality', 'affect planetary systems'])}."
        
        # 30% chance for an additional effect
        if random.random() < 0.3:
            description += f" Additionally, it can {random.choice(self.actions)} {random.choice(self.targets)} in a {random.choice(['minor', 'secondary'])} way."
        
        return {
            "Name": name,
            "Intensity": intensity,
            "Type": power_type,
            "Description": description
        }
    
    def play(self):
        """Main game loop for superpower generator"""
        print("\n🦸 Welcome to the Superpower Generator! 🦸")
        print("Generate random superpowers for your characters!")
        print("="*50)
        
        while True:
            try:
                # Get number of powers to generate
                num_input = input("\nHow many superpowers would you like to generate? (1-10): ").strip()
                
                if not num_input.isdigit():
                    print("Please enter a valid number.")
                    continue
                
                num_powers = int(num_input)
                if num_powers < 1 or num_powers > 10:
                    print("Please enter a number between 1 and 10.")
                    continue
                
                print(f"\n🎲 Generating {num_powers} superpower(s)...")
                print("="*50)
                
                # Generate and display powers
                for i in range(num_powers):
                    power = self.generate_superpower()
                    print(f"\n--- Power {i+1} ---")
                    print(f"Name: {power['Name']}")
                    print(f"Intensity: {power['Intensity']}")
                    print(f"Type: {power['Type']}")
                    print(f"Description: {power['Description']}")
                    print("-" * 40)
                
                # Ask if user wants to generate more
                again = input("\nGenerate more superpowers? (y/n): ").strip().lower()
                if again != 'y':
                    break
                    
            except KeyboardInterrupt:
                print("\nSuperpower generator cancelled.")
                break
            except Exception as e:
                print(f"An error occurred: {e}")

def generate_powers(num_powers=1):
    """Legacy function for backward compatibility"""
    if num_powers <= 0:
        print("Please specify a positive number of powers to generate.")
        return
    
    game = SuperpowerGame()
    results = []
    for i in range(num_powers):
        power = game.generate_superpower()
        results.append(f"--- Power {i+1} ---")
        results.append(f"Name: {power['Name']}")
        results.append(f"Intensity: {power['Intensity']}")
        results.append(f"Type: {power['Type']}")
        results.append(f"Description: {power['Description']}\n")
    
    print("\n".join(results))

def main():
    """Standalone main function for running Superpower generator directly."""
    game = SuperpowerGame()
    game.play()

if __name__ == "__main__":
    main()