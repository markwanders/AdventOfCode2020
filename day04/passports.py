with open("input.txt") as f:
    data = f.read().split("\n\n")
    passports = [line.replace("\n", "") for line in data]

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid = 0
for passport in passports:
    if all(field in passport for field in required):
        valid+=1
print valid

