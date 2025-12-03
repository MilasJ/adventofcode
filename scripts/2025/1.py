from timer import time_it
def main():
    lines = [line.strip() for line in open('inputs/2025/1.txt').readlines()]
    @time_it
    def part1():
        dial = 50
        counter = 0
        for line in lines:
            if line[0] == "R":
                dial += int(line[1:])
            elif line[0] == "L":
                dial -= int(line[1:])
            dial = dial%100
            if dial == 0:
                counter += 1
        return counter
    @time_it
    def part2():
        dial = 50
        counter = 0
        directions = {"L":-1, "R":1}
        for line in lines:
            direction = directions[line[0]]
            for _ in range(int(line[1:])):
                dial += direction
                dial = dial%100
                if dial == 0:
                    counter += 1
        return counter
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
if __name__ == '__main__':
    main()
