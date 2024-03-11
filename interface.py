import tkinter as tk
from tkinter import font

master = tk.Tk()
master.title("Demo Burner Control")
master.attributes('-fullscreen', True)
master.rowconfigure(0, weight=1)
master.rowconfigure(1, weight=2)
master.rowconfigure(2, weight=2)
master.rowconfigure(3, weight=2)
master.rowconfigure(4, weight=1)
master.columnconfigure(0, weight=1)
master.columnconfigure(1, weight=4)
master.columnconfigure(2, weight=1)

large_font = font.Font(family='Helvetica', size=25)


# Tkinter definitions
PowerButton = tk.Button(master, text="Power on", bg="darkgrey", font=large_font,
                        activebackground='darkgrey')
PowerButton.grid(row=1, column=1, sticky="NSEW")
OnLabel = tk.Label(master, text="Machine turned OFF", fg="red", font=large_font)
OnLabel.grid(row=0, column=1, sticky="NSEW")
FANbutton = tk.Button(master, text="Fan off", bg="darkgrey", font=large_font,
                      activebackground='darkgrey')
FANbutton.grid(row=2, column=1, sticky="NSEW")
FANbutton["state"] = "disabled"
#Exitbutton = tk.Button(master, text="Exit", bg="red", font=large_font, activebackground='red')
#Exitbutton.grid(row=3, column=1, sticky="NSEW")
