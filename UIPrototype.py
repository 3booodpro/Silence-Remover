from customtkinter import *

set_appearance_mode("dark")
root = CTk()
root.title("Test")
root.geometry("1280x720")

canvas = CTkCanvas(root,bg="#242424")
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

update_time = 1
line_x = 0
line_y = 0
line_fx = canvas.winfo_width()
line_fy = canvas.winfo_height()
line_speed = 1

def update():
    global line_x, line_y, line_fx, line_fy
    canvas.delete('all')
    canvas.create_line(line_x,line_y,canvas.winfo_width() + line_fx,canvas.winfo_height() + line_fy,fill="purple")
    line_x += line_speed
    line_fx -= line_speed
    root.after(update_time,update)

root.after(update_time,update)
root.mainloop()