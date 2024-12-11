from timer import time_it
def main():
    lines = [line for line in open('inputs/2015/2.txt').readlines()]
    @time_it
    def part1():
        paper = 0
        for line in lines:
            l, w, h = map(int,line.split('x'))
            a,b,c = l*w, w*h, l*h
            paper += 2*a +2*b + 2*c + min(a,b,c)
        return paper
    @time_it
    def part2():
        ribbon = 0
        for line in lines:
            l,w,h = map(int,line.split('x'))
            a,b,c = 2*l+2*w, 2*w+2*h,2*l+2*h
            ribbon += min(a,b,c) + l*w*h
        return ribbon
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
if __name__ == '__main__':
    main()
