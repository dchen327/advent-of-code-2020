
passports = open('aoc4.txt').read().split('\n\n')  # split by blank lines
passports = [p.replace('\n', ' ')
             for p in passports]  # replace new lines in passports
req_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
t = 0
for passport in passports:
    keys = [pair.split(':')[0] for pair in passport.split()]
    if all(req_key in keys for req_key in req_keys):
        t += 1

print(t)
