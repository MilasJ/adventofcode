from timer import time_it
from os.path import abspath,join
# from collections import defaultdict
mainpath = __file__.split('\\')[-1]
match mainpath:
    case 'run.py':
        path = '..\\inputs\\2019\\3.txt'
    case '3.py':
        path = '..\\..\\..\\inputs\\2019\\3.txt'
inputfile = abspath(join(__file__,path))
dirdict = {
    'R':1,
    'D':-1j,
    'U':1j,
    'L':-1
} #complex numbers rule!
def main():
    lines = [line.split(',') for line in open(inputfile).read().split('\n')]
    grid = {}
    @time_it
    def part1():
        backup = {a:b for a,b in tracewires(lines[0],grid).items()}
        backup = tracewires(lines[1],backup)
        print(backup == grid)
        x = [manhattandist(coord) for coord in backup if backup[coord] == 'X']
        print(x)
        return min(x)
    @time_it
    def part2():
        pass
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
def manhattandist(coord:complex)->int:
    coords = coord.real,coord.imag
    return int(sum(list(map(abs,coords))))
def tracewires(wire,grid)->dict:
    pos = 0
    for direction in wire:
        direct = dirdict[direction[0]]
        dist = int(direction[1:])
        for _ in range(dist):
            pos += direct
            if pos in grid:
                grid[pos] = 'X'
            else:
                grid[pos] = '#'
    # print(grid)
    return {pos:state for pos,state in grid.items()}
if __name__ == '__main__':
    main()