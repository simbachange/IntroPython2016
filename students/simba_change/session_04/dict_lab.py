city = {'name': 'Chris', 'city': 'Seattle', 'Cake': 'Chocolate'}
print (city)

city.pop('Cake')

print (city)

city.update{('fruit':'mango')}

print (city)

for k , v in city.items():
    print('Key:  ' + k + 'Value:'  + v)

'Cake' in city.keys()

'Mango' in city.values()

new_city = {'name':'0','fruit': '0', 'city': '2'}

s2 = {"0","2","4","6","8","10","12","14","16","18","20"}

s3 = {"0","3","6","9","12","15","18"}

s4 = {"0","4","8","12","16","20"}

s3.issubset(s2)

s4.issubset(s2)

p = {"P","y","t","h","o","n"}

p.update("i")

mr = frozenset(("marathon"))

p.union(mr)

p.intersection(mr)