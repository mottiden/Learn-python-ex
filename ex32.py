hairs = ['brown', 'blond', 'red']
eyes = ['brown', 'blue', 'green']

the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

for number in the_count:
    print "This is count %r" % number

for fruit in fruits:
    print "A fruit can be: %r" % fruit

for i in change:
    print"I got %r change" % i

elements = []

for i in range(0, 6):
    print "Adding %d to the list." % i
    elements.append(i)

for i in elements:
    print "Element contains: %d" % i
