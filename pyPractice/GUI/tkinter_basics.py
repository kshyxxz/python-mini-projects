import tkinter as tk

root = tk.Tk()

root.title("GUI demo")
root.geometry("800x400")

label = tk.Label(root, text="Hi, user!", font="Helvetica")
label.pack(pady=20)

label_instruction = tk.Label(root, text="Enter your name : ", font="Helvetica")
label_instruction.pack(pady=20)

entry = tk.Entry(root, width=20)
entry.pack(pady=20)

def put_name():
	text = entry.get()
	label.config(text=f"Hi, {text}!")

button_enter = tk.Button(root, text="Enter", font="Helvetica", command=put_name)
button_enter.pack(pady=10)

def del_name():
	entry.delete(0,tk.END)
	label.config(text="Hi, user!")

button_reset = tk.Button(root, text="Reset", font="Helvetica", command=del_name)
button_reset.pack(pady=5)

root.mainloop()