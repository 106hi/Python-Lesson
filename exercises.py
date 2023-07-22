a = 0
b = 5
try:
    print(a / b)
except ZeroDivisionError:
    print('zero division')

try:
    print(b / a)
except ZeroDivisionError:
    print('zero division')