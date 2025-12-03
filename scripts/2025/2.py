from timer import time_it
import textwrap
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
                    idsum += num
        return idsum
                

    @time_it
    def part2(): #  Thirty seconds to run. Oy...
        idsum = 0
        for start, end in ranges:
            for num in range(start, end+1):
                numstring = str(num)
                digits = len(numstring)
                for factor in range(1, digits):
                    if digits % factor:
                        continue
                    groups = textwrap.wrap(numstring, factor)
                    if all(group == groups[0] for group in groups):
                        idsum += num
                        break
        return idsum
                    


    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
if __name__ == '__main__':
    main()
