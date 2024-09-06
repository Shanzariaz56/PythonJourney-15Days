# exception chaining mean you may cal another error inside exception
# mean rasie error inside exception means chain error

class div:
    def __init__(self):
        pass
    def display(self,x,y):
        try:
            self.x=x
            self.y=y
            res=self.x/self.y
        except ZeroDivisionError as err:
            raise ValueError("not divisble by zero:")
        
d=div()
print(d.display(10,0))

# another example....
try:
    open("nofile.text")
except OSError:
    raise RuntimeError("unable to handle")
        