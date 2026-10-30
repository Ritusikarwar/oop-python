# class Customer:
#     def __init__(self,name):
#         self.name=name
# print("real class id:   ")
# cust=Customer("Julia")
# print(id(cust))

# def greet(customer):
#     print(id(customer))
# greet(cust)


class Customer:
    def __init__(self,name):
        self.name=name                    #<---------- Julia
print("real class id:   ")
cust=Customer("Julia")
print(id(cust))                          #<---------- Julia

def greet(customer):                     #<---------- Julia
    customer.name="Jessica"
    print(customer.name)
    print(id(customer))
greet(cust)                  #<----------- Julia enters the func but Jessica comes out.