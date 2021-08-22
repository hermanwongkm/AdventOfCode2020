
def readFile():
    with open("input.txt", "r") as f:
        return [int(line) for line in f.readlines()]  # List comprehension


def process2Sum(entries: list):
    seen = set()
    for entry in entries:
        if(2020 - entry in seen):
            return entry * (2020-entry)
        else:
            seen.add(entry)


def process3Sum(entries: list):
    entries.sort()

    for i in range(len(entries)):
        left = i + 1
        right = len(entries) - 1

        while(left < right):
            sum = entries[i] + entries[left] + entries[right]
            if(sum == 2020):
                return entries[i] * entries[left] * entries[right]
            elif sum > 2020:
                right = right - 1
            else:
                left = left + 1


if __name__ == '__main__':
    entries = readFile()
    # print(f'Part1: Product of the 2 entries is {process2Sum(entries)}')
    print(f'Part1: Product of the 3 entries is {process3Sum(entries)}')
