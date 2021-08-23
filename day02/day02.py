import re


def readFile():
    with open("input.txt", "r") as f:
        return [line for line in f.readlines()]  # List comprehension


def process(entries: list):
    finalCount = 0
    for entry in entries:
        min, max, value, _, password = re.split('[- :]', entry)
        count = password.count(value)
        if count >= int(min) and count <= int(max):
            finalCount += 1
    return finalCount


def process2(entries: list):
    finalCount = 0
    for entry in entries:
        first, last, value, _, password = re.split('[- :]', entry)
        if (password[int(first)-1] == value) ^ (password[int(last)-1] == value):
            finalCount += 1
    return finalCount


if __name__ == '__main__':
    entries = readFile()
    print(process(entries))
    print(process2(entries))
