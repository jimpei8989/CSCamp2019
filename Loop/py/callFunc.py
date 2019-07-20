def calcRank(scores):
    rank = {}
    for i, s in enumerate(sorted(scores, reverse = True)):
        if s not in rank:
            rank[s] = i + 1
    return [rank[s] for s in scores]

N = int(input('Number of students: '))

# scores: a list of (int) scores
scores = [int(x) for x in input('Scores: ').split(' ')]
i = int(input('i: '))

rank = calcRank(scores)

print(rank)
print(rank[i])

# TODO
