#!/usr/bin/env python
# coding: utf-8

# In[1]:


from snake import Snake      
from snake_food import Food
from game_over import Game_over
from scoreboard import Scoreboard
        
        


from turtle import RawTurtle,Screen
import time

def snake_game():
    
    s=Screen()
    s.setup(width=600,height=600)
    s.bgcolor("cyan")
    s.tracer(0)

    snake=Snake()
    food=Food()
    scoreboard=Scoreboard()
    game=Game_over()

    s.listen()
    s.onkey(snake.up,"Up")
    s.onkey(snake.down,"Down")
    s.onkey(snake.right,"Right")
    s.onkey(snake.left,"Left")



    chances=3
    game_is_on=True
    while game_is_on:
        s.update()
        time.sleep(0.1)
        snake.move()
        if snake.head.distance(food)<15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        if snake.head.xcor()<-290 or snake.head.xcor()>280 or snake.head.ycor()<-290 or snake.head.ycor()>280:


            scoreboard.reset()
            snake.reset()
            chances-=1
            if chances==0:
                game_is_on=False
                game.out()




        for segment in snake.segments[1:]:
            if segment==snake.head:
                pass
            elif snake.head.distance(segment)<10:
                scoreboard.reset()
                snake.reset()
                chances-=1
                if chances==0:
                    game_is_on=False
                    game.out()



    s.exitonclick()


# In[2]:


import turtle
import tkinter as tk
import tkinter.messagebox as tmsg


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.p1=tk.PhotoImage(file="anaconda.png")
        self.master.iconphoto(False,self.p1)
        self.canvas = tk.Canvas(master)
        self.canvas.config(width=600, height=600,bg="white")
        self.canvas.pack(side="right")
        self.oval=self.canvas.create_oval(5,5,248,198,fill="black")
        self.photo=tk.PhotoImage(file="snake.png")
        self.label=tk.Label(image=self.photo)
        self.label.pack()
        self.button = tk.Button(self.canvas, text="Start", command=self.press)
        self.button.config(bg="green",fg="white",width=10,height=5)
        self.button.pack()
       
        self.button = tk.Button(self.canvas, text="About", command=self.about)
        self.button.config(bg="green",fg="white",width=10,height=5)
        self.button.pack()

    def do_stuff(self):
        self.master.destroy()
        snake_game()
        
    def press(self):
        self.do_stuff()

 
        
    def about(self):
        tmsg.showinfo("snake_game","designed by utsav")
        

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()


# In[ ]:




