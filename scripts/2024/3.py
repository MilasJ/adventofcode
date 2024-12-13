from timer import time_it
import re
def main():
    lines = [line.strip() for line in open('inputs/2024/3.txt').readlines()]
    @time_it
    def part1():
        total = 0
        print(mul(0,0))
        for line in lines:
            for match in re.findall(r'mul\(\d{1,3},\d{1,3}\)',line):
                total += eval(match)
        return total
    @time_it
    def part2():
        count = True
        total = 0
        for line in lines:
            for match in re.findall(r'mul\(\d{1,3},\d{1,3}\)|do(?:n\'t)?\(\)',line):
                match match[:4]:
                    case 'do()':
                        count = True
                    case 'don\'':
                        count = False
                    case 'mul(':
                        total += eval(match)*count
        return total
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
def mul(X,Y):
    return int(X*Y)
if __name__ == '__main__':
    main()
