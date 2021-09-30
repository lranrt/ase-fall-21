import lab1 as C

class FooCalculator:

    #empty constructor
    def __init__(self): #a constructor
        pass
    
    def sum(self, m, n): #self because in python it's necessary to pass the instance
        return c.sum(m,n)
    
    def divide(self, m, n):
        return c.divide(m,n)

calc1 = FooCalculator()
calc1.sum(3, 2)