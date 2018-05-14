name = "John Nicholson"

subjects = ["Math","Manderin","Science","English","History",]

print("My name is  " + name)

for i in subjects:
    print("I take " + i + " as one of my classes.")


food_dips = ["Guacamole","Bean dip","mango salsa","Salsa",]

for i in food_dips:
    if i == "Guacamole":
        print("Guacamole is so good because it gots avacods and avacods are good")
    else: print(i + " is really good.")

dips = []

while True:
    print("What is you favorite dip?  Type 'end' to stop program")
    answer = input()
    if answer == "end":
        break
    else:
        dips.append(answer)
for i in dips:
    print(i + " is one of your favoriets.")
    
