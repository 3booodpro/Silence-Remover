import customtkinter as ctk
from tkinter import filedialog
import os
from PIL import Image, ImageTk
from tkinter import messagebox





ctk.set_default_color_theme('green')
ctk.set_appearance_mode('light')
window = ctk.CTk()
window.title('Silence Remover')
window.geometry('1024x720')




def click1():
    messagebox.showinfo("Info", "This app can cut the silence parts out of videos or audio files. \nSelect a video or audio file you would like to cut the silence out of.")

#img1
image_path = os.path.join(os.path.dirname(__file__), 'images/7.png')
image = ctk.CTkImage(light_image= Image.open(image_path), size = (50,50))
image_label = ctk.CTkLabel(window, image = image, text = "")
image_label.place(x = 10, y = 10)
Button1 = ctk.CTkButton(window, command = click1, height = 0, width= 0, image = image, fg_color= 'transparent', text = "", hover_color="green")
Button1.place(x = 10, y = 10)




def changeMode():
    val = switch.get()
    if val:
        ctk.set_appearance_mode('dark')
    else:
        ctk.set_appearance_mode('light')


apps =[]
def runApp():
    filename = filedialog.askopenfilename(initialdir="/", title= "Select File", 
    filetypes= (("Videos","*mp4"), ("Audio", "*.mp3")))
    apps.append(filename)
    
    

font = ctk.CTkFont(family= "Beyond The Mountains", size = 20)
frame = ctk.CTkFrame(window)
frame.pack(padx = 70, pady = 25, fill="both", expand = True)


progressbar = ctk.CTkProgressBar(frame, orientation="horizontal")
progressbar.place(relx = 0.5, rely = 0.10, anchor = "center")
progressbar.set(0)


def move():
    progressbar.start()

def stop():
    progressbar.stop()

start = ctk.CTkButton(frame, text = "Start", command = move)
start.place(relx = 0.5, rely = 0.6, anchor = "center")

bar = int(progressbar.get())
while bar > 0:
    print(bar)
    if bar == 99:
        break



label = ctk.CTkLabel(frame, text = 'Welcome', font = font)
label.pack()

Combobox = ctk.CTkComboBox(frame, values=['Select export type','mp4', 'mp3', 'wav'])
Combobox.place(relx = 0.5, rely = 0.4, anchor ="center")


# PLACE APP NAME BELOW select file
Text = ctk.CTkLabel(frame, text = apps)
Text.place(relx = 0.5, rely = 0.25, anchor = "center")

button = ctk.CTkButton(frame, height = 50, width= 80, text = 'Choose a file', hover_color = 'white', command = runApp)
button.place(relx = 0.5, rely = 0.3, anchor = "center")

switch = ctk.CTkSwitch(master= frame, text="Dark mode", onvalue= 1, offvalue= 0, command= changeMode)
switch.place(relx = 0.9, rely=0.9, anchor="center")


slider = ctk.CTkSlider(frame)
slider.pack()
window.mainloop()



#img2
image2_path = os.path.join(os.path.dirname(__file__), 'images/bg.jpg')
image2 = ctk.CTkImage(light_image= Image.open(image2_path), size = (1024,720))
wndLab = ctk.CTkLabel(window, image = image2, text = "")
wndLab.pack()