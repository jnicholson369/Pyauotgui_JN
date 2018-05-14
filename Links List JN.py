import webbrowser
import pyautogui as pg

videos = ["https://www.youtube.com/watch?v=cRpdIrq7Rbo","https://www.youtube.com/watch?v=qVSy4O3k3u4","https://www.youtube.com/watch?v=NxhVJvCZEPY"]

music = ["https://www.youtube.com/watch?v=gxEPV4kolz0","https://www.youtube.com/watch?v=C1D3G2VGQ_8"]



answer = pg.prompt(
"""
What do you want to do?
a) videos
b) music

"""
    )

if answer == "a":
    for i in videos:
        webbrowser.open(i)

elif answer == "b":
    for i in music:
        webbrowser.open(i)
