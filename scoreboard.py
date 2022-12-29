#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from turtle import *
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("snake_score.txt","r") as f:
            self.high_score=int(float(f.read()))
        self.color("blue")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()
    
    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score:{self.high_score}",align="center",font=("Arial",24,"normal"))

        
        
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("snake_score.txt","w") as f:
                f.write(f"{self.high_score}")
            
        self.score=0
        self.update_score()
    def increase_score(self):
        self.score+=1
        self.update_score()

        
        

        
        
        


