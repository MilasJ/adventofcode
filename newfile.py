import requests
import os
from sys import argv
year,day = argv[-2:]
cookie = {
    # '_ga':'GA1.2.1763632613.1670886531',
    # '_gid':'GA1.2.1160750930.1674516883',
    # '_gat':'1',
    'session':'53616c7465645f5f3629edbaeb85a2b8c366f7c09adb785325acf4473fb53689f90437954735668c6ae0aa7af0ecf6d38da5c9db1222a6b1e66f6fd6d0b75825'}
for folder in ('inputs','scripts'):
    if not os.path.isdir(f'/{folder}/{year}'):
        os.makedirs(f'{folder}/{year}')
r = requests.get(f'https://adventofcode.com/{year}/day/{day}/input',cookies=cookie)
with open(f'inputs/{year}/{day}.txt','w') as f:
    f.write(r.content.decode())
lines = [str(line).replace('year',f'{year}').replace('day',f'{day}') for line in open('template.txt').readlines()]
with open(f'scripts/{year}/{day}.py','w') as f:
    f.write(''.join(lines))
