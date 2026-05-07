import tkinter as tk

root = tk.Tk()
root.title("Dynamic Button Counter")
root.geometry("400x300")

counter = 0 

def increment_counter():
	global counter
	counter += 1
	label.config(text=f"Count : {counter}")

def reset_counter():
	global counter
	counter = 0
	label.config(text=f"Count : {counter}")

label = tk.Label(root, text="Count : 0", font="Helvetica")
label.pack(pady=10)

button = tk.Button(root, text="Increase by 1", command=increment_counter)
button.pack(pady=10)

reset_button = tk.Button(root, text="Reset Counter", command=reset_counter)
reset_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=10)

root.mainloop()