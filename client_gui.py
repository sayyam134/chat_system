from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar, END
import socket
import threading
import pyglet

pyglet.font.add_file('Iceberg-Regular.ttf')


c=socket.socket()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/sayyamsancheti/Desktop/chat/build/assets/frame1")



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def connect_server():
    IP=ip.get()
    c.connect((IP,9999))
    while True:
        threading.Thread(target= recive).start()
def send_msg():
        b=msg.get()
        display(b)
        c.send(bytes(b,"utf-8"))
        msg.set("")

def recive():
      recived_msg=c.recv(1024).decode()
      display(recived_msg)

window = Tk()

window.geometry("846x673")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 673,
    width = 846,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    134.75,
    44.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    522.5,
    46.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    424.75,
    366.25,
    image=image_image_3
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    425.25,
    367.125,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Iceberg-Regular",32),
)
def display(a):
      a=a+"\n"
      entry_1.configure(state="normal")
      entry_1.insert(END,a)
      entry_1.configure(state="disabled")

entry_1.place(
    x=27.75,
    y=173.25,
    width=795.0,
    height=385.75
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    370.75,
    613.25,
    image=image_image_4
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    370.875,
    613.5,
    image=entry_image_2
)
global msg
msg = StringVar()

entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Iceberg-Regular",32),
    justify="left",
    textvariable=msg
)
entry_2.place(
    x=27.75,
    y=578.25,
    width=686.25,
    height=68.5
)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: send_msg(),
    relief="flat"
)
button_1.place(
    x=729.0,
    y=578.25,
    width=93.75,
    height=70.5
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    710.25,
    45.0,
    image=image_image_5
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    711.0,
    45.0,
    image=entry_image_3
)

ip = StringVar()
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Iceberg-Regular",32),
    textvariable=ip
)
entry_3.place(
    x=599.25,
    y=24.0,
    width=223.5,
    height=40.0
)


button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: connect_server(),
    relief="flat"
)
button_2.place(
    x=27.75,
    y=97.5,
    width=795.0,
    height=58.5
)
window.resizable(False, False)
window.mainloop()
