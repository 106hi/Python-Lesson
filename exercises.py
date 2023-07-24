list1 = [12,23,34,45,56,67,78,89]
list2 = [21,32,43,45,65,67,78,98]
A = set(list1)
B = set(list2)
inter_set = A.intersection(B)
union_set = A.union(B)
print(len(inter_set) / len(union_set))