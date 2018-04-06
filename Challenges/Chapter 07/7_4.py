list = ["1","2","3","4","5","6","7","8","9","10"]

while True:
    guess = input("Guess a number on the list (or 'q' to quit): ")
    if guess == 'q':
        print("Goodbye.")
        break
    elif guess in list:
        print("You got it!")
    else:
        print("Better luck next time.")

'''
Better solution containing error handling in the event that the user
enters a string other than 'q':

numbers = [11, 32, 33, 15, 1]

while True:
    answer = input("Guess a number or type q to quit.")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("please type a number or q to quit.")
    if answer in numbers:
        print("You guessed correctly!")
    else:
        print("You guessed incorrectly!")
'''
