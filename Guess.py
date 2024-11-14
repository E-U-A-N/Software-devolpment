import random

def play_single_round(): #creating function
    random_number=random.randint(0,100) #creating random number between 1 and 100 and giving it a variable 
    attempts = 0 
    max_attempts=10
    guess= None # a variable thats empty so it can store user guess


    while random_number!=guess: # while the random number is not equal to the user guess
        print(f"You have {max_attempts} attempts to guess the number")
        attempts = attempts + 1 # everytime this loop goes round the value of attempts will increase by 1
        max_attempts = max_attempts - 1 #everytime this loop goes round the value of max attempts will decrease by 1

        if attempts > 10: #if the user does not guess the correct number within 10 attempts
            print("You have ran out of guesses, game over, try again")
            print(f"Game over the number was {random_number}")
            random_number = random.randint(1,100) #reset the random number to a new one
            attempts = 0 #reset attempts to zero
            max_attempts = 10 # reset max attempts to 10

        try:
            guess = int(input("Guess a number between 1 and 100?"))

        except ValueError: #if the user eneters an incorrect data type like a string return this
            print("Incorrect data type")
            pass
            

        try:
            if guess < random_number: #if guess is more than random number
                print("To low")
            elif guess > random_number: #if guess is less than random number
                print("To high")
            else:
                guess == random_number
                print(f"well done you guessed correctly it only took {attempts} attempts")  #if guess is eqaul to random number
        except ValueError:
            print("Incorrect data type")
            pass
play_single_round()# calling function