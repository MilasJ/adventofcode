from timer import time_it
from os.path import abspath,join
from importlib import util
mainpath = __file__.split('\\')[-1]
match mainpath:
    case 'run.py':
        path = '..\\inputs\\2019\\1.txt'
    case '1.py':
        path = '..\\..\\..\\inputs\\2019\\1.txt'
inputfile = abspath(join(__file__,path))
print(__file__.split('\\')[-1])
def main():
    lines = [line for line in open(inputfile).read().split('\n')]
    for i,line in enumerate(lines):
        lines[i] = int(line)
    @time_it
    def part1():
        count = 0
        for line in lines:
            count += findfuel(line)
        return count
    @time_it
    def part2():
        count = 0
        for line in lines:
            temp = findfuel(line)
            if temp > 0:
                lines.append(temp)
                count += temp
        return count
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
def findfuel(item):
    return item//3-2
if __name__ == '__main__':
    main()