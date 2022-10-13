#
#! ERROR: can't use s.accept() inside mainloop (can't have loop in loop)
# TODO 1. Recieve and Send data to clients
#
import socket
from string import ascii_letters, ascii_lowercase, ascii_uppercase
from time import sleep
import tkinter
import random
import threading
from datetime import datetime

#? This will save listbox into random Log file
def SaveLog():
    randomlogName = "".join(random.choice(ascii_letters) for _ in range(10))
    listbox.insert(tkinter.END, "Closing")
    listbox.insert(0, f"[{datetime.now()}]")
    s=open(f"LOG-{randomlogName}{random.randrange(0, 10000)}.txt", "w+")
    get_content = listbox.get(0, tkinter.END)
    for x in get_content:
        s.write(f"{x}\n")
    tk.destroy()

port = random.randrange(1024, 65534)  # Open random port from 1024-65534
#* Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostbyname(socket.gethostname()), port))
s.listen(5)

#? Tkinter
tk = tkinter.Tk()
tk.geometry("400x400")
tk.title("Server")
tk.config(bg="#212021")

text1 = tkinter.Label(tk, text=f"Server IP: {socket.gethostbyname(socket.gethostname())}", font="Arial 15", width=150, anchor=tkinter.NW, background="#212021", fg="#f5f0f0") # IP text
text2 = tkinter.Label(tk, text=f"Server PORT: {port}", font="Arial 15", anchor=tkinter.NW, width=300, background="#212021", fg="#f5f0f0") # Port text
text3 = tkinter.Label(tk, text="Audit Log", font="Arial 14", anchor=tkinter.CENTER, width=300, background="#2e2d2e", fg="#f5f0f0") # Audit log text
listbox = tkinter.Listbox(tk, width=400, height=300, background="#212021", 
                            borderwidth=0, highlightthickness=0, fg="#f5f0f0", font="System 14", selectbackground="#B2B2B2", selectforeground="#2E2E2E") # Listbox  

text1.pack();text2.pack();text3.pack();listbox.pack()

tk.protocol("WM_DELETE_WINDOW", SaveLog)

tk.mainloop()
