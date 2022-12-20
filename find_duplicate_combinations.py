from typing import List
from collections import Counter

def find_duplicate_combinations(genome: str, length: int, sort_by: str = "combination") -> List[str]:
    if not isinstance(length, int) or length > len(genome):
        return []
    
    combinations = Counter(genome[i:i+length] for i in range(len(genome) - length + 1))
    result = list(filter(lambda x: combinations[x] > 1, combinations))
    
    combination_to_distance = {}
    
    for combination in result:
        indices = [i for i in range(len(genome)) if genome[i:i+length] == combination]
        distances = [abs(indices[i] - indices[i+1]) for i in range(len(indices)-1)]
        combination_to_distance[combination] = min(distances)
    
    result = [combination for combination in result if combination_to_distance[combination] == min(combination_to_distance.values())]
    
    if sort_by == "frequency":
        result = sorted(result, key=lambda x: combinations[x], reverse=True)
    elif sort_by == "combination":
        result = sorted(result)
    elif sort_by == "distance":
        result = sorted(result, key=lambda x: combination_to_distance[x])
    
    return result

# вызываем функцию
result = find_duplicate_combinations("ACCCATACCCGTTTCCCA", 4)
print(result)
