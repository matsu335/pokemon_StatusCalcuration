
import tkinter as tk

root = tk.Tk()
root.geometry("350x100")

run_button = tk.Button(root, text = "Run")
run_button.place(x = 160, y = 40)

set_button = tk.Button(root, text = "Set")
set_button.place(x = 300, y = 7)

input_box = tk.Entry(width = 40)
input_box.place(x = 10, y = 10)

statusbar = tk.Label(root, text =  " No Data!!", bd = 1, relief = tk.SUNKEN, anchor = tk.W)
statusbar.pack(side = tk.BOTTOM, fill = tk.X)

root.mainloop()