#
#TODO 1. Connect with socket
#TODO 2. Send data through socket
#TODO 3. Recieve data from server and send them into listbox
#
import tkinter
import socket
import multiprocessing

from tkinter.messagebox import showinfo

connected = False #!Change to False if server.py is finished)

def sendmsg(_):
    global client
    if entrypoint.get().replace(" ", "") != "":
        client.send(entrypoint.get().encode("utf-8"))
        entrypoint.delete(0, len(entrypoint.get())) # Delete message
    else:
        entrypoint.delete(0, len(entrypoint.get())) # Delete message

def get_data(client):
    data = client.recv(1024).decode()
    listbox.insert(0, data)

#TODO Server connecting
def connect_server():
    global client
    #? Connect to the server
    client.connect((ipinput.get(), int(portinput.get())))
    p1 = multiprocessing.Process(target=get_data,args=(client,))
    p1.start()
    #? Prepare chat
    ipinput.destroy()
    portinput.destroy()
    connectbutt.destroy()
    textIP.destroy()
    textPORT.destroy()
    tk.geometry("600x385")
    #return client

if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tk = tkinter.Tk()   
    tk.geometry("300x240")
    tk.config(background="#1f1f1f"); tk.title(f"Client: {socket.gethostbyname(socket.gethostname())}")
    tk.resizable(False, False)
    
    textIP = tkinter.Label(tk, font="Arial 15", fg="#f5f0f0", text="Server IP", background="#272629")
    textPORT = tkinter.Label(tk, font="Arial 15", fg="#f5f0f0", text="Server PORT", background="#272629")
    ipinput = tkinter.Entry(tk, width=20,font="Arial 15", background="#272629",
                                borderwidth=0, fg="#f5f0f0", selectbackground="#B2B2B2", selectforeground="#2E2E2E", justify=tkinter.CENTER)
    
    portinput = tkinter.Entry(tk, width=20,font="Arial 15", background="#272629",
                                borderwidth=0, fg="#f5f0f0", selectbackground="#B2B2B2", selectforeground="#2E2E2E", justify=tkinter.CENTER)
    
    connectbutt = tkinter.Button(tk, width=20, height=2, text="Connect", background="#1f1f1f", 
                                fg="#f5f0f0", borderwidth=0,activebackground="#363636", command=connect_server)
    
    listbox = tkinter.Listbox(tk,width=100, height=19, background="#212021", 
                                borderwidth=0, highlightthickness=0, fg="#f5f0f0", font="System 14", selectbackground="#B2B2B2", selectforeground="#2E2E2E")
    
    entrypoint = tkinter.Entry(tk, width=100,font="Arial 15", background="#272629",
                                borderwidth=0, fg="#f5f0f0", selectbackground="#B2B2B2", selectforeground="#2E2E2E")
    
    button = tkinter.Button(tk, width=100, height=2, text="Send", background="#1f1f1f", 
                                fg="#f5f0f0", borderwidth=0,activebackground="#363636", command=lambda: sendmsg(0))
    
    tk.bind("<Return>", sendmsg)
    
    textIP.pack(pady=5);ipinput.pack(pady=25);textPORT.pack();portinput.pack(pady=15);connectbutt.pack();listbox.pack();entrypoint.pack();button.pack()
    tk.mainloop()
