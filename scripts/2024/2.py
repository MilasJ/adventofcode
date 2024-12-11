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
        #whatever I have done to deserve this, I am sorry
        safe = 0
        for line in lines:
            goodSoFar = True
            if line not in [sorted(line), sorted(line)[::-1]]:
                goodSoFar = False
            prev = line[0]
            for num in line[1:]:
                if abs(num-prev) not in range(1,4):
                    goodSoFar = False
                    break
            if goodSoFar:
                safe += 1
                continue
            for problem in range(len(line)):
                ostrich = True
                line_ = line[:problem] + line[problem+1:] #so glad I remembered to do that
                print(line, line_)
                if line_ not in [sorted(line_), sorted(line_)[::-1]]:
                    continue
                prev_ = line_[0]
                for num_ in line_[1:]:
                    if abs(num_-prev_) not in range(1,4):
                        ostrich = False
                        break
                    prev_ = num_
                if ostrich:
                    safe += 1
                    break
        return safe
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
if __name__ == '__main__':
    main()
