import tkinter
import time
from PIL import Image, ImageTk, ImageSequence, ImageOps


class Gifhandler:
    def __init__(self,parent,canvas,gif,speed,width=126,height=130):      
        self.parent = parent
        self.sequence=self.loadgif(gif)
        self.canvas=canvas
        self.image=self.canvas.create_image(width,height,image=self.sequence[0])
        self.speed=speed
        self.tic=1
        self.stop=False

    def loadgif(self,gif):
        loaded=Image.open(gif)
        sequence=[]
        for img in ImageSequence.Iterator(loaded):
            frame=ImageTk.PhotoImage(img)
            sequence.append(frame)
        return sequence

    def stop_animation(self):
        self.stop=True

    def start_animation(self):
        self.stop=False

    def animate(self):
        if not self.stop:
            self.canvas.itemconfig(self.image, image=self.sequence[self.tic])
            self.tic=(self.tic+1)%len(self.sequence)
            self.parent.after(self.speed,lambda: self.animate())
        else:
            pass

    def animate_noloop(self):
        if not self.stop and not self.tic==(len(self.sequence)-1):
            self.canvas.itemconfig(self.image, image=self.sequence[self.tic])
            self.tic=(self.tic+1)%len(self.sequence)
            self.parent.after(self.speed,lambda: self.animate_noloop())
        else:
            pass

