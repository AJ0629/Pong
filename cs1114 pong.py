#AJ Sanon
# CS-UY 1114
# Final project

import turtle
import time
import random

user1x = 0
user2x = 0

ballx = 0
bally = 0

ballvx = 0
ballvy = 0

user1points = 0
user2points = 0


def draw_frame():
    wn = turtle.Screen()
    wn.bgcolor("black")
    turtle.goto(ballx+4, bally)
    #Gives the coordinates for the ball to start, with the +4 centering the ball in the middle of the paddle
    turtle.pendown()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    turtle.circle(8)
    #Draws the ball
    turtle.end_fill()
    turtle.penup()


    turtle.goto(user1x+50, turtle.window_height()/2.25)
    #Centers top paddle position
    turtle.pendown()
    turtle.fillcolor("firebrick")
    #Fill color set as firebrick red
    turtle.begin_fill()
    #Fills in top paddle 

    turtle.right(90)
    #Following block of code draws the top (AI) paddle
    turtle.forward(16)
    #Width of paddle
    turtle.right(90)
    turtle.forward(100)
    #Length of paddle
    turtle.right(90)
    turtle.forward(16)
    turtle.right(90)
    turtle.forward(100)
    turtle.end_fill()
    turtle.penup()
    #Top paddle is drawn

    turtle.goto(user2x+50, turtle.window_height()/-2.55)
    #Centers bottom paddle position 
    turtle.pendown()
    turtle.fillcolor("navy")
    #Fill color as navy
    turtle.begin_fill()
    #Fills in bottom paddle 

    turtle.right(90)
    # Following block of code draws bottom (Player 1) paddle  
    turtle.forward(16)
    #Width of paddle
    turtle.right(90)
    turtle.forward(100)
    #Length of paddle
    turtle.right(90)
    turtle.forward(16)
    turtle.right(90)
    turtle.forward(100)
    turtle.end_fill()
    turtle.penup()
    #Bottom paddle is drawn 

    turtle.goto(200,0)
    #Pen is placed in the middle right of screen 
    turtle.pendown()
    turtle.pencolor("white")
    #Color is now black
    turtle.write("PLAYER 1:" + str(user2points) + "\nAI:" + str(user1points), font =("ms serif", 16, "bold"))
    #Creates counter
    turtle.penup()

def key_left():
    global user2x
    user2x-= 30
    #Moves paddle left 30 frames

def key_right():
    global user2x
    user2x += 30
    #Moves paddle right 30 frames

def reset():
    global user1x, user2x
    global ballvx, ballvy
    global ballx, bally
    user1x, user2x, ballx, bally = 0,0,0,0
    #Resets ball when called
    ballvx = random.choice([-10, 10])
    #Moves the ball horizontally
    ballvy = random.choice([-10, 10])
    #Moves the ball vertically
    
    
def ai():
    global user1x
    if ballx > user1x:
        if bally>0:
            user1x+=12
        #If the ball is to the right of the paddle and above the center
        #paddle moves at  speed of ball to the right
    elif ballx < user1x:
        if bally > 0:
            user1x -= 12
       #If the ball is to the left of the paddle and above center
        #paddle moves at speed of ball to the left
    global user2x


def physics():
    global ballx, bally
    global ballvx, ballvy
    global user1points, user2points
    ballx += ballvx
    bally += ballvy
    
    if ballx >= turtle.window_width()/2:
        #Reflects ball back to the center if the ball hits right wall
        ballvx = -ballvx
        #(Actual reflection)
    if ballx <= -turtle.window_width()/2:
        #Reflects ball back to the center if the ball hits left wall
        ballvx = -ballvx
        #(Actual reflection)


    if bally >= (turtle.window_height()/2.25) -32 and user1x -50 <= ballx<=user1x +50:
        #Reflects ball back towards center if the ball hits the top paddle based on the length of the paddle and position of ball
        ballvy = -ballvy
        #(Actual reflection)
    if bally <=(turtle.window_height()/-2.55)+4 and  user2x-50<=ballx<=user2x + 50:
        #Relects ball back towards center if the ball hits the bottom paddle based on the length of paddle and position of ball
        ballvy = -ballvy
        if user2x-50<=ballx<=user2x:
            ballvx = (-1/2)*ballvx
            #reflects ball back Left
        else:
            ballvx = 2*ballvx
            #Reflects ball back right
    if bally > turtle.window_height() -300:
        #If the ball is higher than the frame, player is given point and ball resets
        user2points += 1
        reset()
    if bally < -turtle.window_height() +300 :
        #If the ball is lower than the frame, AI is given point and ball resets
        user1points += 1
        reset()

def is_game_over():
    if user1points == 5:
        return True
    else:
        return False
        
def read_high_scores():
    scores = open("scores.txt", "a+")
    #Reads scores file, creates said file if it didn't exist
    scores.close()


def update_high_scores():
    read_high_scores()
    global user1points, user2points
    name = input(str("Name:"))
    info = (user2points, name)
    #Tuple made from points and name inputted in shell
    scores = open("scores.txt", "a")
    infoStr = (str(info))
    #Tuple is made a string to be able to be written to file
    scores.write(infoStr +"\n")
    #Tuple is written to a file with a carriage return 
    scores.close()
            

def display_high_scores():
    scores = open("scores.txt", "r").readlines()
    #Scores is made a list of the info tuples
    curr = []
    for elem in scores:
        curr.append((elem))
        #Info tuples appended into curr
        curr.sort(reverse = True)
        #Curr list is order in decreasing order with user2points as parameter
    curr = curr[:10]
    #Curr list shortened to the first 10 tuples
    yPosAcc = 60
    turtle.goto(-305, 80)
    #Pen positioned in upper left of window
    turtle.pendown()
    turtle.write("High Scores:\n", font =("ms serif", 18, "bold"))
    turtle.penup()
    for elem in range(len(curr)):
        results = curr[elem]
        #Individual info tuple selected
        turtle.goto(-305, yPosAcc)
        turtle.pendown()
        turtle.write(results, font = ("ms serif", 12, "bold"))
        #Tuple written underneath High Score
        yPosAcc -= 20
        #Y position of next info tuple lowered
        turtle.penup()
    
def main():
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onkey(key_left, "Left")
    turtle.onkey(key_right, "Right")
    turtle.listen()
    reset()
    while not is_game_over():
        physics()
        ai()
        turtle.clear()
        draw_frame()
        turtle.update()
        time.sleep(0.05)
    update_high_scores()
    display_high_scores()

main()
