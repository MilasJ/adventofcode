from timer import time_it
from os.path import abspath,join
from intcode import intcode
mainpath = __file__.split('\\')[-1]
match mainpath:
    case 'run.py':
        path = '..\\inputs\\2019\\2.txt'
    case '2.py':
        path = '..\\..\\..\\inputs\\2019\\2.txt'
inputfile = abspath(join(__file__,path))
def main():
    line = eval(f'[{open(inputfile).read()}]')
    @time_it
    def part1():
        backup = [i for i in line]
        backup[1] = 12
        backup[2] = 2
        program = intcode(backup)
        program.run()
        return program.program[0]
    @time_it
    def part2():
        for i in range(100):
            for j in range(100):
                backup = [i for i in line]       
                backup[1] = i
                backup[2] = j
                # print(i,j)
                # print(backup[:4])
                program = intcode(backup)
                program.run()
                output = program.program[0]
                if output == 19690720:
                    # print(program.program)
                    return 100*i+j
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
if __name__ == '__main__':
    main()