import numpy as np

# Membuat matriks A dan vektor b
A = np.array([[50, 12, -12], [12, 57, -47], [-12, -47, 43]])
b = np.array([40.5, 35.75, -25.75])

# Membuat tebakan awal x0
x0 = np.array([0, 0, 0])

# Toleransi kesalahan
tolerance = 0.0001

# Membuat fungsi Gauss-Seidel
def gauss_seidel(A, b, x0, tolerance):
    D = np.diag(np.diag(A))
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    x = x0
    error = np.linalg.norm(np.dot(A, x) - b)
    while error > tolerance:
        x = np.dot(np.linalg.inv(D - L), np.dot(U, x) + b)
        error = np.linalg.norm(np.dot(A, x) - b)
    return x

# Menjalankan metode Gauss-Seidel
x = gauss_seidel(A, b, x0, tolerance)

# Menampilkan hasil
print("Hasil: x = ", x)
