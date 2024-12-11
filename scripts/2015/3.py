from timer import time_it
def main():
    lines = [line for line in open('inputs/2015/3.txt').readlines()]
    line = lines[0]
    @time_it
    def part1():
        return len(travel(line,[0]))
    @time_it
    def part2():
        places = travel(line[::2],[0])
        places = travel(line[1::2],places)
        return len(places)
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
def travel(directions, allpos):
    pos = 0
    for dir in directions:
        match dir:
            case '^':
                pos += 1j
            case 'v':
                pos -= 1j
            case '>':
                pos += 1
            case '<':
                pos -= 1
        if pos not in allpos:
            allpos.append(pos)
    return allpos
if __name__ == '__main__':
    # print(travel('>'))
    # print(travel('^>v<'))
    arr = '^v'
    # print(len(travel(arr[1::2],travel(arr[::2]))))
    main()
