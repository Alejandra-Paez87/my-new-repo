"""Módulo para imprimir los números primos menores de 100."""

import math


def is_prime(n):
    """Devuelve True si n es un número primo, False en caso contrario."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def main():
    """Imprime todos los números primos menores de 100."""
    for i in range(100):
        if is_prime(i):
            print(i, end=' ')
    print()


if __name__ == '__main__':
    main()
