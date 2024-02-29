with open("day_14.txt") as input_file:
    lines = [line.replace("\n", "") for line in input_file.readlines()]


def create_mask(mask_text):
    or_mask = 0
    and_mask = 2 ** 36 - 1
    for (i, a) in enumerate(reversed(mask_text)):
        if a == "1":
            or_mask += 2 ** i
        elif a == "0":
            and_mask -= 2 ** i
        else:
            assert a == "X"
    return or_mask, and_mask


def apply_mask(number_text, mask):
    number = int(number_text, 2)
    number |= mask[0]
    number &= mask[1]
    return number


def decode_address(address, mask_text):
    addresses = [address]
    for (i, a) in enumerate(reversed(mask_text)):
        if a == "1":
            addresses = [(x | (2 ** i)) for x in addresses]
        elif a == "0":
            continue
        else:
            addresses = [(x | (2 ** i)) for x in addresses] + [(x - (x & (2 ** i))) for x in addresses]
    return addresses


memory = {}

for line in lines:
    if line[:4] == "mask":
        mask = line[7:]
    else:
        address, value = line.split("=")
        address = int(address[4:-2])
        value = int(value[1:])
        for _address in decode_address(address, mask):
            memory[_address] = value

print(sum(memory.values()))
