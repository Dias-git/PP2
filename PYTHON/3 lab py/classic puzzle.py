def solve(numheads, numlegs):       #head, leg
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits

# Проверка
print(solve(35, 94))  # (23, 12)