from collections import defaultdict

groups = open('aoc6.txt').read().split('\n\n')
# part 1
groups_no_spaces = [g.replace('\n', '') for g in groups]
t = sum(len(set(group)) for group in groups_no_spaces)
print(t)

# part 2
t = 0
for group in groups:
    ppl = group.split('\n')
    num_answers = defaultdict(int)
    for person in ppl:
        for answer in person:
            num_answers[answer] += 1
    t += list(num_answers.values()).count(len(ppl))

print(t)
