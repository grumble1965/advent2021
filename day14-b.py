import sys


rules = {}


def f(in_str):
    prefix = ''
    while len(in_str) > 0:
        if len(in_str) == 1:
            prefix += in_str
            in_str = ''
        elif len(in_str) == 2:
            (x, y) = (in_str[0], in_str[1])
            tmp = rules[x + y]
            prefix += x + tmp + y
            in_str = ''
        else:
            (x, y, zs) = (in_str[0], in_str[1], in_str[2:])
            tmp = rules[x + y]
            prefix += x + tmp
            in_str = y + zs
    return prefix


def f_better(in_str, prefix):
    if not in_str:
        return prefix
    elif len(in_str) == 1:
        return prefix + in_str
    elif len(in_str) == 2:
        (x, y) = (in_str[0], in_str[1])
        tmp = rules[x+y]
        return prefix + x + tmp + y
    else:
        (x, y, zs) = (in_str[0], in_str[1], in_str[2:])
        tmp = rules[x+y]
        front = x + tmp
        rest = y + zs
        # rest = f_better(rest)
        return f_better(rest, prefix + front)


def count_str(string):
    """
    Build a dict of letter frequency for a string.
    :param string:
    :return: New dictionary.
    """
    tt = {}
    for ch in string:
        tt[ch] = string.count(ch)
    return tt


def add_counts(dict1, dict2):
    """
    Combine two letter frequency dictionaries into one dictionary.
    :param dict1:
    :param dict2:
    :return: New dictionary.
    """
    tt = {}
    for ch, v in dict1.items():
        tt[ch] = v
    for ch, v in dict2.items():
        if ch in tt:
            tt[ch] += v
        else:
            tt[ch] = v
    return tt


def sub_counts(dict1, dict2):
    tt = {}
    for ch, v in dict1.items():
        tt[ch] = v
    for ch, v in dict2.items():
        if ch in tt:
            tt[ch] -= v
        else:
            tt[ch] = v
    return tt


def process_step(polymer_list):
    product_list = [polymer_list[0]]
    for idx in range(len(polymer_list) - 1):
        pair = polymer_list[idx] + polymer_list[idx + 1]
        new_molecule = rules[pair]
        product_list.append(new_molecule)
        product_list.append(polymer_list[idx + 1])
    return product_list


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    template = None
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

    # build quantity table
    # quants = []
    # row = 0
    # quants.append({})
    # for given in rules:
    #     given_str = given[0] + given[1]
    #     quants[row][given] = count_str(given_str)
    # print(quants[0])
    #
    # for row in range(1, 11):
    #     quants.append({})
    #     for given, get in rules.items():
    #         string1 = given[0] + get
    #         string2 = get + given[1]
    #         inter_sum = add_counts(quants[row - 1][string1], quants[row - 1][string2])
    #         inter_sum[get] -= 1
    #         quants[row][given] = inter_sum
    #     print(quants[row])

    # print("How do these combine?")
    # d1 = quants[2]['CB']
    # d2 = quants[0]['NB']
    # d3 = quants[0]['NC']
    # t1 = add_counts(d1, d2)
    # final = add_counts(t1, d3)
    # print(f"does q(foo(NNCB, 2)) = {final}")


    # for step in range(10):
    #     result = rec_step(polymer, rules)
    #     # result = process_step(polymer, rules)
    #     # print(f"After step {step}: {result}")
    #     polymer = result
    #     print(f"step {step+1}  length {len(result)}")

    # table = {}
    # for ch in result:
    #     if ch not in table:
    #         table[ch] = 1
    #     else:
    #         table[ch] += 1
    #
    # quantities = table.values()
    # print(f"difference = {max(quantities) - min(quantities)}")

    # verify f
    # f_template = f(template)
    # print(f"  f({template}) -> {f_template}")
    # f_f_template = f(f_template)
    # print(f"f^2({template}) -> {f_f_template}")

    polymer = template
    for step in range(20):
        result = f(polymer)
        polymer = result
        print(f"step {step+1}  length {len(result)}")


if __name__ == '__main__':
    main()
