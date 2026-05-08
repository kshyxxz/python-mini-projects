import tkinter as tk

root = tk.Tk()
root.title("Todo List")
root.geometry("300x400")

def add_task():
	task = task_entry.get()
	if task.strip():
		listbox.insert(tk.END, task)
		task_entry.delete(0, tk.END)

def reset_tasks():
	listbox.delete(0, tk.END)

def delete_task():
	listbox.delete(tk.ACTIVE)

tk.Label(root, text="Enter the task : ").pack(pady=10)
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

task_button = tk.Button(button_frame, text="Enter", command=add_task)
task_button.grid(row=0, column=0, padx=5)

reset_button = tk.Button(button_frame, text="Reset", command=reset_tasks)
reset_button.grid(row=0, column=1, padx=5)

listbox = tk.Listbox(root)
listbox.pack(pady=10)

delete_button = tk.Button(root, text="Delete", command=delete_task)
delete_button.pack(pady=5)

root.mainloop()