import time
subjects = ['English','History','Chorus','Math','Manderin','Science']
for i in subjects:
    if i == "Math":
        print("My favorite subject is " + i)
    else:
        print("One of my subjects is " + i)
friends = ['steven','donald','barack','muhamuhd','kim']

for i in friends:
    print(i.title() + " is awesome!")
myname = ""
letters = ['k','i','m',' ','j','o','n','g',' ','u','n']

for i in letters:
    myname = myname + i
    print(myname)
    time.sleep(0.5)

print(myname.title())
