#
#TODO 1. Connect with socket
#TODO 2. Send data through socket
#TODO 3. Recieve data from server and send them into listbox
#
import tkinter
import socket

def sendmsg(_):
    listbox.insert(0, f"{socket.gethostbyname(socket.gethostname())} -> {entrypoint.get()}")
    entrypoint.delete(0, len(entrypoint.get())) # Delete message

tk = tkinter.Tk()
tk.geometry("600x400")
tk.config(background="#1f1f1f"); tk.title(f"Client: {socket.gethostbyname(socket.gethostname())}")

listbox = tkinter.Listbox(tk,width=100, height=19, background="#212021", 
                            foreground="#212021", borderwidth=0, highlightthickness=0, fg="#f5f0f0", font="System 14")

entrypoint = tkinter.Entry(tk, width=100,font="Arial 15", background="#272629",
                            borderwidth=0, fg="#f5f0f0", selectbackground="#B2B2B2", selectforeground="#1E1E1E", )

button = tkinter.Button(tk, width=100, height=3, text="Send", background="#1f1f1f", 
                            fg="#f5f0f0", borderwidth=0,activebackground="#363636", command=lambda: sendmsg(0))


tk.bind("<Return>", sendmsg)

listbox.pack();entrypoint.pack();button.pack()
tk.mainloop()