#Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат


for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            p = (not(x&y&z)) == (not(x))or(not(y))or(not(z))
            print(f'for {x}, {y}, {z}: ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z  --> {p}')
            #print(((not(x&y&z))) == ((not(x))&(not(y))&(not(z))))