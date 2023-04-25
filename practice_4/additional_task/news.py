import re
from functools import reduce
from collections import OrderedDict


#class NewsDict(OrderedDict):


def parse_line(line):
    match = re.search(r'\d+', line)
    if match:
        index = int(match.group())
        text = line[match.end():].strip()
        return index, text
    else:
        return None


def print_text(accumulator, current):
    if accumulator is None:
        print(current[1])
        return current[0]
    elif current[0] > accumulator:
        print(current[1])
        return current[0]
    else:
        return accumulator


def make_news_compilation():
    with open('news.txt', 'r') as file:
        lines = file.readline()

    data = list(filter(lambda x: x is not None, map(parse_line, lines)))

    reduce(print_text, data, None)

    file.close()


if __name__ == '__main__':
    make_news_compilation()
