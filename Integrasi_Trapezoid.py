import time
import numpy as np

def f(x):
    return 4 / (1 + x**2)

def trapezoidal_rule(f, a, b, N):
    """
    Menghitung integral dari f dari a sampai b menggunakan metode trapesium dengan N trapesium.
    """
    h = (b - a) / N
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, N):
        integral += f(a + i*h)
    integral *= h
    return integral

def calculate_pi(N):
    """
    Menghitung estimasi nilai pi menggunakan integral fungsi f(x) = 4 / (1 + x^2) dari 0 sampai 1
    dengan metode trapesium dan N trapesium.
    """
    a = 0.0
    b = 1.0
    pi_estimate = trapezoidal_rule(f, a, b, N)
    return pi_estimate

def compute_rms_error(pi_estimate):
    """
    Menghitung galat RMS dari estimasi pi terhadap nilai referensi pi.
    """
    reference_pi = np.pi
    rms_error = np.sqrt(np.mean((pi_estimate - reference_pi)**2))
    return rms_error

# Variasi nilai N yang akan diuji
Ns = [10, 100, 1000, 10000]

# List untuk menyimpan hasil
results = []

# Menghitung pi, galat RMS, dan waktu eksekusi untuk setiap N
for N in Ns:
    start_time = time.time()
    pi_estimate = calculate_pi(N)
    execution_time = time.time() - start_time
    rms_error = compute_rms_error(pi_estimate)
    results.append((N, pi_estimate, rms_error, execution_time))

# Menampilkan hasil
print("N\tEstimasi Pi\t\tGalat RMS\tWaktu Eksekusi (s)")
print("-" * 60)
for result in results:
    print(f"{result[0]}\t{result[1]:.10f}\t{result[2]:.10f}\t{result[3]:.6f}")
