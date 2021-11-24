Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def add1():
    a=5
    b=10
    print(a+b)
add1()
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> def add():
	a=5
	b=5
	print(a+b)

	
>>> add()
10
>>> def name(fname):
	print(fname+" sarika")

	
>>> name("alka")
alka sarika
>>> name("nakul")
nakul sarika
>>> def arg(*case):
	print("case is "+ case[2])

	
>>> arg("one","two","three","four","five","six")
case is three
>>> def key(name5,name1,name2,name3,name4):
	print("name is "+ name2)

	
>>> key(name4="sarika",name2="alka",name1="nakul",name3="parul",name5="nandini")
name is alka
>>> key("A","B","C","D","E")
name is C
>>> def key1(**name):
	print("name is "+key["name2"])

	
>>> key1(name1="sarika",name2="alka",name3="nandini",name4="nakul")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    key1(name1="sarika",name2="alka",name3="nandini",name4="nakul")
  File "<pyshell#26>", line 2, in key1
    print("name is "+key["name2"])
TypeError: 'function' object is not subscriptable
>>> def key1(**name):
	print("name is "+key1["name2"])

	
>>> key1(name1="sarika",name2="alka",name3="nandini",name4="nakul")
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    key1(name1="sarika",name2="alka",name3="nandini",name4="nakul")
  File "<pyshell#29>", line 2, in key1
    print("name is "+key1["name2"])
TypeError: 'function' object is not subscriptable
>>>  def key1(**name):
	print("name is "+key1["name2"])
	
SyntaxError: unexpected indent
>>> >>> key1(name1="sarika",name2="alka",name3="nandini",name4="nakul")

SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def key5(**name):
	print("name is " + name["lname"])

	
>>> key5(fname="jhon", lname="robert")
name is robert
>>> def default(name="sarika"):
	print("Name is "+name)

	
>>> default()
Name is sarika
>>> default("alka")
Name is alka
>>> def abc(food):
	print(food)
fruit=["apple","banana","orange"]
SyntaxError: invalid syntax
>>> 
>>> def abc(food):
	print(food)
    fruit=["apple","banana","orange"]

SyntaxError: unindent does not match any outer indentation level
>>> def abc(food):
	print(food)

	
>>>     fruit=["apple","banana","orange"]

SyntaxError: unexpected indent
>>> fruit=["apple","mango","orange"]
>>> abc(fruit)
['apple', 'mango', 'orange']
>>> for x in food:
	print(x)

	
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    for x in food:
NameError: name 'food' is not defined

>>> def abc(food):
	print(food)
	for v in food:
		print(v)

		
>>> fruit=["apple","mango","orange"]
>>> abc(fruit)
['apple', 'mango', 'orange']
apple
mango
orange
>>> def tri(k):
	if(k>0):
		print(k+tri(k-1))
	else:
		print("zero")

		
>>> tri(6)
zero
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    tri(6)
  File "<pyshell#76>", line 3, in tri
    print(k+tri(k-1))
  File "<pyshell#76>", line 3, in tri
    print(k+tri(k-1))
  File "<pyshell#76>", line 3, in tri
    print(k+tri(k-1))
  [Previous line repeated 3 more times]
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
>>> def tri(k):
	if(k>0):
		result=k+tri(k-1)
		print(result)
	else:
		print("zero")

		
>>> tri(6)
zero
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    tri(6)
  File "<pyshell#79>", line 3, in tri
    result=k+tri(k-1)
  File "<pyshell#79>", line 3, in tri
    result=k+tri(k-1)
  File "<pyshell#79>", line 3, in tri
    result=k+tri(k-1)
  [Previous line repeated 3 more times]
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
>>> 
>>> 
>>> 
>>> 
>>> def tri(k):
	if(k>0):
		result=k+tri(k-1)
		print(result)
	else:
		print("zero")
	return result

>>> tri(6)
zero
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    tri(6)
  File "<pyshell#87>", line 3, in tri
    result=k+tri(k-1)
  File "<pyshell#87>", line 3, in tri
    result=k+tri(k-1)
  File "<pyshell#87>", line 3, in tri
    result=k+tri(k-1)
  [Previous line repeated 3 more times]
  File "<pyshell#87>", line 7, in tri
    return result
UnboundLocalError: local variable 'result' referenced before assignment
>>> def tri(k):
	if(k>0):
		result=k+tri(k-1)
		print(result)
	else:
		return = 0
	return result
SyntaxError: invalid syntax
>>> def tri(k):
	if(k>0):
		result=k+tri(k-1)
		print(result)
	else:
		result = 0
	return result

>>> tri(6)
1
3
6
10
15
21
21
>>> 
