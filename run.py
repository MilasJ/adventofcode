from os import system
import sys
try:
    year,day = [int(num) for num in sys.argv[-2:]]
    exec(open(f'scripts/{year}/{day}.py').read())
except ValueError:
    print('Use exactly two values: make sure you use both year and day')
except FileNotFoundError:
    if int(day-1) in range(25):
        system(f'python newfile.py {year} {day}')
        exec(open(f'scripts/{year}/{day}.py').read())
    else:
        print('Make sure to enter:\n\t\'py run.py [year] [day]\'')