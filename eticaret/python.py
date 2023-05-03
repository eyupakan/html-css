from scipy import integrate

def integrand(x):
    return abs(x - 4) + x

result, error = integrate.quad(integrand, 3, 1)

print(result)
