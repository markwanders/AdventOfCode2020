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
            print('byr invalid: %s' % d['byr'])
        elif int(d['iyr']) not in range(2010, 2021):
            print('iyr invalid: %s' % d['iyr'])
        elif int(d['eyr']) not in range(2020, 2031):
            print('eyr invalid: %s' % d['eyr'])
        elif d['hgt'].endswith("cm") and int(filter(str.isdigit, d['hgt'])) not in range(150, 194):
            print('hgt invalid: %s' % d['hgt'])
        elif d['hgt'].endswith("in") and int(filter(str.isdigit, d['hgt'])) not in range(59, 77):
            print('hgt invalid: %s' % d['hgt'])
        elif not (d['hgt'].endswith("in") or d['hgt'].endswith("cm")):
            print('hgt invalid: %s' % d['hgt'])
        elif not (len(d['hcl']) == 7 and bool(re.search("^#([0-9a-f]{6})$", d['hcl']))):
            print('hcl invalid: %s' % d['hcl'])
        elif not any(color in d['ecl'] for color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
            print('ecl invalid: %s' % d['ecl'])
        elif not (len(d['pid']) == 9 and bool(re.search("^([0-9a-f]{9})$", d['pid']))):
            print('pid invalid: %s' % d['pid'])
        else:
            valid += 1
print valid
print present
