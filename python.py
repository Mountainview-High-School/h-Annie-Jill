import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="helo welcome")
label.pack()
button = tk.Button(root, text="click", width=25,)
button.pack()
root.mainloop()