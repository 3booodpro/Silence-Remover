from customtkinter import *
from PIL import Image, ImageTk
from math import *
from time import *
from threading import *
from editor import *

set_appearance_mode("dark")
root = CTk()
root.title("Silence Remover")
root.geometry("1280x720")

#EXPLORER 
def select_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi"), ("Audio Files", "*.mp3;*.wav")])
    if file_path:
        deletebutton.pack(side=LEFT,fill=BOTH)
        file_name = file_path.split("/")[-1]  # Extract the file name from the path
        file_size = os.path.getsize(file_path)
        size_kb = file_size / 1024
        size_mb = size_kb / 1000
        Namesize.configure(text=f"\n         Selected File:   {file_name}\nFile Size:   {size_mb:.0f} MB")
        export5.place(relx = 0.5, rely = 0.55, anchor= CENTER)
        nextab.place(relx = 0.5, rely = 0.65, anchor = CENTER)

def delete_selection():
    deletebutton.pack_forget()   # Hide the buttons
    nextab.place_forget()     
    Namesize.configure(text="")
    export5.place_forget()

def next_page():
    if file_path == "":
        return

    file_select_button.pack_forget()
    deletebutton.pack_forget()
    nextab.place_forget()
    Namesize.place_forget()
    frame.place_forget()
    export5.place_forget()
    
    export_type = None #['One Clip', 'Clip Sequence', 'Premiere', 'Davinci Resolve', 'Final Cut Pro', 'Shotcut']
    if export5.get() == "One Clip":
        export_type = None
    elif export5.get() == "Clip Sequence":
        export_type = "clip-sequence"
    elif export5.get() == "Premiere":
        export_type = "premiere"
    elif export5.get() == "Davinci Resolve":
        export_type = "resolve"
    elif export5.get() == "Final Cut Pro":
        export_type = "final-cut-pro"
    elif export5.get() == "Shotcut":
        export_type = "shotcut"

    CutFile(file_path,export_type)

    global progress_frame
    progress_frame = CTkFrame(root, width = 700, height = 100, fg_color='transparent')
    progress_frame.place(relx = 0.5, rely= 0.45, anchor= CENTER)
    global progress_label
    progress_label = CTkLabel(progress_frame, text="Cutting...", font = ("Aldo the Apache", 26))
    progress_label.place(relx = 0.5, rely = 0.25, anchor = CENTER)
    global progress_bar
    progress_bar = CTkProgressBar(progress_frame, mode="indeterminate", progress_color='#3C9E6D')
    progress_bar.start()  
    progress_bar.place(relx = 0.5, rely = 0.6, anchor= CENTER)
    root.after(1, stopbar, progress_frame, progress_bar)

def mainmenu():
    backtomenu.place_forget()
    finish_label.place_forget()
    progress_label.place_forget()
    progress_frame.place_forget()
    file_select_button.pack(side=LEFT,fill=BOTH,expand=True)
    frame.place(relx=0.5,rely=0.4,anchor=CENTER)

def stopbar(progress_frame, progress_bar):
    if CuttingProgress() == False:
        return
    
    global backtomenu
    global finish_label
    progress_bar.place_forget()
    progress_label.configure(text = "Done!")
    finish_label = CTkLabel(root,text = "File has been saved at the same directory of the selected file", font = (("Aldo the Apache", 20)))
    finish_label.place(relx = 0.5, rely = 0.45, anchor = CENTER)
    progress_label.configure(text_color = "#3C9E6D")

    image4 = CTkImage(light_image=Image.open("images/img14.png"), size=(30,30))
    backtomenu = CTkButton(root, text= "Return to Main Menu", text_color='white', fg_color='transparent', font = ("Aldo the Apache", 26), image=image4, hover_color='#3C9E6D', command=mainmenu)
    backtomenu.place(relx = 0.5, rely = 0.55, anchor = CENTER)
    finished = False

