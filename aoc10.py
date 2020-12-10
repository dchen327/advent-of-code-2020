adapters = open('aoc10.txt').read().splitlines()
adapters = list(map(int, adapters))
adapters.sort()

chains = [([0], adapters[:])]
for _ in range(len(adapters)):
    new_chains = []
    for chain, remaining in chains:
        prev_jolt = chain[-1]
        for jolt in remaining:
            if 1 <= jolt - prev_jolt <= 3:
                new_chain = chain[:] + [jolt]
                new_remaining = remaining[:]
                new_remaining.remove(jolt)
                new_chains.append((new_chain, new_remaining))
        chains = new_chains
final_chain = chains[0][0]
diffs = [final_chain[i + 1] - final_chain[i]
         for i in range(len(final_chain) - 1)]
diffs.append(3)
print(diffs.count(1), diffs.count(3))
