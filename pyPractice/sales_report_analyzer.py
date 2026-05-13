import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
	try:
		print("Loading Data...")
		data = pd.read_csv(file_path)  
		print("Data Loaded Successfully!")
		return data
	except Exception as e:
		print(f'{e}')
		return None
	
def clean_data(data):
	print("Cleaning Data...")
	data['Product_Category'] = data['Product_Category'].fillna("Unknown")
	data = data.dropna()

	data['Date'] = pd.to_datetime(data['Date'])
	data['Sales_Amount'] = pd.to_numeric(data['Sales_Amount'], errors='coerce')

	data['Year_Month'] = data['Date'].dt.to_period('M')
	if ('Qunatity' and 'Price') in data.columns:
		data['Revenue'] = data['Quantity'] * data['Price']

	print("Data Cleaned Successfully!")
	return data

def analyze_data(data):
	print("Sales Insights")

	monthly_sales = data.groupby('Year_Month')['Sales_Amount'].sum()
	print(monthly_sales)

	if 'Revenue' in data.columns:
		top_products = data.groupby('Product_Name')['Revenue'].sum().sort_values(ascending=False).head()
		print(top_products)

	monthly_sales.plot(kind="bar", figsize=(10,6), color="skyblue")
	plt.title("Monthly Sales")
	plt.xlabel("Month")
	plt.ylabel("Total Sales")
	plt.xticks(rotation=45)
	plt.show()

def main():
	print("Sales Data Analyzer")
	print("Enter 1 to add file path or 2 to use default path (sales_data.csv)")
	choice = input("Enter your choice: ")
	if choice == "1":
		file_path = input("Enter the path to the sales data CSV file: ")
	else:
		file_path = 'sales_data.csv'
	data = load_data(file_path)
	if data is not None:
		cleaned_data = clean_data(data)
		analyze_data(cleaned_data)

if __name__ == "__main__":
	main()