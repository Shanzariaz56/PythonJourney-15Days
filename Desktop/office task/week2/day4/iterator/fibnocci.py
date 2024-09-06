class fib:
    def __init__(self,max):
        self.max=max
        self.count=0
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def __next__(self):
        if self.count>=self.max:
            raise StopIteration
        fib_val=self.a
        self.a,self.b=self.b,self.a+self.b
        self.count+=1
        return fib_val
    
f=fib(20)
for i in f:
    print(i)
        