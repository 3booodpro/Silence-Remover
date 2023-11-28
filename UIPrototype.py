from customtkinter import *
from math import *
from time import *

set_appearance_mode("dark")
root = CTk()
root.title("Test")
root.geometry("1280x720")

canvas = CTkCanvas(root,bg="#242424",highlightthickness=0)
canvas.pack(fill=BOTH,expand=TRUE)
label = CTkLabel(root,text="Silence Remover",font=("Gill Sans", 32))
label.place(relx=0.5,rely=0.4,anchor=CENTER)
frame = CTkFrame(root,width=512,height=32,border_width=32,border_color="")
frame.place(relx=0.5,rely=0.5,anchor=CENTER)
frame.propagate(0)

file_entry = CTkEntry(frame,border_width=0)
file_entry.pack(side=LEFT,fill=BOTH,expand=True,anchor=CENTER)
file_select_button = CTkButton(frame,text="#",fg_color="transparent",width=32)
file_select_button.pack(side=RIGHT,fill=BOTH)

class circle:
    global update_time, all_time
    canvas : CTkCanvas = None
    pos_x : int = 0
    pos_y : int = 0
    radius : int = 1
    speed : int = 1
    speed_x_dir : int = 1
    speed_y_dir : int = 1
    previous_time : float = time()

    def __init__(self, canvas : CTkCanvas, pos_x : int = 0, pos_y : int = 0, speed : int = 1) -> None:
        self.canvas = canvas
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = speed
        self.canvas.after(update_time,self.update)
        pass

    def update(self):
        self.canvas.after(update_time,self.update)

        dt = time() - self.previous_time
        self.previous_time = time()

        self.pos_x += self.speed * self.speed_x_dir * dt
        self.pos_y += self.speed * self.speed_y_dir * dt
        self.radius = round(1 + 15 * abs(sin(radians(all_time))))

        if self.pos_x > self.canvas.winfo_width() - self.radius:
            self.speed_x_dir *= -1
            self.pos_x = self.canvas.winfo_width() - self.radius
        elif self.pos_x < self.radius:
            self.speed_x_dir *= -1
            self.pos_x = self.radius
        elif self.pos_y > self.canvas.winfo_height() - self.radius:
            self.speed_y_dir *= -1
            self.pos_y = self.canvas.winfo_height() - self.radius
        elif self.pos_y < self.radius:
            self.speed_y_dir *= -1
            self.pos_y = self.radius
        pass
    
    def draw(self):
        self.canvas.create_aa_circle(self.pos_x,self.pos_y,self.radius)
        pass

update_time = 1
all_time = 0.0
objects_list = [
    circle(canvas,0,0,120)
]

def update():
    global all_time
    canvas.delete('all')
    x_last = 0
    y_last = round(canvas.winfo_height())
    for x in range(1,canvas.winfo_width(),8):
        y = round(canvas.winfo_height()) + 32*sin(radians(x + all_time))
        canvas.create_line(x,y,x,canvas.winfo_height(),width=16,fill="purple")
        canvas.create_aa_circle(x,y,radius=32,fill="purple")
        x_last = x
        y_last = y
    # for i in objects_list:
    #     i.draw()
    all_time += 1.0
    root.after(update_time,update)

root.after(update_time,update)
root.mainloop()