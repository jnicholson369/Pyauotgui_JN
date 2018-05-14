import pyautogui as pg

import webbrowser

answer = pg.prompt("""
what site do you want to open?
a)history
b)math
c)english
""")

if answer == "a":
    webbrowser.open("https://sites.google.com/a/gcds.net/spencer-history-8/homework-b-spring")

elif answer == "b":
    webbrowser.open("https://docs.google.com/spreadsheets/d/1DvsGyfK5kHDXkJUC-RVNr3_FevXD4oSkRBlppx3uncM/edit#gid=1609266901")

elif answer == "c":
    webbrowser.open("https://classroom.google.com/c/NTEyNzU0MTMyMVpa")
