from itertools import combinations
from pprint import pprint

L, N = map(int, input().split())

P = []

for i in range(N):
    v, w = map(int, input().split())
    P.append((v, w))


S = len(P)
combs = []


for len in range(1, S + 1):
    for comb in combinations(P, len):
        combs.append(comb)


best = []

for i in combs:
    weight = 0
    value = 0
    for v, w in i:
        weight += w
        value += v
    
    # print(f"{i} - V: {value} W: {weight}")

    if not best:
        best = [i, [value, weight]]

    if weight <= L and value > best[-1][0]:
        best = [i, [value, weight]]


# print("- - -The best - - -")
print(f"{best[-1][0]}")

