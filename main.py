def f(x):
    # Gantilah ini dengan fungsi yang ingin Anda cari akarnya
    return x**2 - 6*x + 5

def bisection_method(a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        print("Metode biseksi tidak dapat digunakan pada interval ini.")
        return None

    iteration = 0
    while (b - a) / 2.0 > tol and iteration < max_iter:
        c = (a + b) / 2.0
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iteration += 1

    return (a + b) / 2.0

# Contoh penggunaan
a = 3.0  # Batas bawah interval
b = 6.0  # Batas atas interval
tolerance = 0.3  # Toleransi
max_iterations = 4  # Jumlah iterasi maksimum

result = bisection_method(a, b, tolerance, max_iterations)
if result is not None:
    print(f"Akar fungsi adalah {result}")
else:
    print("Metode biseksi tidak konvergen.")
