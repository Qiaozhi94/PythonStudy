age_of_george = 25

for i in range(3):

    guess_age = int(input("Guess Age:"))
    if guess_age == age_of_george:
      print("yes, you got it")
      break

    elif guess_age > age_of_george:
      print("think smaller!")
    else:
      print("think bigger!")


else:
    print("You Lose!")