canvas = CTkCanvas(root,bg="#242424",highlightthickness=0)
canvas.pack(fill=BOTH,expand=TRUE)

Namesize = CTkLabel(root, text = "", font = ("Aldo the Apache", 16))
Namesize.place(relx = 0.5, rely = 0.45, anchor = "center")

title_frame = CTkFrame(root,fg_color="transparent",bg_color="transparent")
title_frame.place(relx=0.5,rely=0.3,anchor=CENTER)
label = CTkLabel(title_frame,text="Silence ",font=("Aldo The Apache", 46), text_color='#e3e3e3')
label2 = CTkLabel(title_frame,text="Remover",font=("Aldo The Apache", 46), text_color='#0099cc')
label.pack(side=LEFT)
label2.pack(side=LEFT)


frame = CTkFrame(root,width=256,height=36,border_width=32,border_color="")
frame.place(relx=0.5,rely=0.4,anchor=CENTER)
frame.propagate(0)

export5 = CTkComboBox(root, values= ['One Clip', 'Clip Sequence', 'Premiere', 'Davinci Resolve', 'Final Cut Pro', 'Shotcut'], width= 256, border_color="#484A48", button_color="#484A48", border_width=2, fg_color='#2C2C2C', 
                     text_color='white', font= ("Aldo the Apache", 16), dropdown_font=("Aldo the Apache", 12), state= "readonly", hover=True)
export5.set('One Clip')

#export
export5.lift(aboveThis=frame)
export5.bind("<<ComboboxSelected>>")

image2 = CTkImage(light_image= Image.open("images/img11.png"), size = (30,30))
# file_entry = CTkEntry(frame,border_width=0)
# file_entry.pack(side=LEFT,fill=BOTH,expand=True,anchor=CENTER)
file_select_button = CTkButton(frame,text="Select file",fg_color="transparent",width=36, image = image2,
                                font = ("Aldo The Apache", 18), text_color= 'white', command = select_file, hover_color='#5d91a2'
                                , border_color='#859da8',border_width=float(0.7))
file_select_button.pack(side=LEFT,fill=BOTH,expand=True)

imagedel = CTkImage(light_image= Image.open("images/img13.png"), size = (25,25))
deletebutton = CTkButton(master=frame, text="X", fg_color="transparent", width=36, text_color= 'white' ,
                         hover_color='#9E3C3C', font=("Aldo The Apache", 18), command = delete_selection, image = imagedel
                         ,border_width=1, border_color='#9E3C3C')

previous_time = time()
# image = Image.open("images/BG.png")
# image = ImageTk.PhotoImage(image)
speed = 30
offset_x = 0
offset_y = 0

image3 = CTkImage(light_image= Image.open("images/img12.png"), size = (50,50))
nextab = CTkButton(root, text = "Cut it!", image = image3, fg_color='transparent', width=16, 
                   hover_color='#4b8b60', border_color='#3C9E6D', border_width=1, font = ("Aldo The Apache", 18), command= next_page)

def process():
    global previous_time, image, speed, offset_x, offset_y
    canvas.delete('all')
    
    sine_points = [(0,root.winfo_height())]
    for x in range(-8,root.winfo_width() + 8,8):
        y = root.winfo_height() + round(8 * sin(radians(x + speed * time())))
        pos = (x,y)
        sine_points.append(pos)

    # for x in range(-64,root.winfo_width() + 64,64):
    #     for y in range(-64,root.winfo_height() + 64,64):
    #         canvas.create_image(x - offset_x,y + offset_y,image=image,anchor=NW)

    canvas.create_line(sine_points,fill="#2e2e2e",width=64)
    
    dt = time() - previous_time
    previous_time = time()

    offset_x += speed * dt
    offset_y += speed * dt

    if offset_x >= 64:
        offset_x -= 64
    elif offset_y >= 64:
        offset_y -= 64
    root.after(1,process)

root.after(1,process)
root.mainloop()