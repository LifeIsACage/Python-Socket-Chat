#
#! ERROR: can't use s.accept() inside mainloop (can't have loop in loop)
# TODO 1. Recieve and Send data to clients
#
import socket
import tkinter
import sys
import random
import threading

port = random.randrange(1024, 65534)
#* Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostbyname(socket.gethostname()), port))
s.listen(5)

def GetHosts(socket):
    conn, adr = socket.accept()
    listbox.insert(0, adr[0])

#x = threading.Thread(GetHosts, ())
#x.start()   

#? Tkinter
tk = tkinter.Tk()
tk.geometry("400x400")
tk.title("Server")

text1 = tkinter.Label(tk, text=f"Server IP: {socket.gethostbyname(socket.gethostname())}", font="Arial 15", width=150, anchor=tkinter.NW)
text2 = tkinter.Label(tk, text=f"Server PORT: {port}", font="Arial 15", anchor=tkinter.NW, width=300)
listbox = tkinter.Listbox(tk, width=400, height=300, font="Arial 15")


text1.pack();text2.pack();listbox.pack()
tk.mainloop()
