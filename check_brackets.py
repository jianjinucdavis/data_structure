# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opens = []
    for idx, item in enumerate(text):
        b = Bracket(item, idx)
        if item in "([{":
            opens.append(b)
        if item in ")]}":
            if len(opens) > 0:
                x = opens.pop()
                if not are_matching(x.char, b.char):
                    return idx + 1
            else:
                return idx + 1  # unmatch closed bracket
    if len(opens) == 0:
        return "Success"
    return opens[0].position + 1  # unmatch open bracket


def main():
    # text = input()
    text = "[{{}]" # s.append([), s.pop(), x.append("("), x.append("("),
    mismatch = find_mismatch(text)
    print(mismatch)
    return mismatch


if __name__ == "__main__":
    main()


'''
    if len(opening_brackets_stack) > 0:
        return list(text).index(opening_brackets_stack[0]) + 1
'''