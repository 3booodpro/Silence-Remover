
from customtkinter import *
from PIL import Image, ImageTk
from math import *
from time import *
from threading import *
set_appearance_mode("dark")
root = CTk()
root.title("Test")
root.geometry("1280x720")

#EXPLORER 
def select_file():
    global count
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi"), ("Audio Files", "*.mp3;*.wav")])
    if file_path:
        deletebutton.pack(side = LEFT)
        file_name = file_path.split("/")[-1]  # Extract the file name from the path
        file_size = os.path.getsize(file_path)
        size_kb = file_size / 1024
        size_mb = size_kb / 1000
        Namesize.configure(text=f"\n         Selected File:   {file_name}\nFile Size:   {size_mb:.0f} MB")
        nextab.place(relx = 0.5, rely = 0.7, anchor = CENTER)


def delete_selection():
    deletebutton.grid_forget()   # Hide the Delete button
    nextab.place_forget()     # Hide the Next button
    Namesize.configure(text="")
      
deletebutton = CTkButton(root, text = "Delete Selection", command = delete_selection)

def next_page():
    label.place_forget()
    file_select_button.pack_forget()
    deletebutton.pack_forget()
    nextab.place_forget()
    Namesize.place_forget()
    frame.place_forget()





canvas = CTkCanvas(root,bg="#242424",highlightthickness=0)
canvas.pack(fill=BOTH,expand=TRUE)
Namesize = CTkLabel(root, text = "", font = ("Aldo the Apache", 16))
Namesize.place(relx = 0.5, rely = 0.55, anchor = "center")
label = CTkLabel(root,text="Silence Remover",font=("Aldo The Apache", 42))
label.place(relx=0.5,rely=0.4,anchor=CENTER)
frame = CTkFrame(root,width=256,height=32,border_width=32,border_color="")
frame.place(relx=0.5,rely=0.5,anchor=CENTER)
frame.propagate(0)



image2 = CTkImage(light_image= Image.open("img11.png"), size = (30,30))
# file_entry = CTkEntry(frame,border_width=0)
# file_entry.pack(side=LEFT,fill=BOTH,expand=True,anchor=CENTER)
file_select_button = CTkButton(frame,text="Select file",fg_color="transparent",width=36, image = image2, font = ("Aldo The Apache", 18), text_color= 'white', command = select_file, hover_color='gray')
file_select_button.pack(fill=BOTH)

previous_time = time()
image = Image.open("BG.png")
image = ImageTk.PhotoImage(image)
speed = 30
offset_x = 0
offset_y = 0


image3 = CTkImage(light_image= Image.open("img12.png"), size = (50,50))
nextab = CTkButton(root, text = "Next", image = image3, fg_color='transparent', width=16, hover_color='gray', border_color='gray', border_width=1, font = ("Aldo The Apache", 18), command= next_page,)

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