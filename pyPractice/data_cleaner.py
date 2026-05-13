import pandas as pd

def load_file(file_path):
	try:
		print("Loading data...")
		df = pd.read_csv(file_path)
		print("Data loaded successfully!")
		return df
	except Exception as e:
		print("Error loading data ", e)
		return None

def clean_data(df):
	print("Cleaning data...")
	print("Initial shape : ",df.shape)

	print("Handling missing values...")
	df = df.fillna(df.mean(numeric_only=True))
	print("Missing values handled.", df.shape)

	print("Removing duplicates...")
	df = df.drop_duplicates()
	print("Duplicates removed.", df.shape)

	return df

def save_file(df, output_path):
	try:
		print("Saving cleaned data...")
		df.to_csv(output_path, index=False)
		print("Data saved successfully!")
	except Exception as e:
		print("Error saving data ", e)

def main():
	print("Enter input file path (default: raw_data.csv): ")
	input_file = input().strip()
	if not input_file:
		input_file = "raw_data.csv"
	print("Enter output file path (default: cleaned_data.csv): ")
	output_file = input().strip()
	if not output_file:
		output_file = "cleaned_data.csv"

	df = load_file(input_file)
	if df is not None:
		cleaned_df = clean_data(df)
		save_file(cleaned_df, output_file)

if __name__ == "__main__":	
	main()