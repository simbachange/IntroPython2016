Fruit = ['Apples','Pears','Oranges','Peaches']
print (Fruit)

print ('Enter the name of another fruit')
name = input()

Fruit.append(name)

print ('Give me a number if you dare!')
number = input()

print (Fruit [(int(number))])

Fruit.insert(0,'guava')

for i in Fruit:

    if Fruit[0][0] == 'p':
        print (Fruit[0][:])
    if Fruit[1][0] == 'p':
        print (Fruit[1])
    if Fruit[2][0] == 'P':
        print (Fruit[2][:])
    if Fruit[3][0] == 'p':
        print (Fruit[3][:])
    if Fruit [4][0] == 'P':
        print (Fruit[4][:])

        break
else:
    print (' ')

print (Fruit)

Fruit.pop()

print (Fruit)

print ('What Fruit would you like to delete')
print (Fruit)

remove = input()

Fruit.remove(remove)

print (Fruit)

print ('Do you like apples?')

for fruit in Fruit:
    print (fruit.lower())