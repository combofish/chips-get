import numpy as np

def create_matrix():    
    A = np.mat("0 1 2; 1 0 3;4 -3 8")
    print("A\n",A)
    
    inverse = np.linalg.inv(A)
    print("inverse of A\n", inverse)
    print("Check\n", A * inverse)

def solution():
    A = np.mat("1 -2 1; 0 2 -8; -4 5 9")
    print("A\m",A)
    b = np.array([0, 8, -9])
    print("b\n",b)
    x = np.linalg.solve(A,b)
    print("Solution:",x)
    print("Check\n",np.dot(A,x))

def matrix_det():
    A = np.mat("2 3; 4 5")
    print("|A|(Determinant) = \n",np.linalg.det(A))

def matrix_sigenvalue():
    A = np.mat("3 -2;1 0")
    print("A\n",A)
    print("Eigenvalues\n", np.linalg.eigvals(A))

    eigenvalues, eigenvectors = np.linalg.eig(A)
    print("First tuple of eig\n", eigenvalues)
    print("Second tuple of eig\n", eigenvectors)

    for i in range(len(eigenvalues)):
        print("Left\n", np.dot(A, eigenvectors[:,i]))
        print("Right\n", eigenvalues[i] * eigenvectors[:i])
        print("")

if __name__ == '__main__':
    # create_matrix()
    # solution()
    # matrix_det()
    matrix_sigenvalue()
