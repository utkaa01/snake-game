#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from turtle import Turtle

class Game_over(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.hideturtle()
        self.penup()
    def out(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=("Arial",50,"normal"))

