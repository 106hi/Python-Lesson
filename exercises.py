li1 = list(range(1, 32))
li2 = list(range(1,13))
counter = 0
for elem1 in li1:
    for elem2 in li2:
        if elem1%10 == elem2%10:
            counter += 1
print(counter)