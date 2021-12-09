age_of_george = 25

count = 0
while count < 2:
    guess_age = int(input("Guess Age:"))
    if guess_age == age_of_george:
      print("yes, you got it")
      break

    elif guess_age > age_of_george:
      print("try smaller!")
    else:
      print("try bigger!")

    count = count + 1

else:
    guess_age = int(input("Guess Age:"))
    if guess_age == age_of_george:
      print("yes, you got it")

    elif guess_age > age_of_george or guess_age < age_of_george:
      print("You Lose!")