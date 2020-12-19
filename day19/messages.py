with open("input.txt") as f:
    parts = f.read().split("\n\n")
    rules = {r.split(": ")[0]: r.replace("\"","").split(": ")[1].split(" | ") for r in parts[0].split("\n")}
    messages = parts[1].split("\n")


def validate(text, rule):
    if "a" in rule or "b" in rule:
        return rule[0], True
    prefix = ""
    for branch in rule:
        print("branch %s out of rule %s" % (branch, rule))
        rules_to_follow = branch.split(" ")
        for rule_to_follow in rules_to_follow:
            print("rule %s : %s" % (rule_to_follow, rules[rule_to_follow]))
            new_prefix, valid = validate(text, rules[rule_to_follow])
            prefix += new_prefix
            print("prefix %s" % prefix)
        if not text.startswith(prefix):
            print("%s does not start with %s, going to next branch" % (text, prefix))
            prefix = prefix[:-len(branch.split(" "))]
        else:
            print("%s does start with %s" % (text, prefix))
            return prefix, True
    return prefix, False


for message in messages:
    print("checking %s" % message)
    print(message, validate(message, rules['0'])[1])
