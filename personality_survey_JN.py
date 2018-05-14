print("What's your favorite sport?")
sport = input()

if sport == "curling":
    print("Wow, curling is my favorite sport too!")
elif sport == "chess":
    print("Chess is not a sport.")
elif sport == "baseball":
    print("I find that boring.")
else:
    print("Okay then.")

print("What's your favorite school printer?")

schoolprinter = input()
if schoolprinter == "Technology Printer.":  
    print ("That's my favorite printer too!")
elif schoolprinter == "US History":
    print ("Good for last minute Spencer Outline printings.")
else:
    print(" great for you.")

print("What's you favorite book?")
book = input()

if "Harry Potter" in book:
    print("Thats a classic.")
else:
    print("Wow, I have no idea what that is.")

print("What's your favorite song?")
song = input()

if song == "Killing in The Name of":
    print("Are you a heavy mettal fan?")
    answer = input()
    if answer == "Yes":
        print("You must have an interesting personality.")
else:
    print("Wow, someone has a bad taste.")

mycolors = ["blue","green","red","orange"]
print("What's your favorite color?")
color = input()
if color in mycolors:
    print("That's a basic color.")
else:
    print("Good for you.")

      
