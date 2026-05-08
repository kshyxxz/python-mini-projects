import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x400")
root.configure(bg="#7aadba")

title_label = tk.Label(root, text="BMI Calculator", bg = "#7aadba", font={"Arial, 18"})
title_label.pack(pady=20)

weight_label = tk.Label(root, text="Enter your weight(kg) : ", bg = "#7aadba")
weight_label.pack(pady=5)
weight_entry = tk.Entry(root, width=20)
weight_entry.pack(pady=5)

height_label = tk.Label(root, text="Enter your height(m) : ", bg = "#7aadba")
height_label.pack(pady=5)
height_entry = tk.Entry(root, width=20)
height_entry.pack(pady=5)

def calculate_BMI():
	try:
		weight = float(weight_entry.get())
		height = float(height_entry.get())
		if weight <=0 or height <= 0:
			raise ValueError("Weight and Height must be greater than 0!")
		else:
			bmi = weight / (height ** 2)
			status = ""
			if bmi < 18.5:
				status = "Underweight"
			elif 18.5 <= bmi < 24.9:
				status = "Normal"
			elif 25 <= bmi < 29.9:
				status = "Overweight"
			else:
				status = "Obesity"

			result_label.config(text=f"BMI : {bmi}")
			status_label.config(text=f"Result : {status}")
	except Exception as e:
		messagebox.showerror(f"{e}")

def reset():
	weight_entry.delete(0, tk.END)
	height_entry.delete(0, tk.END)
	result_label.config(text="")
	status_label.config(text="")

result_label = tk.Label(root, text="", bg = "#7aadba")
result_label.pack(pady=5)
status_label = tk.Label(root, text="", bg = "#7aadba")
status_label.pack(pady=5)

confirm_button = tk.Button(root, text="Calculate", command=calculate_BMI)
confirm_button.pack(pady=20)
reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.pack(pady=20)

root.mainloop()