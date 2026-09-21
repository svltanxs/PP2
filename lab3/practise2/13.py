import random
def guesGame(x):

    rdm = random.randint(1,20)
    print(f"Well,{x}, I am thinking of a number between 1 and 20. \n Take a guess.")
    
    cnt = 0
    while(True):
        number = int(input())
        cnt+=1
        if(number == rdm):
            print(f"Good job,{x}! You guessed my number in {cnt} guesses")
            break
        elif(number > rdm):
            print(f"Your guess is too high.")
        else: print(f"Your guess is too low.")
print("Hello! What is your name?")
x = input()
guesGame(x)

        
    
