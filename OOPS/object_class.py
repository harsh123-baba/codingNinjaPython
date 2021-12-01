class Vehicle:
    def __init__(self, name):
        self.__name = name;
    def __str__(self):
        # by deafault this str function gives us print(object_name) output as memory address of object 
        return "This is vehicle class i am reintialized before that i have the value of object address"

v = Vehicle('sokda')    
print(v)