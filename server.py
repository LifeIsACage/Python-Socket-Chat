#
#! ERROR: can't use s.accept() inside mainloop (can't have loop in loop)
# TODO 1. Recieve and Send data to clients
#
import socket
from string import ascii_letters
import tkinter
import random
import multiprocessing
from datetime import datetime
from os import mkdir
from os.path import exists

port = random.randrange(1024, 65534)
clients = []
addresses = []

logfolder = 'Chat_Logs' # Log Folder

def listen_datas():
    global clients, addresses
    print("Recieving data")
    print(clients)
    while True:
        for client in clients:
            data = client.recv(1024)
            print(data)
            client.send(data)

#? This will save listbox into random Log file
def SaveLog():
    if not exists(logfolder): # Create folder for datas
        mkdir(logfolder)

    randomlogName = "".join(random.choice(ascii_letters) for _ in range(12))
    listbox.insert(tkinter.END, "Closing")
    listbox.insert(0, f"[{datetime.now()}]")
    s=open(f"{logfolder}/LOG-{randomlogName}{random.randrange(0, 999999)}.tmp", "w+") # Create random log files
    get_content = listbox.get(0, tkinter.END)
    for data in get_content:
        s.write(f"{data}\n")
    tk.destroy()
        
def listen_server(server):
    global clients, addresses
    conn, address = server.accept()
    print(conn)
    clients.append(conn)
    addresses.append(address)
    p1 = multiprocessing.Process(target=listen_datas)
    p1.start()
    while True:
        print("Connected socket")
        conn, address = server.accept()
        print (conn, address)
        clients.append(conn)
        addresses.append(address)
        print(clients, address)

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((socket.gethostbyname(socket.gethostname()), port))
    server.listen(20)
    process1 = multiprocessing.Process(target=listen_server, args=(server,))
    process1.start()

    #? Tkinter
    tk = tkinter.Tk()
    tk.geometry("400x400")
    tk.title("Server")
    tk.config(bg="#212021")
    tk.resizable(False, False)
    
    text1 = tkinter.Label(tk, text=f"Server IP: {socket.gethostbyname(socket.gethostname())}", font="Arial 15", width=150, anchor=tkinter.NW, background="#212021", fg="#f5f0f0") # IP text
    text2 = tkinter.Label(tk, text=f"Server PORT: {port}", font="Arial 15", anchor=tkinter.NW, width=300, background="#212021", fg="#f5f0f0") # Port text
    text3 = tkinter.Label(tk, text="Audit Log", font="Arial 14", anchor=tkinter.CENTER, width=300, background="#2e2d2e", fg="#f5f0f0") # Audit log text
    listbox = tkinter.Listbox(tk, width=400, height=300, background="#212021", 
                                borderwidth=0, highlightthickness=0, fg="#f5f0f0", font="System 14", selectbackground="#B2B2B2", selectforeground="#2E2E2E") # Listbox  
    
    text1.pack();text2.pack();text3.pack();listbox.pack()
    
    tk.protocol("WM_DELETE_WINDOW", SaveLog)

    tk.mainloop()
    process1.kill()
