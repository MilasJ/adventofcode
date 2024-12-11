from timer import time_it
import re
def main():
    lines = [line.strip() for line in open('inputs/2015/5.txt').readlines()]
    @time_it
    def part1():
        counter = 0
        # naught.y = 0
        # print(bool(re.search(r'^(?=.*(.)\1)(?=([aeiou].*){3})((?!ab|cd|pq|xy).)*$','uavfnvyrjeiwqmuu')))
        for line in lines:
            if re.search(r'^(?=.*(.)\1)(?=.*[aeiou].*[aeiou].*[aeiou])((?!ab|cd|pq|xy).)*$',line):
                counter += 1
            else:
                print(line)
        #         naughty += 1
        # if counter + naughty != len(lines):
        #     print('warning')
        return counter
    @time_it
    def part2():
        return len([line for line in lines if re.search(r'^(?=.*(..).*\1)(?=.*(.).\2)',line)])
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
if __name__ == '__main__':
    main()
