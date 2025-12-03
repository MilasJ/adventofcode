from timer import time_it
def main():
    lines = [line.strip() for line in open('inputs/2025/2.txt').readlines()]
    ranges = [[int(num) for num in range.split("-")] for range in lines[0].split(",")]
    @time_it
    def part1():
        idsum = 0
        for start, end in ranges:
            for num in range(start, end+1):
                numstring = str(num)
                digits = len(numstring)
                half = int(digits/2)
                if numstring[:half] == numstring[half:]:
                    idsum += int(numstring)
        return idsum
                

    @time_it
    def part2():
        pass
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
if __name__ == '__main__':
    main()
