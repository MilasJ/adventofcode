from timer import time_it
def main():
    lines = [[int(num) for num in line.strip().split()] for line in open('inputs/2024/2.txt').readlines()]
    @time_it
    def part1():
        safe = 0
        for line in lines:
            needcontinue=False
            if line not in [sorted(line),sorted(line)[::-1]]:
                continue
            prev = line[0]
            for num in line[1:]:
                if abs(num-prev) not in range(1,4):
                    needcontinue= True
                    break
                prev = num
            if needcontinue:
                continue
            safe += 1
        return safe

    @time_it
    def part2():
        pass
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
if __name__ == '__main__':
    main()
