"""
Pong Arcade Game
-------------------------------------------------------------
"""


import turtle
import time
import sys

# pause = False

def update_score(l_score, r_score, player, score_board):
   if player == "l":
       l_score += 1
   else:
       r_score += 1
       

   score_board.clear()
   score_board.write("Left Player: {} -- Right Player: {}".format(l_score, r_score), 
                     align="center",font=("Arial", 24, "normal"))
   return l_score, r_score, score_board

def end_game_page(player):
    if(player == "l"):
       end_page = turtle.Turtle()
       end_page.speed(0)
       end_page.color("blue")
       end_page.penup()
       end_page.hideturtle()
       end_page.goto(0, 0)
       end_page.write("Congratulations player 1 has won the game",
                     align="center", font=("Arial", 24, "normal"))
    else:
       end_page = turtle.Turtle()
       end_page.speed(0)
       end_page.color("blue")
       end_page.penup()
       end_page.hideturtle()
       end_page.goto(0, 0)
       end_page.write("Congratulations player 2 has won the game",
                     align="center", font=("Arial", 24, "normal"))


def setup_game():
   screen = turtle.Screen()
   screen.title("Pong Game")
   screen.bgcolor("white")
   screen.setup(width=1000, height=600)

   l_paddle = turtle.Turtle()
   l_paddle.speed(0)
   l_paddle.shape("square")
   l_paddle.color("red")
   l_paddle.shapesize(stretch_wid=6, stretch_len=2)
   l_paddle.penup()
   l_paddle.goto(-400, 0)

   r_paddle = turtle.Turtle()
   r_paddle.speed(0)
   r_paddle.shape("square")
   r_paddle.color("black")
   r_paddle.shapesize(stretch_wid=6, stretch_len=2)
   r_paddle.penup()
   r_paddle.goto(400, 0)

   ball = turtle.Turtle()
   ball.speed(40)
   ball.shape("circle")
#    ball.shapesize(2)
   ball.color("blue")
   ball.penup()
   ball.goto(0, 0)
   ball.dx = 10
   ball.dy = -5

   score_board = turtle.Turtle()
   score_board.speed(0)
   score_board.color("blue")
   score_board.penup()
   score_board.hideturtle()
   score_board.goto(0, 260)
   score_board.write("Left Player: 0 -- Right Player: 0",
                     align="center", font=("Arial", 24, "normal"))

   return screen, ball, l_paddle, r_paddle, score_board


def paddle_up(paddle):
    paddle.sety(paddle.ycor() + 20)

def paddle_down(paddle):
    paddle.sety(paddle.ycor() - 20)

def pause_game():
    global pause
    pause = not pause


def pong_game():
   game_components = setup_game()
   screen = game_components[0]
   ball = game_components[1]
   l_paddle = game_components[2]
   r_paddle = game_components[3]
   score_board = game_components[4]
   l_score = 0
   r_score = 0
   global pause 
   pause = False

   screen.listen()
   screen.onkeypress(lambda: paddle_up(l_paddle), "w")
   screen.onkeypress(lambda: paddle_down(l_paddle), "s")
   screen.onkeypress(lambda: paddle_up(r_paddle), "Up")
   screen.onkeypress(lambda: paddle_down(r_paddle), "Down")
   screen.onkeypress(pause_game, "p")

    
   while True:
       if not pause:
           screen.update()
           ball.setx(ball.xcor()+ball.dx)
           ball.sety(ball.ycor()+ball.dy)

           if ball.ycor() > 280:
               ball.sety(280)
               ball.dy *= -1

           if ball.ycor() < -280:
               ball.sety(-280)
               ball.dy *= -1

           if ball.xcor() > 480:
               ball.goto(0, 0)
               ball.dy *= -1
               l_score, r_score, score_board = update_score(l_score, r_score, "l", score_board)
               if(l_score >2):
                   end_game_page("l")
                   time.sleep(5)
                   screen.clear()
                   pong_game()
               continue

           elif ball.xcor() < -480:
               ball.goto(0, 0)
               ball.dy *= -1
               l_score, r_score, score_board = update_score(l_score, r_score, "r", score_board)
               if(r_score >2):
                   end_game_page("r")
                   time.sleep(5)
                   screen.clear()
                   sys.exit()
               continue

           if ((ball.xcor() == 370) and
               (ball.ycor() < r_paddle.ycor()+80) and (ball.ycor() > r_paddle.ycor()-80)):
               ball.setx(360)
               ball.dx *= -1

           if ((ball.xcor() == -370) and
                   (ball.ycor() < l_paddle.ycor()+80) and (ball.ycor() > l_paddle.ycor()-80)):
               ball.setx(-360)
               ball.dx *= -1
       else:
           screen.update()

if __name__ == "__main__":
   pong_game()