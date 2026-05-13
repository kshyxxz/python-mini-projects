import matplotlib.pyplot as plt
import pandas as pd

def plot_graph():
	print("Choose the graph type:")
	print("1. Line Graph")
	print("2. Bar Graph")
	print("3. Scatter Plot")
	choice = input("Enter your choice (1/2/3): ")	

	if choice not in ['1', '2', '3']:
		print("Invalid choice. Please select 1, 2, or 3.")
		return

	print("Choose the data source:")
	print("1. CSV File")
	print("2. Manual Input")
	data_choice = input("Enter your choice (1/2): ")

	if data_choice not in ['1', '2']:
		print("Invalid choice. Please select 1 or 2.")
		return
	
	if data_choice == '1':
		file_path = input("Enter the path to the CSV file: ")
		try:
			data = pd.read_csv(file_path)
			x = data.iloc[:, 0]
			y = data.iloc[:, 1]
		except Exception as e:
			print(f"Error reading the file: {e}")
			return
		
	elif data_choice == '2':
		x = input("Enter the x values (comma separated): ")
		y = input("Enter the y values (comma separated): ")
		try:
			x = list(map(float, x.split(',')))
			y = list(map(float, y.split(',')))
		except ValueError:
			print("Invalid input. Please enter numeric values.")
			return

	if choice == '1':
		plt.plot(x, y)
		plt.title("Line Graph")
	elif choice == '2':
		plt.bar(x, y)
		plt.title("Bar Graph")
	elif choice == '3':
		plt.scatter(x, y)
		plt.title("Scatter Plot")

	plt.xlabel("X-axis")
	plt.ylabel("Y-axis")
	plt.grid()
	plt.show()	

if __name__ == "__main__":
	plot_graph()