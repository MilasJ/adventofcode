from timer import time_it
import hashlib
def main():
    lines = [line for line in open('inputs/2015/4.txt').readlines()]
    key = lines[0]
    @time_it
    def part1():
        return encrypt(key,5)
    @time_it
    def part2():
        return encrypt(key,6)
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
def encrypt(key, zeroes):
    num = 1
    while 1:
        keynum = key + str(num)
        hash = hashlib.md5(keynum.encode('utf-8')).hexdigest()
        if hash[:zeroes] == '0'*zeroes:
            return num, hash
        num +=1
if __name__ == '__main__':
    main()
