class Customer:
    def __init__(self,name):
        self.name=name
print("real class id:   ")
cust=Customer("Julia")
print(id(cust))

def greet(customer):
    print(id(customer))
greet(cust)