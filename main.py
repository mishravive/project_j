import random
youdict = {"stone": 1, "paper": 2, "scissor": 3}
reversedict = {1: "stone", 2: "paper", 3: "scissor"}
user_score = 0
computer_score = 0
draws = 0

while True:
    computer = random.choice([1, 2, 3])#1 = stone , 2 = paper , 3 = scissor
    your_choice = input("Enter your choice :")
    if your_choice in youdict:
      you = youdict[your_choice]
    else:
      print("Invalid choice! Please enter 'stone', 'paper', or 'scissor'.")
      exit()  
    print(f"You chose :{reversedict[you]}\ncomputer chose :{reversedict[computer]}")
    if computer == you:
      print("It's a draw! Try again.")
      draws += 1
    elif (computer == 1 and you == 2) or \
     (computer == 2 and you == 3) or \
     (computer == 3 and you == 1):
      print("You win! Congratulations!")
      user_score += 1
    else:
      print("You lose! Try again.")
      computer_score += 1
    print(f"Scores - You: {user_score}\n Computer: {computer_score}\n Draws: {draws}")

print("Game over!")
print(f"Final Scores - You: {user_score}\n Computer: {computer_score}\n Draws: {draws}")
    