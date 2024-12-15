from timer import time_it
from itertools import zip_longest
def main():
    lines = [line.strip() for line in open('inputs/2024/4.txt').readlines()]
    @time_it
    def part1():
        finds = 0
        for line in lines:
            finds += line.count('XMAS') + line.count('SAMX')
        tlines = transpose(lines)
        for line in tlines:
            finds += line.count('XMAS') + line.count('SAMX')
        dlines = [''.join(dline) for dline in transpose(['.'*i + line for i,line in enumerate(lines)])]
        for line in dlines:
            finds += line.count('XMAS') + line.count('SAMX')
        dtlines = [''.join(dtline) for dtline in transpose(['.'*(len(lines)-i-1) + line for i, line in enumerate(tlines)])]
        for line in dtlines:
            finds += line.count('XMAS') + line.count('SAMX')
        return finds
    @time_it
    def part2():
        pass
    def transpose(A: list[str])->list[str]:
        return [''.join(line) for line in [['.' if char is None else char for char in string] for string in list(map(list,zip_longest(*A)))]]
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
if __name__ == '__main__':
    main()
