import numpy as np

def get_matrix():
	try:
		rows = int(input("Enter the number of rows : "))
		columns = int(input("Enter the number of columns : "))

		elements = []
		for _ in range(rows):
			row = list(map(float, input().split()))
			if len(row) != columns:
				raise ValueError("Number of columns doesn't match.")
			elements.append(row)
		return np.array(elements)
	except Exception as e:
		print("Error : ", e)

def matrix_operations(A, B):
	print("Matrix A : \n", A)
	print("Matrix B : \n", B)

	try:
		print("Addition : \n", A + B)
	except ValueError as e:
		print("Error in addition : ", e)

	try:
		print("Subtraction : \n", A - B)
	except ValueError as e:
		print("Error in subtraction : ", e)

	try:
		print("Dot Product : \n", np.dot(A, B))
	except ValueError as e:
		print("Error in dot product : ", e)

	try:
		print("Element-wise Multiplication : \n", A * B)
	except ValueError as e:
		print("Error in element-wise multiplication : ", e)

	print("Transpose of A : ", A.T)
	print("Transpose of B : ", B.T)

	try:
		print("Determinant : ", np.linalg.det(A))
	except ValueError as e:
		print("Error in determinant : ", e)
	try:
		print("Inverse : ", np.linalg.inv(A))
	except ValueError as e:
		print("Error in inverse : ", e)

def main():
	A = get_matrix()
	B = get_matrix()
	matrix_operations(A, B)

if __name__ == "__main__":
	main()
