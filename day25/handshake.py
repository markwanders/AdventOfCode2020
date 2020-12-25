card_pub = 1
sub_num = 7
card_loop = 0
while card_pub != 7573546:
    card_pub *= sub_num
    card_pub %= 20201227
    card_loop += 1
print(card_loop)

door_pub = 1
door_loop = 0
while door_pub != 17786549:
    door_pub *= sub_num
    door_pub %= 20201227
    door_loop += 1
print(door_loop)

enc = 1
for _ in range(door_loop):
    enc *= card_pub
    enc %= 20201227
print(enc)