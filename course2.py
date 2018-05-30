import sys

friend = sys.stdin.readline()
friend = friend[0:-1]


if friend == "gordo" or friend == "sam":
    print "Jerk"
elif friend == "kyle":
    print "Something else"
else:
    print "Bad touch, Bad touch!!"
