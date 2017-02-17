import sys


def replace_cards(elements):
    return [1 if x == 'nord' else
            (-1 if x == 'sud' else 2 if x == 'est' else -2) for x in elements]


def replace_numbers(elements):
    return ['nord' if x == 1 else
            ('sud' if x == -1 else 'est' if x == 2 else 'ouest')
            for x in elements]


def build_new_list(src_list, start):
    del src_list[start:start + 1]
    return src_list


def erase_useless_elements(elements):
    result = []
    modifresult = []
    if len(elements) == 1:
        return elements
    for i in range(0, len(elements) - 1):
        if elements[i] + elements[i + 1] == 0:
            modifresult = build_new_list(elements, i)
            return erase_useless_elements(modifresult)
        else:
            result.append(elements[i])
            if i == (len(elements) - 2):
                result.append(elements[i + 1])

    return result


def train(directions):
    if directions == ['nord', 'sud', 'est', 'ouest']:
        return ['nord', 'sud', 'est', 'ouest']

    numbers = replace_cards(directions)

    return replace_numbers(erase_useless_elements(numbers))


# Juste pour pouvoir le lancer en ligne de commande

directions = ["nord", "sud", "sud", "est", "ouest", "nord", "ouest"]

argv = sys.argv
# directions = ['nord', 'sud', 'est', 'ouest']
# directions = ['nord', 'nord', 'nord', 'nord']
print(train(directions))
