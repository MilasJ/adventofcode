from timer import time_it


def main():
    lines = [line.strip() for line in open("inputs/2025/3.txt").readlines()]

    @time_it
    def part1():
        joltage = 0
        for bank in lines:
            first_digit = str(max(bank[:-1]))
            second_digit = str(max(bank[bank.find(first_digit) + 1 :]))
            joltage += int(first_digit + second_digit)
        return joltage

    @time_it
    def part2():
        joltage = 0
        for bank in lines:
            digits = ""
            pos = 0
            for i in range(1, 12):
                digits += str(max(bank[: i - 12]))
                pos = bank.find(digits[-1]) + 1
                bank = bank[pos:]
            digits += str(max(bank[:]))
            joltage += int(digits)
        return joltage

    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
