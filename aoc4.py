
passports = open('aoc4.txt').read().split('\n\n')  # split by blank lines
passports = [p.replace('\n', ' ')
             for p in passports]  # replace new lines in passports
req_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
# part 1
t = 0
for passport in passports:
    keys = [pair.split(':')[0] for pair in passport.split()]
    if all(req_key in keys for req_key in req_keys):
        t += 1

print(t)

# part 2
t = 0
for passport in passports:
    key_values = dict([pair.split(':') for pair in passport.split()])
    if all(req_key in key_values for req_key in req_keys):  # fields present
        num_valid_fields = 0
        num_valid_fields += 1920 <= int(key_values['byr']) <= 2002
        num_valid_fields += 2010 <= int(key_values['iyr']) <= 2020
        num_valid_fields += 2020 <= int(key_values['eyr']) <= 2030
        if key_values['hgt'][-2:] == 'cm':
            num_valid_fields += 150 <= int(key_values['hgt'][:-2]) <= 193
        elif key_values['hgt'][-2:] == 'in':  # inches
            num_valid_fields += 59 <= int(key_values['hgt'][:-2]) <= 76
        num_valid_fields += key_values['hcl'][0] == '#' and all(
            c in '0123456789abcdef' for c in key_values['hcl'][1:])
        num_valid_fields += key_values['ecl'] in 'amb blu brn gry grn hzl oth'.split()
        num_valid_fields += len(key_values['pid']) == 9
        t += num_valid_fields == 7

print(t)
