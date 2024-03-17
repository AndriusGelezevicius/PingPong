from tkinter import *
import pygame


WIDTH = 597
HEIGHT = 350
xSpeed = 1 #speed of ball
ySpeed = 1
player1_score = 0
player2_score = 0
# Initialize pygame mixer
pygame.mixer.init()
bounce_sound = pygame.mixer.Sound("bounce.mp3")
pygame.mixer.music.load("game_music.mp3")

def player1_move_up(event):
    if canvas.coords(player1)[1] > 0:
        canvas.move(player1, 0, -10)

def player1_move_down(event):
    if canvas.coords(player1)[3] < HEIGHT:
        canvas.move(player1, 0, 10)

def player2_move_up(event):
    if canvas.coords(player2)[1] > 0:
        canvas.move(player2, 0, -10)

def player2_move_down(event):
    if canvas.coords(player2)[3] < HEIGHT:
        canvas.move(player2, 0, 10)

def move_ball():
    global player1_score
    global player2_score
    global xSpeed
    global ySpeed
    coordinates = canvas.coords(ball)
    ball_width = coordinates[2] - coordinates[0]
    ball_height = coordinates[3] - coordinates[1]
    #print(coordinates)

    player2_coords = canvas.coords(player2)
    if (coordinates[0] <= player2_coords[2] and
            coordinates[1] <= player2_coords[3] and
            coordinates[2] >= player2_coords[0] and
            coordinates[3] >= player2_coords[1]):
        bounce_sound.play()
        xSpeed = -xSpeed  # Change ball's direction
    player1_coords = canvas.coords(player1)
    if (coordinates[0] <= player1_coords[2] and
            coordinates[1] <= player1_coords[3] and
            coordinates[2] >= player1_coords[0] and
            coordinates[3] >= player1_coords[1]):
        bounce_sound.play()
        xSpeed = -xSpeed  # Change ball's direction

    if(coordinates[0]>=(WIDTH - ball_width)):
        #xSpeed = -xSpeed
        player1_score += 1
        player1_label.config(text="Player one: " + str(player1_score))
        reset_game()

        print(player1_score)
    elif (coordinates[0]<0):
        player2_score += 1
        player2_label.config(text="Player two: " + str(player2_score))
        reset_game()

    if(coordinates[1]>=(HEIGHT - ball_width) or coordinates[1]<0):
        ySpeed = -ySpeed

    canvas.move(ball, xSpeed, 0)
    canvas.move(ball, 0, ySpeed)
    window.after(10, move_ball)

def reset_game():
    canvas.coords(ball, 287,140,297,150)


window = Tk()
window.geometry("600x400")
window.title("Ping Pong")

canvas = Canvas(window, height=HEIGHT, width=WIDTH, background="black")
player1 = canvas.create_rectangle(10,120,20,200, fill="white")
player2 = canvas.create_rectangle(577,120,587,200, fill="white")
player1_label = Label(window, text="Player one: " + str(player1_score))
player1_label.place(x=225, y=30)
player2_label = Label(window, text="Player two: " + str(player2_score))
player2_label.place(x=325, y=30)
score_label = Label(window, text="Score", font=('Arial', 10, 'bold', 'underline'))
score_label.pack()
ball = canvas.create_oval(287,140,297,150, fill="white")
canvas.place(x=0, y=50)

window.bind("<w>", player1_move_up)
window.bind("<s>", player1_move_down)
window.bind("<Up>", player2_move_up)
window.bind("<Down>", player2_move_down)
pygame.mixer.music.play()
move_ball()

window.mainloop()
