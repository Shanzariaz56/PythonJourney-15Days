"""l1=[1,2,3,4,5,6,6,7]
i=iter(l1)
print(next(i))"""

# iterator that print top 10 values
class values:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=20:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration
v= iter(values())
v1 = iter(values())
print(next(v))
print(next(v))
print(next(v))
print(next(v))
print(next(v))

for i in v1:
    print(i)
        