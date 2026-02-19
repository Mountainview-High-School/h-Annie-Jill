import tkinter as tk

def print_text():
    print("helo welcom")
    label.config(text=click_button)

root = tk.Tk()

button = tk.Button(root, text="click", width=25, command=click_button)
button.pack()

label= tk.Label(root, text="")
label.pack(pady=10)


root.mainloop()