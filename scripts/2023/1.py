from functools import reduce
from timer import time_it
from re import sub,search
def main():
    lines = [line.strip() for line in open('inputs/2023/1.txt').readlines()]
    @time_it
    def part1():
        test = list(map(lambda x: [i for i in x if i.isdigit()],lines))
        # print(test)
        total = sum(int(i) for i in list(map(lambda y:y[0]+y[-1],test)))
        return total
        pass
    @time_it
    def part2():
        nums = ['zero','one','two','three','four','five','six','seven','eight','nine']
        # test = [reduce(lambda a,kv: a.replace(*kv),nums, line) for line in lines]
        test = [line for line in lines]
        # for i, line in enumerate(test):
        #     # for num, digit in nums:
        #     string = r'zero|one|two|three|four|five|six|seven|eight|nine'
        #     test[i] = sub(string,lambda x: str(nums.index(x.group())),line)
        test = [sub(r'(?=(zero|one|two|three|four|five|six|seven|eight|nine))',lambda x: str(nums.index(x.group(1))),line) for line in test]
        print(test)
        # test = list(map(lambda x: [i for i in x if i.isdigit()],test))
        test = [[i for i in line if i.isdigit()] for line in test]
        # print(test)
        print(list(map(lambda y: y[0]+ y [-1],test)))
        total = sum(int(i) for i in list(map(lambda y: y[0]+y[-1],test)))
        return total
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
if __name__ == '__main__':
    main()
