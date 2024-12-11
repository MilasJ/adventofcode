from timer import time_it
def main():
    lines = [line.strip().split()[-4:] for line in open('inputs/2015/6.txt').readlines()]
    for i, line in enumerate(lines):
        
        line[1] = list(map(int,line[1].split(',')))
        line[3] = list(map(int,line[3].split(',')))
        # for j, coord in enumerate(line[1::2]):
        #     line[2*j+1] = list(map(int,coord.split(',')))
        lines[i] = line
    # print(lines[0])
    @time_it
    def part1():
        map = [[False]*1000 for _ in range(1000)]
        for line in lines:
            # print(line)
            coords = line[1::2]
            # print(coords)
            x1, y1 = coords[0]
            x2, y2 = coords[1]
            if x1>x2:
                x1, x2 = x2, x1
            if y1>y2:
                y1,y2 = y2, y1
            # print(x1,x2)
            for x in range(x1,x2+1):
                for y in range(y1,y2+1):
                    match line[0]:
                        case 'on':
                            map[x][y] = True
                        case 'off':
                            map[x][y] = False
                        case 'toggle':
                            map[x][y] = not map[x][y]
            # for i in map:
            #     str = ''
            #     for j in i:
            #         if j:
            #             str += '#'
            #         else:
            #             str += '*'
            #     print(str)
            # print ('*'*1000)
        # for i in map:
        #     str = ''
        #     for j in i:
        #         if j:
        #             str += '#'
        #         else:
        #             str += ' '
        #     print(str)
        # print(len([j for i in map for j in i if j]))
        return sum(sum(i) for i in map)
    @time_it
    def part2():
        map = [[0]*1000 for _ in range(1000)]
        for line in lines:
            x1,y1 = line[1]
            x2,y2 = line[3]
            for x in range(x1,x2+1):
                for y in range(y1,y2+1):
                    match line[0]:
                        case 'on':
                            map[x][y] += 1
                        case 'off':
                            map[x][y] -= 1 if map[x][y] else 0
                        case 'toggle':
                            map[x][y] += 2
        return(sum(sum(i) for i in map))
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
if __name__ == '__main__':
    main()
