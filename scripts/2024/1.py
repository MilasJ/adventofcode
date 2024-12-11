from timer import time_it
def main():
    lines = [line.strip().split('   ') for line in open('inputs/2024/1.txt').readlines()]
    list1, list2 = list(map(list, zip(*lines)))
    list1 = list(map(int,list1))
    list2 = list(map(int,list2))
    @time_it
    def part1():
        diff = 0
        list1.sort()
        list2.sort()
        for i in range(len(list1)):
            diff += abs(list1[i]-list2[i])
        return diff
    @time_it
    def part2():
        simscore = 0
        for i in list1:
            samenum = 0
            for j in list2:
                if i == j:
                    samenum += 1
            simscore += samenum * i
        return simscore
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
if __name__ == '__main__':
    main()
