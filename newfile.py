import requests
import os
from sys import argv
year,day = argv[-2:]
cookie = {
    # '_ga':'GA1.2.1763632613.1670886531',
    # '_gid':'GA1.2.1160750930.1674516883',
    # '_gat':'1',
    'session':'53616c7465645f5fb7e085420a02b867a3c559d41a8652429a91df9413da0072b3a1a81520df46ac7470e40057249250ef0cfdf5b298fe3533ae7b1991c4e994'}
for folder in ('inputs','scripts'):
    if not os.path.isdir(f'/{folder}/{year}'):
        os.makedirs(f'{folder}/{year}')
r = requests.get(f'https://adventofcode.com/{year}/day/{day}/input',cookies=cookie)
with open(f'inputs/{year}/{day}.txt','w') as f:
    f.write(r.content.decode())
lines = [str(line).replace('year',f'{year}').replace('day',f'{day}') for line in open('template.txt').readlines()]
with open(f'scripts/{year}/{day}.py','w') as f:
    f.write(''.join(lines))
