impowrt pyautogui as pg
import time
import webbrowser

points = 0

answer = pg.prompt(
"""
You see a live and scary dragon. What do you do?

a) kill the dragon
b) stun the dragon
c) try and keep the dragon as a pet.
d) run from the dragon
e) find an alternitive
"""
    )

if answer == "a":
    points +=1
elif answer == "b":
    points +2
elif answer == "c":
    points +3
elif answer == "d":
    points +4
elif answer == "e":
    points +5

answer = pg.prompt(
"""
your enemy is in mortal danger. What do you do?

a) Let him die
b) do whatever you can to save him, knowing that you are risking your life
c) do some complicated spell to save him and not endanger you
d) do nothing and then feel really bad about it
e) stand there and be confused
"""
    )

if answer == "a":
    points +=1
elif answer == "b":
    points +5
elif answer == "c":
    points +2
elif answer == "d":
    points +4
elif answer == "e":
    points +3
answer = pg.prompt(
"""
Would you rather

a) study
b) hang with your freinds
c) fight evil
d) play with illegal animals
e) find ways to make you live forever
"""
    )

if answer == "a":
    points +=2
elif answer == "b":
    points +4
elif answer == "c":
    points +5
elif answer == "d":
    points +3
elif answer == "e":
    points +1
answer = pg.prompt(
"""
Are you

a) an evil physcopath
b) an extremely smart person
c) a kind but not too smart person
d) a slightly couragous person, but more likely to run from danger and face it at a better time
e) a hero
"""
    )

if answer == "a":
    points +=1
elif answer == "b":
    points +2
elif answer == "c":
    points +3
elif answer == "d":
    points +4
elif answer == "e":
    points +5

#END OF SURVEY
pg.alert("You are...")

#Voldemort
if points < 7:
    pg.alert("Voldemort")
    webbrowser.open("https://media.giphy.com/media/u51RcfpJ1tLRC/giphy.gif")
#Herminone
if points < 11 and points > 6:
    pg.alert("Herminone granger")
    webbrowser.open("https://media.giphy.com/media/YUzHyNHMqo2k/giphy.gifhttps://media.giphy.com/media/YUzHyNHMqo2k/giphy.gif")
#Hagrid
if points < 14 and points > 10:
    pg.alert("Hagrid")
    webbrowser.open("https://media.giphy.com/media/qaHC1oc6fDqDK/giphy.gif")
#RON
if points <17 and points > 13:
    pg.alert("Ronald Weasly")
    webbrowser.open("https://media.giphy.com/media/X7byz3vE1NRGU/giphy.gif")
#Harry
if points <20 and points > 16:
    pg.alert("Harry Potter")
    webbrowser.open("https://media.giphy.com/media/26BRzozg4TCBXv6QU/giphy.gif")



