import customtkinter as ctk
from tkinter import filedialog, Canvas
import os
from PIL import Image, ImageTk
from tkinter import messagebox
import threading
import time
import pathlib  




#main window
ctk.set_default_color_theme('green')
ctk.set_appearance_mode('light')
window = ctk.CTk()
window.title('Silence Remover')
window.geometry('1024x720')




def click1():
    messagebox.showinfo("Info", "This app can cut the silence parts out of videos or audio files. \nSelect a video or audio file you would like to cut the silence out of.")

#img1 info on click
image_path = os.path.join(os.path.dirname(__file__), 'images/7.png')
image = ctk.CTkImage(light_image= Image.open(image_path), size = (50,50))
image_label = ctk.CTkLabel(window, image = image, text = "")
image_label.place(x = 10, y = 10)
Button1 = ctk.CTkButton(window, command = click1, height = 0, width= 0, image = image, fg_color= 'transparent', text = "", hover_color="green")
Button1.place(x = 10, y = 10)


#frame
font = ctk.CTkFont(family= "Gabriola", size = 25)
frame = ctk.CTkFrame(window)
frame.pack(padx = 70, pady = 25, fill="both", expand = True)

#darkmode toggle
def changeMode():
    val = switch.get()
    if val:
        ctk.set_appearance_mode('dark')
    else:
        ctk.set_appearance_mode('light')

switch = ctk.CTkSwitch(master= frame, text="Dark mode", onvalue= 1, offvalue= 0, command= changeMode, font = font)
switch.place(relx = 0.9, rely=0.9, anchor="center")




#windows explorer select file
apps =[]
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi"), ("Audio Files", "*.mp3;*.wav")])
    if file_path:
        file_name = file_path.split("/")[-1]  # Extract the file name from the path
        file_size = os.path.getsize(file_path)
        size_kb = file_size / 1024
        size_mb = size_kb / 1000
        Text.configure(text=f"\nSelected File:   {file_name}\nFile Size:   {size_mb:.2f} MB")
 

            



# SHOW APP NAME & SIZE BELOW select file (test)
Text = ctk.CTkLabel(frame, text = "", font = font)
Text.place(relx = 0.5, rely = 0.38, anchor = "center")

SELECTFile = ctk.CTkButton(frame, height = 50, width= 80, text = 'Choose a file', command = select_file, font = font)
SELECTFile.place(relx = 0.5, rely = 0.3, anchor = "center")

    
    

def updateprogress():
    progress = 0

    def update():
        nonlocal progress
        progress += 5
        Canvas.itemconfig(progressbar, width = progress)
        if progress < 100:
            Canvas.after(100, update)
        else:
            progress = 0


def move():
    steps = 23
    for i in range (steps + 1):
        value = (i * steps) / 100
        progressbar.set(value)
        time.sleep(1)

def updateonclick():
    t = threading.Thread(target = move)
    t.start()
    
#progress bar

progressbar = ctk.CTkProgressBar(frame, orientation="horizontal")
progressbar.place(relx = 0.5, rely = 0.80, anchor = "center")
progressbar.set(0)


#start button
start = ctk.CTkButton(frame, text = "Start", command = updateonclick, font = font)
start.place(relx = 0.5, rely = 0.7, anchor = "center")




label = ctk.CTkLabel(frame, text = 'Welcome', font = font)
label.pack()

#choose file type
Combobox = ctk.CTkComboBox(frame, state = "readonly", values=['Select export type','mp4', 'mp3'], width = 150, hover=True, button_hover_color='green')
Combobox.place(relx = 0.5, rely = 0.55, anchor ="center")






#test slider
slider = ctk.CTkSlider(frame)
slider.pack()
window.mainloop()



#img2 canceled
#image2_path = os.path.join(os.path.dirname(__file__), 'images/bg.jpg')
#image2 = ctk.CTkImage(light_image= Image.open(image2_path), size = (1024,720))
#wndLab = ctk.CTkLabel(window, image = image2, text = "")
#wndLab.pack()