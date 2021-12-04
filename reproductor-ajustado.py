import pygame 
import tkinter as tkr 
from tkinter.filedialog import askdirectory 
import os 

music_player = tkr.Tk() 
music_player.title("reproductor de phyton") 
music_player.geometry("400x300")

directory = askdirectory()
os.chdir(directory) 
song_list = os.listdir()

play_list = tkr.Listbox(music_player, font="white ", bg="blue", selectmode=tkr.SINGLE,width=44)
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()

var = tkr.StringVar() 
song_title = tkr.Label(music_player, width=40, height=2, font="Helvetica 12 bold", bg="green", fg="white", textvariable=var)

Button1 = tkr.Button(music_player, width=9, height=3, font="Helvetica 12 bold", text="PLAY", command=play, bg="blue", fg="white")
Button2 = tkr.Button(music_player, width=9, height=3, font="Helvetica 12 bold", text="STOP", command=stop, bg="red", fg="white")
Button3 = tkr.Button(music_player, width=9, height=3, font="Helvetica 12 bold", text="PAUSE", command=pause, bg="purple", fg="white")
Button4 = tkr.Button(music_player, width=9, height=3, font="Helvetica 12 bold", text="UNPAUSE", command=unpause, bg="orange", fg="white")

Button1.place(x=0, y=0)
Button2.place(x=100, y=0)
Button3.place(x=200, y=0)
Button4.place(x=300, y=0)
song_title.place(x=0,y=70)
play_list.place(x=0 ,y=110)

music_player.mainloop()