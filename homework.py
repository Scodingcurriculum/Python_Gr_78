dict1= {
      "Eiffel Tower":"France",
      "Taj Mahal":"India",
      "Machu Picchu":"Peru",
      "Pyramids": "Egypt"  
  }
landmarks = list(dict1.keys())
score = 0
while True:
    for i in landmarks: 
      print(f"\nWhere is {i} located? ")
      user_guess = input("Your answer: ")
      if user_guess.lower() == dict1[i].lower():
        print("Correct!")
        score += 1
      else:
        print(f"Wrong! The landmark of {i} is in {dict1[i]}.")
      print(f"Your current score is: {score}")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print(f"Thank you for playing! Your final score is: {score}")
        break



