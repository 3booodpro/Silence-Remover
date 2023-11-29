from customtkinter import *
from PIL import Image, ImageTk
from math import *
from time import *
from threading import *

set_appearance_mode("dark")
root = CTk()
root.title("Test")
root.geometry("1280x720")

canvas = CTkCanvas(root,bg="#242424",highlightthickness=0)
canvas.pack(fill=BOTH,expand=TRUE)
label = CTkLabel(root,text="Silence Remover",font=("Aldo The Apache", 32))
label.place(relx=0.5,rely=0.4,anchor=CENTER)
frame = CTkFrame(root,width=512,height=32,border_width=32,border_color="")
frame.place(relx=0.5,rely=0.5,anchor=CENTER)
frame.propagate(0)

file_entry = CTkEntry(frame,border_width=0)
file_entry.pack(side=LEFT,fill=BOTH,expand=True,anchor=CENTER)
file_select_button = CTkButton(frame,text="#",fg_color="transparent",width=32)
file_select_button.pack(side=RIGHT,fill=BOTH)

previous_time = time()
image = Image.open("BG.png")
image = ImageTk.PhotoImage(image)
speed = 25
offset_x = 0
offset_y = 0

while True:
    canvas.delete('all')
    
    sine_points = [(0,root.winfo_height())]
    for x in range(-8,root.winfo_width() + 8,8):
        y = root.winfo_height() + round(8 * sin(radians(x + speed * time())))
        pos = (x,y)
        sine_points.append(pos)

    for x in range(-64,root.winfo_width() + 64,64):
        for y in range(-64,root.winfo_height() + 64,64):
            canvas.create_image(x - offset_x,y + offset_y,image=image,anchor=NW)

    canvas.create_line(sine_points,fill="#2e2e2e",width=64)
    
    dt = time() - previous_time
    previous_time = time()

    offset_x += speed * dt
    offset_y += speed * dt

    if offset_x >= 64:
        offset_x -= 64
    elif offset_y >= 64:
        offset_y -= 64
    root.update()