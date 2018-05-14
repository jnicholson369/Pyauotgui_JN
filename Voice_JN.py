import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb
speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak("What is your favorite snack?")
answer = pg.prompt("Enter your favorite snack below.")

if answer == "fruit":
    speak.Speak("your healthy, and sad, and need help, and should go home and eat icecream.")

elif answer == "oreos":
    speak.Speak("your fat")

elif answer == "i don't eat snacks":
    speak.Speak("... I don't even know anymore. I thought that humans were improving, and were finally getting better. You just crushed my hopes. WHO DOESN'T SNACK!!! you probably are skinnier than a twig and lie in bed all day eating only two small meals once every day. You are pathetic.")
    

speak.Speak("What's your favorite meme?")

memes = pg.prompt("Enter your favorite meme below.")

speak.SPeak("OK,searching YouTube for dank " + memes + "now.")

wb.open("https://www.youtube.com/results?search_query=" + "dank" + memes + " videos")
