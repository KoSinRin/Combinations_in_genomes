from collections import defaultdict

def find_repeats(genome, k):
    if len(genome) < k:
        raise ValueError("Length of genome is less than k")

    repeats = defaultdict(int)
    for i in range(len(genome) - k + 1):
        kmer = genome[i:i+k]
        repeats[kmer] += 1
    return repeats

genome = "ATGCATGCATGC"
k = 4
repeats = find_repeats(genome, k)
for kmer, count in repeats.items():
    if count > 1:
        print(f"{kmer}: {count}")
