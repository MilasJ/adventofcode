from timer import time_it
def main():
    lines = [line.strip().split(', ') for line in open('inputs/2016/1.txt').readlines()]
    @time_it
    def part1():
        line = lines[0]
        pos = 0
        face = 1j
        for step in line:
            direction = step[0]
            length = int(step[1:])
            match direction:
                case 'L':
                    face *= 1j
                case 'R':
                    face *= -1j
            pos += length * face
        return abs(pos.real) + abs(pos.imag)
    @time_it
    def part2():
        line = lines[0]
        pos = 0
        face = 1j
        locs = []
        done = False
        for step in line:
            direction = step[0]
            length = int(step[1:])
            match direction:
                case 'L':
                    face *= 1j
                case 'R':
                    face *= -1j
            for _ in range(length):
                pos += face
                if pos in locs:
                    done = True
                    break
                locs.append(pos)
            if done:
                break
        return abs(pos.real) + abs(pos.imag)
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
if __name__ == '__main__':
    main()