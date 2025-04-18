import random

# Number of rounds
rounds = 5
score = 0

print("Welcome to the High-Low Game!")
print(f"You will play {rounds} rounds.\n")

for round_num in range(1, rounds + 1):
    user_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    
    print(f"Round {round_num}:")
    print(f"Your number is: {user_number}")
    
    guess = input("Do you think your number is higher or lower than the computer's? (Enter 'higher' or 'lower'): ").lower()
    
    # Determine the correct answer
    if user_number > computer_number:
        correct_answer = "higher"
    elif user_number < computer_number:
        correct_answer = "lower"
    else:
        correct_answer = "equal" 
    
    print(f"The computer's number was: {computer_number}")
    
    if guess == correct_answer:
        print("You guessed right! +1 point.\n")
        score += 1
    elif correct_answer == "equal":
        print("Both numbers are equal! No points this round.\n")
    else:
        print("Wrong guess. No points this round.\n")


print(f"Game Over! Your total score is: {score} out of {rounds}")
