#odd number bewteen 1 and 20
for i in range(1, 21, 2):
    print(i,end='')
print()
#a. count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i,end='')
print()
#b. count down from 20 to 1
for i in range(20, 0, -1):
    print(i,end='')
print()
#c. print n stars
Number = int(input ("Enter number of stars:"))
for i in range(Number):
    print('*', end='')
print()
#d. print n lines of increasing stars
#Using the same number as above print lines of increasing stars, starting at 1
for i in range(1, Number + 1):
    print('*' * i)
print()