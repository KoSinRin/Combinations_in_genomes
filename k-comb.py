def find_repeats(genome, k):
    repeats = {}
    for i in range(len(genome) - k + 1):
        kmer = genome[i:i+k]
        if kmer in repeats:
            repeats[kmer] += 1
        else:
            repeats[kmer] = 1
    return repeats

genome = "ATGCATGCATGC"
k = 4
repeats = find_repeats(genome, k)
for kmer, count in repeats.items():
    if count > 1:
        print(f"{kmer}: {count}")