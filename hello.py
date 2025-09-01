import random
import argparse

def generate_number():
    """Generate a random 4-digit number as a string."""
    return str(random.randint(1000, 9999))

def cows_and_bulls(secret: str, guess: str):
    """Return (cows, bulls) for a given guess.
    
    cows = correct digit in correct position
    bulls = correct digit in wrong position
    """
    if len(secret) != 4 or len(guess) != 4 or not secret.isdigit() or not guess.isdigit():
        raise ValueError("Both secret and guess must be 4-digit numbers.")

    # cows: correct digit, correct position
    cows = sum(s == g for s, g in zip(secret, guess))
    
    # bulls: correct digit, wrong position
    bulls = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - cows
    return cows, bulls

def play_game(secret_override: str | None = None):
    print("Welcome to the Cows and Bulls Game!")
    secret = secret_override if secret_override else generate_number()
    attempts = 0

    while True:
        guess = input("Enter a 4-digit number: ").strip()
        if not guess.isdigit() or len(guess) != 4:
            print("Invalid input! Please enter a 4-digit number (e.g., 1038).")
            continue
        
        attempts += 1
        cows, bulls = cows_and_bulls(secret, guess)
        print(f"{cows} cows, {bulls} bulls")

        if cows == 4:
            print(f"🎉 Congratulations! You guessed {secret} in {attempts} attempts.")
            break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Play the Cows and Bulls game.")
    parser.add_argument("--secret", help="Set a fixed 4-digit secret (for demo/testing).", default=None)
    args = parser.parse_args()
    play_game(args.secret)
