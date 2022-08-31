# Program do obliczania stopnia pokrewieństwa między wnukami jednej babci urodzonymi z dwóch różnych dziadków

import random

def simulate():
    A1 = list(range(0,100))
    B1 = list(range(100,200))
    C1 = list(range(200,300))

    A2 = A1 + B1
    random.shuffle(A2)
    A2 = A2[0:100]

    B2 = A1 + C1
    random.shuffle(B2)
    B2 = B2[0:100]

    C2 = list(range(300,400))
    D2 = list(range(400,500))

    A3 = A2 + C2
    random.shuffle(A3)
    A3 = A3[0:100]

    B3 = B2 + D2
    random.shuffle(B3)
    B3 = B3[0:100]

    # zmień na A2 i B2, jeśli chcesz obliczyć pokrewieństwo w pierwszym pokoleniu 
    return len(set(A3).intersection(B3))

suma = 0
index = 0

powtorzenia = 100000

while index < powtorzenia:
    suma  += simulate()
    index += 1
    
# oblicz średnią wszystkich wyników
print(suma/powtorzenia)
