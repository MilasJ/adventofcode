from timer import time_it
def main():
    lines = [line.strip().replace(':',';').split('; ') for line in open('inputs/2023/2.txt').readlines()]
    @time_it
    def part1():
        total = 0
        # list(map(print,lines))
        for line in lines:
            red, green, blue = 0,0,0
            for i in line[1:]:
                continue_= False
                for shells in i.split(', '):
                    match shells.split()[1]:
                        case 'blue':
                            if int(shells.split()[0]) > blue:
                                blue = int(shells.split()[0])
                        case 'red':
                            if int(shells.split()[0]) > red:
                                red = int(shells.split()[0])
                        case 'green':
                            if int(shells.split()[0]) > green:
                                green = int(shells.split()[0])
                    # if continue_:
                    #     continue
            #     if continue_:
            #         continue
            # if continue_:
            #     continue
            print(red,green,blue)
            if red<=12 and green <= 13 and blue <= 14:
                total += int(line[0].split()[1])
                print(line[0].split()[1], total)
        return total
    @time_it
    def part2():
        total = 0
        # list(map(print,lines))
        for line in lines:
            red, green, blue = 0,0,0
            for i in line[1:]:
                continue_= False
                for shells in i.split(', '):
                    match shells.split()[1]:
                        case 'blue':
                            if int(shells.split()[0]) > blue:
                                blue = int(shells.split()[0])
                        case 'red':
                            if int(shells.split()[0]) > red:
                                red = int(shells.split()[0])
                        case 'green':
                            if int(shells.split()[0]) > green:
                                green = int(shells.split()[0])
                    # if continue_:
                    #     continue
            #     if continue_:
            #         continue
            # if continue_:
            #     continue
            print(red,green,blue)
            # if red<=12 and green <= 13 and blue <= 14:
            #     total += int(line[0].split()[1])
            #     print(line[0].split()[1], total)
            total += red*green*blue
        return total
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
if __name__ == '__main__':
    main()
