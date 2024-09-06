# simple generator....
def value():
    yield 5
v=value()
print(v)

# use of generator function
def count_value(max_value):
    current=1
    while current<=max_value:
        yield current
        current+=1
c=count_value(10)
for i in c:
    print(i)