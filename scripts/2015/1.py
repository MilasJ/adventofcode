from timer import time_it
def main():
    lines = [line for line in open('inputs/2015/1.txt').readlines()]
    # print(lines)
    @time_it
    def part1():
        floor = 0
        for i in lines[0]:
            match i:
                case '(':
                    floor += 1
                case ')':
                    floor -= 1
        return floor
    @time_it
    def part2():
        floor = 0
        i = 0
        while floor >= 0:
            match lines[0][i]:
                case '(':
                    floor += 1
                case ')':
                    floor -= 1
            i += 1
        return i
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
if __name__ == '__main__':
    main()
