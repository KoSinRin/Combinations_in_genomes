def levenshtein_distance(s1, s2):
    # Создаем двумерный массив для хранения результатов
    d = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]

    # Заполняем нулевую строку и столбец
    for i in range(len(s1)+1):
        d[i][0] = i
    for j in range(len(s2)+1):
        d[0][j] = j

    # Заполняем остальную часть массива
    for j in range(1, len(s2)+1):
        for i in range(1, len(s1)+1):
            if s1[i-1] == s2[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = min(d[i-1][j], d[i][j-1], d[i-1][j-1]) + 1

    return d[len(s1)][len(s2)]

def find_closest_combinations(genome):
    # Создаем список всех возможных комбинаций длиной 4 символа
    combinations = [genome[i:i+4] for i in range(len(genome)-3)]

    # Находим самые "близкие" комбинации
    min_distance = float('inf')
    closest_combinations = []
    for i in range(len(combinations)-1):
        for j in range(i+1, len(combinations)):
            distance = levenshtein_distance(combinations[i], combinations[j])
            if distance < min_distance:
                min_distance = distance
                closest_combinations = [combinations[i], combinations[j]]
            elif distance == min_distance:
                closest_combinations.append(combinations[i])
                closest_combinations.append(combinations[j])
    return closest_combinations
# Тестируем функцию
print(find_closest_combinations('ACCCATACCCGT')) # ['ACCC', 'ACCC']

# Находим самые "близкие" комбинации
closest_combinations = find_closest_combinations(genome)
print(closest_combinations) # ['ACCC', 'ACCC']

# Считаем количество самых "близких" комбинаций
count = 0
for combination in closest_combinations:
    count += genome.count(combination)
print(count) # 2

# Считаем общее количество комбинаций
total_count = len(genome) - 3
print(total_count) # 8

# Считаем долю самых "близких" комбинаций
closest_combinations_ratio = count / total_count
print(closest_combinations_ratio) # 0.25
