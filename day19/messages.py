with open("input.txt") as f:
    parts = f.read().split("\n\n")
    rules = {r.split(": ")[0]: r.replace("\"", "").split(": ")[1].split(" | ") for r in parts[0].splitlines()}
    messages = parts[1].splitlines()
    for k, v in rules.items():
        rules[k] = [i.split(" ") for i in v]


def validate(text, rule):
    if not text or not rule:
        return not text and not rule

    r = rule.pop(0)
    if 'a' in r or 'b' in r:
        if text.startswith(r):
            return validate(text[1:], rule[:])
    else:
        for rule_to_follow in rules[r]:
            if validate(text, rule_to_follow + rule):
                return True
    return False


print(sum(1 for message in messages if validate(message, rules['0'][0][:])))
rules['8'] = [['42'], ['42', '8']]
rules['11'] = [['42', '31'], ['42', '11', '31']]
print(sum(1 for message in messages if validate(message, rules['0'][0][:])))
