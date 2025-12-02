import requests
import os
from sys import argv
year,day = argv[-2:]
cookie = {
    # '_ga':'GA1.2.1763632613.1670886531',
    # '_gid':'GA1.2.1160750930.1674516883',
    # '_gat':'1',
    'session':'53616c7465645f5f7b6fd25f5edad251c334a5967a626b48bef22b3436dbbd755cd9c30b9ed088ce97e4dacb203991c9018fc2cc9db860b8cefe2e722996fb7f'}
for folder in ('inputs','scripts'):
    if not os.path.isdir(f'/{folder}/{year}'):
        try:
            os.makedirs(f'{folder}/{year}')
        except FileExistsError:
            pass
r = requests.get(f'https://adventofcode.com/{year}/day/{day}/input',cookies=cookie)
with open(f'inputs/{year}/{day}.txt','w') as f:
    f.write(r.content.decode())
if not os.path.isfile(f'scripts/{year}/{day}.py'):
    lines = [str(line).replace('year',f'{year}').replace('day',f'{day}') for line in open('template.txt').readlines()]
    with open(f'scripts/{year}/{day}.py','w') as f:
        f.write(''.join(lines))
