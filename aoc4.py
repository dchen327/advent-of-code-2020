
passports = open('aoc4.txt').read().split('\n\n')  # split by blank lines
passports = [p.replace('\n', ' ')
             for p in passports]  # replace new lines in passports
print(passports[0])
