import os
import platform
import time

from year import logos
from year import colors
from year import sprint
sp = sprint
c = colors
l = logos

def clear():
    s = platform.platform()
    if "Windows" in s:
        os.system("cls")
    else:
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
    clear()
    print(c.c + l.b)
    mysleep()
    clear()
    print(c.g + l.c)
    mysleep()
    clear()
    print(c.lg+ l.wish)
    mysleep()
    clear()
    
    sp.sprint(l.year)

    clear()
    print(c.c + l.hap)
    print(c.lr + l.name)
    mysleep()
    clear()
    print(c.y + l.wish)
    print(c.lr + l.name)
    mysleep()
    clear()
    print(c.c + l.hap)
    print(c.lr + l.name)
    mysleep()
    clear()
    print(c.lr + l.yearptext)
    mysleep()
    clear()
    print(c.lg + l.yearptext)
    print(c.lr + l.name)
    mysleep()
    clear()
    print(c.lc + l.yearptext)
    print(c.lc + l.name)
    mysleep()
    clear()
    print(c.ly + l.yearptext)
    print(c.c + l.name)
    mysleep()
    clear()
    print(c.c + l.yearptext)
    print(c.y + l.name)
    mysleep()
    clear()
    print(c.r + l.yearptext)
    print(c.r + l.name)
    mysleep()
    clear()
    print(c.g + l.yearptext)
    print(c.ly + l.name)
    mysleep()
    clear()
    print(c.c + l.year)
    print(c.lg + l.wish)
    print(c.r + l.name)
    mysleep()
    clear()
    print(c.c + l.year)
    print(c.lg + l.wish)
    print(c.lr + l.name)
    mysleep()
    clear()
    print(c.lr + l.year)
    print(c.g + l.wish)
    print(c.ly + l.name)
    mysleep()
    clear()
    print(c.lc + l.year)
    print(c.ly + l.wish)
    print(c.lg + l.name)
    
    mysleep()
    clear()
    print(c.g+ l.name)
    print(c.y + l.wish)
    print(c.lr + l.name)
    mysleep()
    clear()
    print(c.c + l.year +"\n" + l.c)
    mysleep()
    clear()
    print(c.r + l.year+"\n" + l.c)
    mysleep()
    clear()
    print(c.g + l.year+"\n" + l.c)
    print(c.lr + l.name)

    mysleep()
    clear()

    print(c.lr + l.yearptext)
    print(c.lr + l.name)

    mysleep()
    clear()
    print(c.lg + l.yearptext)
    print(c.lg + l.name)

    mysleep()
    clear()
    print(c.lc + l.yearptext)
    print(c.lc + l.name)

    mysleep()
    clear()
    print(c.ly + l.yearptext)
    print(c.ly + l.name)

    mysleep()
    clear()
    print(c.c + l.yearptext)
    print(c.c + l.name)

    mysleep()
    clear()
    print(c.r + l.yearptext)
    print(c.r + l.name)

    mysleep()
    clear()
    print(c.g + l.yearptext)
    print(c.g + l.name)

    mysleep()

if __name__ == "__main__":
    main()