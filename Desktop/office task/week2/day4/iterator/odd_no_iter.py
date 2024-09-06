class old_num:
    def __init__(self,end_range):
        self.start=-1
        self.end_range=end_range
    def __iter__(self):
        return self
    def __next__(self):
        if self.start<self.end_range-1:
            self.start+=2
            return self.start
        else:
            raise StopIteration
        
o=old_num(20)
while True:
    try:
        num=next(o)
        print(num)
    except StopIteration:
        break
    
    
            