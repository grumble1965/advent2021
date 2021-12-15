import sys


def process_step(polymer_list, rules):
    product_list = [polymer_list[0]]
    for idx in range(len(polymer_list) - 1):
        pair = polymer_list[idx] + polymer_list[idx + 1]
        new_molecule = rules[pair]
        product_list.append(new_molecule)
        product_list.append(polymer_list[idx + 1])
    product = "".join(product_list)
    return product


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    template = None
    rules = {}
    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            # print(f"{tmp}")

            words = tmp.split(' -> ')
            if len(words) == 1 and template is None:
                template = words[0]
            elif len(words) == 2:
                given, get = words[0], words[1]
                rules[given] = get

    # print(f"template = {template}")
    # for (gvn, get) in rules:
    #     print(f" {gvn} -> {get}")

    # print(f"Template:     {template}")
    polymer_list = list(template)
    result = ''
    for step in range(10):
        result = process_step(polymer_list, rules)
        # print(f"After step {step}: {result}")
        polymer_list = list(result)

    table = {}
    for ch in result:
        if ch not in table:
            table[ch] = 1
        else:
            table[ch] += 1

    quantities = table.values()
    print(f"difference = {max(quantities) - min(quantities)}")


if __name__ == '__main__':
    main()
