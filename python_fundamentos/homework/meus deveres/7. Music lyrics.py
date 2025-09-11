import time
import sys

def letra():
    linhas = [
        ('FATHER- father', 0.07),
        ('FATHER- father', 0.07),
        ('FATHER- father', 0.07),
        ('FATHER- father', 0.12),
        ('Father, into you hands i comment my spirit', 0.09),
        ('Father, into you hands-', 0.08),
        ('Why have you forsaken me-', 0.10),
        ('In your eyes, forsaken me-', 0.11),
        ('In your thoughts, forsaken me-', 0.13),
        ('In your heart, forsaken me- oh', 0.17),
    ]

    delay_linhas = [0.5] * len(linhas)

    for i, (linha, tempo) in enumerate(linhas):
        for letra in linha:
            print(letra, end='', flush=True)
            time.sleep(tempo)
        print()
        time.sleep(delay_linhas[i])

if __name__ == '__main__':
    letra()

