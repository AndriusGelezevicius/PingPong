from tkinter import *
WIDTH = 597
HEIGHT = 350


def player1_move_up(event):
    canvas.move(player1, 0, -10)

def player1_move_down(event):
    canvas.move(player1, 0, 10)

def player2_move_up(event):
    canvas.move(player2, 0, -10)

def player2_move_down(event):
    canvas.move(player2, 0, 10)


window = Tk()
window.geometry("600x400")
window.title("Ping Pong")

canvas = Canvas(window, height=HEIGHT, width=WIDTH, background="black")
player1 = canvas.create_rectangle(10,120,20,200, fill="white")
player2 = canvas.create_rectangle(577,120,587,200, fill="white")
ball = canvas.create_oval(287,140,297,150, fill="white")
canvas.place(x=0, y=50)

window.bind("<w>", player1_move_up)
window.bind("<s>", player1_move_down)
window.bind("<Up>", player2_move_up)
window.bind("<Down>", player2_move_down)
window.mainloop()
