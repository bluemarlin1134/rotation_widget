import os
with open('state') as c:
    current = int(c.readlines()[0])

states = ['normal', 'left', 'right', 'inverted']

if(current == 3):
    current = 0
else:
    current = current + 1

os.system(f"xrandr -o {states[current]}")

with open('state', 'w') as f:
    f.write(str(current))
