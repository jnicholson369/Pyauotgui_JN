def question(q):
    global answer
    answer = input(q)
    print(answer)

question("What's your name?")

question("How was your summer?")
if answer == "Great":
    question("What did you do?")
    print("Sounds like fun.")
if answer == "Horrible":
    question("Why?")
    print("Well maybe next summer will be better.")
else:
    question("Tell me more.")
    print("Sounds like a good summber.")

question("What is some of your defining charachter traits?")
