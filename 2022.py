import os
import sys
import time
from time import sleep
from year import logos
from year import colors
c = colors
l = logos

def clear():
    os.system("clear")

def mysleep():
    time.sleep(0.5)

def main():
    clear()
    print(c.c + l.text1)
    mysleep()
    clear()
    print(c.ly + l.text2)
    mysleep()
    clear()
    print(c.lr + l.text1)
    mysleep()
    clear()
    print(c.lg + l.text2)
    mysleep()
    clear()
    print(c.lc + l.text1)

    for i in c.c + l.year:
        for k in i:
            print(k , end="")
            sys.stdout.flush()
            sleep(0.1)

            break

    print(c.y + l.wish)
    mysleep()
    clear()
    print(c.c + l.hap)
    mysleep()
    clear()
    print(c.lr + l.yearptext)
    mysleep()
    clear()
    print(c.lg + l.yearptext)
    mysleep()
    clear()
    print(c.lc + l.yearptext)
    mysleep()
    clear()
    print(c.ly + l.yearptext)
    mysleep()
    clear()
    print(c.c + l.yearptext)
    mysleep()
    clear()
    print(c.r + l.yearptext)
    mysleep()
    clear()
    print(c.g + l.yearptext)
    mysleep()
    clear()
    print(c.lr + l.name)
    print(c.c + l.year)
    print(c.lg + l.wish)
    mysleep()
    clear()
    print(c.c + l.year)
    print(c.lg + l.wish)
    mysleep()
    clear()
    print(c.lr + l.year)
    print(c.g + l.wish)
    mysleep()
    clear()
    print(c.lc + l.year)
    print(c.ly + l.wish)
    print(c.lr + l.name)
    mysleep()
    clear()
    print(c.g+ l.name)

if __name__ == "__main__":
    main()