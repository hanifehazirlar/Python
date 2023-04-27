def find_fact(x):  # faktoriyel fonsiyonu
    """Bu fonksiyon tek parametrelidir. Girilen sayinin faktoriyelini return eder"""
    çarpim_değeri = 1
    for i in range(x, 0, -1):
        çarpim_değeri *= i
    return çarpim_değeri


def find_hypo(x, y):  # dik ucgende hipotenusu bulma
    return (x ** 2 + y ** 2) ** 0.5


pi = 3.14

e = 2.7182

# 1. yol


def ekok1(x, y):
    for i in range(max(x, y), (x * y + 1)):
        if i % x == 0 and i % y == 0:
            print(i)
            break
