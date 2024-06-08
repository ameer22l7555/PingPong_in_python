import turtle

window = turtle.Screen()
window.title("Ping Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0) 

paddle_a = turtle.Turtle()
paddle_a.speed(0)  
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0) 
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

ball = turtle.Turtle()
ball.speed(40) 
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3 
ball.dy = -0.3 

score_a = 0
score_b = 0

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

def update_score():
    score_display.clear()
    score_display.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

paddle_a_move_up = False
paddle_a_move_down = False
paddle_b_move_up = False
paddle_b_move_down = False

def paddle_a_up():
    global paddle_a_move_up
    paddle_a_move_up = True

def paddle_a_down():
    global paddle_a_move_down
    paddle_a_move_down = True

def paddle_b_up():
    global paddle_b_move_up
    paddle_b_move_up = True

def paddle_b_down():
    global paddle_b_move_down
    paddle_b_move_down = True

def paddle_a_stop_up():
    global paddle_a_move_up
    paddle_a_move_up = False

def paddle_a_stop_down():
    global paddle_a_move_down
    paddle_a_move_down = False

def paddle_b_stop_up():
    global paddle_b_move_up
    paddle_b_move_up = False

def paddle_b_stop_down():
    global paddle_b_move_down
    paddle_b_move_down = False

window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeyrelease(paddle_a_stop_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeyrelease(paddle_a_stop_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeyrelease(paddle_b_stop_up, "Up")
window.onkeypress(paddle_b_down, "Down")
window.onkeyrelease(paddle_b_stop_down, "Down")

def game_loop():
    global paddle_a_move_up, paddle_a_move_down, paddle_b_move_up, paddle_b_move_down

    if paddle_a_move_up and paddle_a.ycor() < 250:
        paddle_a.sety(paddle_a.ycor() + 0.5)
    if paddle_a_move_down and paddle_a.ycor() > -240:
        paddle_a.sety(paddle_a.ycor() - 0.5)
    if paddle_b_move_up and paddle_b.ycor() < 250:
        paddle_b.sety(paddle_b.ycor() + 0.5)
    if paddle_b_move_down and paddle_b.ycor() > -240:
        paddle_b.sety(paddle_b.ycor() - 0.5)
        
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        global score_a
        score_a += 1
        update_score()

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1 
        global score_b
        score_b += 1
        update_score()

    if (ball.dx > 0) and (350 > ball.xcor() > 340) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.dx < 0) and (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

    window.update() 
    window.ontimer(game_loop, 1) 

game_loop()

window.mainloop()
