import re
from functools import reduce
from collections import OrderedDict


class NewsDict(OrderedDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.move_to_end(key)


def parse_line(line, d):
    match = re.search(r'\d+', line)
    if match:
        index = int(match.group())
        text = line[match.end():].strip()
        d[index] = text
    return d


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
    d = NewsDict()
    for line in lines:
        d = parse_line(line, d)
    print(d)
    #data = list(filter(lambda x: x is not None, map(parse_line, lines)))

    #reduce(print_text, data, None)

    #file.close()


if __name__ == '__main__':
    make_news_compilation()
