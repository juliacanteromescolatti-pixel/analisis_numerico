#Analisis del determinante para saber si converge 
import numpy as np

# Matriz original del sistema
A = np.array([[1, -1], [1,  1]], dtype=float)

#Descomposición exacta: A = D + L + U 
D = np.diag(np.diag(A))
L = np.tril(A, -1)  # Triangular inferior estricta (ceros en la diagonal)
U = np.triu(A, 1)   # Triangular superior estricta (ceros en la diagonal)

#ANÁLISIS DE JACOBI: T_J = -D^(-1) * (L + U) , (M es d y n es menos (l+u))
M_J = D
N_J = -(L + U)

T_J = np.linalg.inv(M_J) @ N_J

det_TJ = np.linalg.det(T_J)
autovalores_J = np.linalg.eigvals(T_J)
radio_espectral_J = max(abs(autovalores_J))

print("ANÁLISIS DE JACOBI CORREGIDO")
print(f"Determinante de T_J: {det_TJ:.4f}")
print(f"Autovalores de T_J: {autovalores_J}")
print(f"Radio espectral ρ(T_J): {radio_espectral_J:.4f}\n")


#ANÁLISIS DE GAUSS-SEIDEL: T_GS = -(D + L)^(-1) * U
M_GS = D + L
N_GS = -U

T_GS = np.linalg.inv(M_GS) @ N_GS

det_TGS = np.linalg.det(T_GS)
autovalores_GS = np.linalg.eigvals(T_GS)
radio_espectral_GS = max(abs(autovalores_GS))

print("ANÁLISIS DE GAUSS-SEIDEL CORREGIDO")
print(f"Determinante de T_GS: {det_TGS:.4f}")
print(f"Autovalores de T_GS: {autovalores_GS}")
print(f"Radio espectral ρ(T_GS): {radio_espectral_GS:.4f}")