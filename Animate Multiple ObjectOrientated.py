from tkinter import *
import random
import time

WIDTH = 800
HEIGHT = 600


tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("Bouncing Ball")
canvas.pack()

class Ball():
    def __init__(self, colour, size):
        self.shape = canvas.create_oval(10, 10, size, size, fill=colour)
        self.xspeed =random.randrange(1, 8)
        self.yspeed = random.randrange(1, 8)

    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape)
        if pos[3] >= HEIGHT or pos[1] <= 0: 
            self.yspeed = -self.yspeed
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.xspeed = -self.xspeed
    
newball = Ball("red", 50)
newball2 = Ball("blue", 100)
newball3 = Ball("green", 55)


while True:
    newball.move()
    newball2.move()
    newball3.move()
    tk.update()
    time.sleep(0.01)
tk.mainloop()
