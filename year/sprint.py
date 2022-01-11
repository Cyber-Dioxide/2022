import sys,time
from year import colors
c = colors
def sprint(str):
	for i in str +c.c + "\n":
		sys.stdout.write(i)
		sys.stdout.flush()

		time.sleep(0.0001)


#
# for line in c.c + l.year:
# 	for i in line:
# 		print(i, end='')
# 		sys.stdout.flush()
# 		sleep(0.01)
# 		break