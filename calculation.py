def count_sevens_in_multiples_of_seven():
  count = 0
  for num in range(7, 7777778, 7):
      count += str(num).count('7')

  return count

total_sevens = count_sevens_in_multiples_of_seven()
print("数字「7」は{}回現れます".format(total_sevens))