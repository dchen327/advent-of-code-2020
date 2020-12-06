groups = open('aoc6.txt').read().split('\n\n')
groups = [g.replace('\n', '') for g in groups]
t = 0
for group in groups:
    t += len(set(group))
print(t)
