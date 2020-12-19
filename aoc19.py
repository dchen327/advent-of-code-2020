rules = {}
for line in open('aoc19.txt').read().splitlines():
    num, rule = line.split(': ')
    rules[num] = rule.strip('"')

print(rules)
valid = [rules['0']]
final = []
while valid:
    s = valid.pop(0)
    if all(c in 'ab ' for c in s):  # done
        final.append(s)
    else:
        s = s.split()
        for i, num in enumerate(s):
            if num not in 'ab':
                for rule in rules[num].split(' | '):
                    prev = s[i]
                    s[i] = rule
                    valid.append(' '.join(s))
                    changed = True
                    s[i] = prev
                break

print(final)
