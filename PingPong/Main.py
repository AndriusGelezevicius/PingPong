from tkinter import *
WIDTH = 597
HEIGHT = 350
xSpeed = 1 #speed of ball
ySpeed = 1

def player1_move_up(event):
    canvas.move(player1, 0, -10)

def player1_move_down(event):
    canvas.move(player1, 0, 10)

def player2_move_up(event):
    canvas.move(player2, 0, -10)

def player2_move_down(event):
    canvas.move(player2, 0, 10)

def move_ball():
    global xSpeed
    global ySpeed
    coordinates = canvas.coords(ball)
    ball_width = coordinates[2] - coordinates[0]
    ball_height = coordinates[3] - coordinates[1]
    print(coordinates)

    player2_coords = canvas.coords(player2)
    if (coordinates[0] <= player2_coords[2] and
            coordinates[1] <= player2_coords[3] and
            coordinates[2] >= player2_coords[0] and
            coordinates[3] >= player2_coords[1]):
        xSpeed = -xSpeed  # Change ball's direction
    player1_coords = canvas.coords(player1)
    if (coordinates[0] <= player1_coords[2] and
            coordinates[1] <= player1_coords[3] and
            coordinates[2] >= player1_coords[0] and
            coordinates[3] >= player1_coords[1]):
        xSpeed = -xSpeed  # Change ball's direction

    #if(coordinates[0]>=(WIDTH - ball_width) or coordinates[0]<0):
     #   xSpeed = -xSpeed

    if(coordinates[1]>=(HEIGHT - ball_width) or coordinates[1]<0):
        ySpeed = -ySpeed

    canvas.move(ball, xSpeed, 0)
    canvas.move(ball, 0, ySpeed)
    window.after(10, move_ball)
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

move_ball()

window.mainloop()
