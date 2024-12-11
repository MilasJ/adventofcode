import sys
try:
    _,year,day = sys.argv
    exec(open(f'scripts/{year}/{day}.py').read())
except ValueError:
    print('Use exactly two values: make sure you use both year and day')
# except FileNotFoundError:
#     print(_path)
#     print('Make sure to enter:\n\t\'py run.py [year] [day]\'')
