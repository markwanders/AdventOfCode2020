import re

with open("input.txt") as f:
    data = f.read().split("\n\n")
    passports = [line.replace("\n", " ") for line in data]

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
present = 0
valid = 0
for passport in passports:
    if all(field in passport for field in required):
        present += 1
        fields = passport.split(" ")
        d = {}
        for field in fields:
            i = field.split(":")
            d[i[0]] = i[1]
        if int(d['byr']) not in range(1920, 2003):
            continue
        if int(d['iyr']) not in range(2010, 2021):
            continue
        if int(d['eyr']) not in range(2020, 2031):
            continue
        if d['hgt'].endswith("cm") and int(filter(str.isdigit, d['hgt'])) not in range(150, 194):
            continue
        if d['hgt'].endswith("in") and int(filter(str.isdigit, d['hgt'])) not in range(59, 77):
            continue
        if not (d['hgt'].endswith("in") or d['hgt'].endswith("cm")):
            continue
        if not re.match("^#([0-9a-f]{6})$", d['hcl']):
            continue
        if not d['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            continue
        if not re.match("^([0-9]{9})$", d['pid']):
            continue
        valid += 1
print present
print valid
