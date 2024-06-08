import time
import numpy as np

# Fungsi f(x) yang akan diintegralkan
def f(x):
    return 4 / (1 + x**2)

# Metode 1: Integrasi Reimann
def reimann_integration(N):
    dx = 1 / N
    integral_sum = sum(f(x) * dx for x in np.arange(0, 1, dx))
    return integral_sum

# Fungsi untuk menghitung nilai absolut dari galat
def calculate_error(approximation):
    true_value = np.pi
    return np.abs(true_value - approximation)

# Fungsi untuk melakukan pengujian dan mengukur waktu eksekusi
def test_integration_method(method, N_values):
    results = {}
    for N in N_values:
        start_time = time.time()
        approximation = method(N)
        execution_time = time.time() - start_time
        error = calculate_error(approximation)
        results[N] = {'Approximation': approximation, 'Error': error, 'Execution Time (s)': execution_time}
    return results

# Variasi nilai N yang akan diuji
N_values = [10, 100, 1000, 10000]

# Pengujian metode integrasi Reimann
reimann_results = test_integration_method(reimann_integration, N_values)

# Menampilkan hasil pengujian
for N, result in reimann_results.items():
    print(f"N = {N}: Approximation = {result['Approximation']}, Error = {result['Error']}, Execution Time = {result['Execution Time (s)']} seconds")
