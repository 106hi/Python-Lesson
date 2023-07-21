d = {'apple': 10, 'grape': 20, 'orange': 30}
d['apple'] = d.get('apple', -1)
d['pinapple'] = d.get('pinapple', -1)
print(d)