import numpy as np

def power_method(A, x0, epsilon=1e-6, max_iter=1000):
    x = x0
    for i in range(max_iter):
        x_next = np.matmul(A, x)
        lambda_next = np.linalg.norm(x_next, 2)
        x_next /= lambda_next
        if np.abs(lambda_next - np.linalg.norm(x, 2)) < epsilon:
            return lambda_next, x_next
        x = x_next
    return lambda_next, x_next

# Example usage
A = np.array([[3, 1], [1, 3]])
x0 = np.array([1, 1])
eigenvalue, eigenvector = power_method(A, x0)
print("Eigenvalue: ", eigenvalue)
print("Eigenvector: ", eigenvector)