#protected use single _
'''
class abc:
    def __init__(self,name,age):
        self._name1=name
        self._age1=age
a=abc("Sarika","11")
print(a._name1)
print(a._age1)
a._age1=34
print(a._age1)
'''

#private uses double __
'''
class abc:
    def __init__(self,name,age):
        self.__name1=name
        self._age1=age
a=abc("Sarika","11")
print(a._age1)
print(a.__name1)

a._age1=34
print(a._age1)'''

#public
'''
class abc:
    def __init__(self,name,age):
        self.name1=name
        self.age1=age
    def display(self):
        print("name is :{} and age is : {} ".format(self.name1,self.age1))
        
a=abc("Sarika","11")
print("name is "+ a.name1)
print ("age is "+a.age1)
a.display()

'''
#protected
'''
class abc:
    def __init__(self,name,age):
        self._name1=name
        self._age1=age
    def display(self):
        print("name is :{} and age is : {} ".format(self._name1,self._age1))
        
a=abc("Sarika","11")
print("name is "+ a._name1)
print ("age is "+a._age1)
a.display()

'''
# private
'''
class abc:
    def __init__(self,name,age):
        self.__name1=name
        self.__age1=age
    def display(self):
        print("name is :{} and age is : {} ".format(self.__name1,self.__age1))
        
a=abc("Sarika","11")
print("name is "+ a.__name1)
print ("age is "+a.__age1)
a.display()
'''

#inheritance

'''class room:
    def student(self,name ,id):
        print("Student name : {} and id is : {}".format(name,id))
class report(room):
    def result(self,marks):
        print("marks is {}".format(marks))

r=report()
r.result(34)
r.student("sarika",23)

'''

#encapsulation
class abc:
    def __init__(self):
        self.__value=200
    def car(self):
        print("value is {}".format(self.__value))
    def setmax(self,price):
        self.__value=price
        
ab=abc()
ab.car()
ab.setmax(400)
ab.car()















































