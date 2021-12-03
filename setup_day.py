import os
import secrets

day = int(input("Enter day: "))
cookie = "***REMOVED***"
folder = f"day_{day}"

while os.path.isdir(folder):
    folder += f"_{secrets.token_hex(4)}"

os.mkdir(folder)
os.system(f"cp template.py {folder}/day_{day}.py")
os.system(
    f'curl --cookie "session={cookie}" https://adventofcode.com/2021/day/{day}/input > {folder}/input.txt'
)
