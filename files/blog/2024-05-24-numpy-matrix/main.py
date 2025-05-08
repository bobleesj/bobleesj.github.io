import numpy as np

Array = np.matrix([[5, 5, 3], [4, 2, 9], [7, 8, 5]])

print("Max value in the matrix: ", np.amax(Array))
print("Max value in the matrix along axis 0: ", np.amax(Array, axis=0))
print("Max value in the matrix along axis 1: ", np.amax(Array, axis=1))


vec = list(range(10))  # [1, ..., 9]
vec[4:8]  # [4, 5, 6, 7]
vec[-5:-2]  # 5th last to 2nd last => [5, 6, 7]
vec[:-5:-1]  # [9, ..., 0]
vec[::-1]  # [9, ..., 0]

# More matrix slicing
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Select the second row
second_row = X[1, :]

# Select the last column
last_column = X[:,]

# Skip the first row and reverse the columns
modified_X = X[1:, ::-1]

X[1, :]
print(modified_X)

cols = X[0, :] > 1
print(cols)
selected_columns = X[:, cols]
print(selected_columns)

print(X[X > 5])  # [6, 7, 8, 9]
