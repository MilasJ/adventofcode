from timer import time_it


def main():
    lines = [line.strip() for line in open("inputs/2025/3.txt").readlines()]

    @time_it
    def part1():
        joltage = 0
        for bank in lines:
            first_digit = str(max([int(battery) for battery in bank[:-1]]))
            second_digit = str(
                max([int(battery) for battery in bank[bank.find(first_digit) + 1 :]])
            )
            joltage += int(first_digit + second_digit)
        return joltage

    @time_it
    def part2():
        pass

    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
