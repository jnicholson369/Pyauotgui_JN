import random

words = ["dog","orange","mouse","tide pods","bleach"]

hint1 = ["tail","color","small","yummy snack","a yummy snack",]

hint2 = ["woof","fruit","eats cheese","is a ded meme"," it cleans",]

number = random.randint(0,4)

secretword = words[number]

guess = ""

counter = 0

while True:
    print("guess the secret word!")
    print("Type 'hint1','hint2','length',first letter',or 'give up' if you need help.")
    guess = input()

    if guess == secretword:
        counter +=1
        print("you win!")
        print("it took you " + str(counter) + " guesses.")
        break
    elif guess == "hint1":
        print(hint1[number])

    elif guess == "hint2":
        print(hint2[number])

    elif guess == "length":
        print( len(secretword) )

    elif guess == "first letter":
        print( secretword[0] )

    elif guess == "last letter":
        print(secretword[-1] )

    elif guess == "give up":
        print( "your weak... the secret word was " + secretword )
        break
    
    else:
        print("try again.")
        counter +=1
