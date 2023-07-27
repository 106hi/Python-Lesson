line_size = int(input())
for i in range(line_size):
    year = int(input())
    #閏年判定
    if (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0:
        print("{} is a leap year".format(year))
    else:
        print("{} is not a leap year".format(year))