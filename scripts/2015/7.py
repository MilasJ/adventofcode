from timer import time_it
def main():
    lines = [line.strip().split(' -> ') for line in open('inputs/2015/7.txt').readlines()]
    # print(lines[0])
    # return
    wires = {}
    # for line in lines:
    #     w = []
    #     next_= False
    #     line=[line[0].split(),line[1]]
    #     if len(line[0])>2:
    #         for wire in line[0][::2]:
    #             if str(wire).isnumeric():
    #                 wire = int(wire)
    #             elif wire not in wires:
    #                 lines.append(line)
    #                 next_ = True
    #                 continue
    #             else:
    #                 w.append(wires[wire])
    #         if next_:
    #             continue
    #         w1, w2 = w
    #         match line[0][1]:
    #             case 'AND':
    #                 wires[line[1]] = w1 & w2
    #             case 'OR':
    #                 wires[line[1]] = w1 | w2
    #             case 'LSHIFT':
    #                 wires[line[1]] = (w1 << w2)%65536
    #             case 'RSHIFT':
    #                 wires[line[1]] = (w1 >> w2)
    #     elif len(line[0])==2 and line[0][1] == 'NOT':
    #         wires[line[1]] = ~line[1]
    #     elif str(line[0][0]).isnumeric():
    #         wires[line[1]] = int(line[0][0])
    #     # print(line)
    @time_it
    def part1():
        for line in lines:
            # print(line[0])
            w = []
            next_= False
            line_=[line[0].split(),line[1]]
            # print(line_[0])
            if len(line_[0])>2:
                # print(line_[0])
                for wire in line_[0][::2]:
                    # print(wire)
                    if str(wire).isnumeric():
                        w.append(int(wire))
                    elif wire not in wires:
                        lines.append(line)
                        next_ = True
                        continue
                    elif wire in wires:
                        # print(wire,wires[wire])
                        w.append(wires[wire])
                        # print(w)
                if next_:
                    continue
                # print(w)
                w1, w2 = w
                match line_[0][1]:
                    case 'AND':
                        wires[line[1]] = w1 & w2
                    case 'OR':
                        wires[line[1]] = w1 | w2
                    case 'LSHIFT':
                        wires[line[1]] = (w1 << w2)%65536
                    case 'RSHIFT':
                        wires[line[1]] = (w1 >> w2)
            elif len(line_[0])==2 and line_[0][0] == 'NOT':
                if line_[0][1] not in wires:
                    lines.append(line)
                    continue
                wires[line_[1]] = ~int(wires[line_[0][1]])%65536
            elif str(line[0][0]).isnumeric():
                # print(wires)
                wires[line_[1]] = int(line_[0][0])
            print(wires)
            # print(f'wires: {wires}')
        # return wires['a']
        return wires['a']
        # print(line)
    @time_it
    def part2():
        pass
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
if __name__ == '__main__':
    main()
