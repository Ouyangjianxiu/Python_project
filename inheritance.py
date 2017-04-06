# -*- coding: utf-8 -*-
class Parent():
	def __init__(self, last_name, eye_color):
		print ("Parent Constructor Called")
		self.last_name = last_name
		self.eye_color = eye_color
		
	def show_info(self):
		print("Last Name - "+self.last_name)
		print("Eye Color - "+self.eye_color)
		
		
class Child(Parent):
	def __init__(self, last_name, eye_color, number_of_toys):
		print ("Child Constructor Called")
		Parent.__init__(self, last_name, eye_color)
		self.number_of_toys = number_of_toys
		
	def show_info(self):
		print("Last Name - "+self.last_name)
		print("Eye Color - "+self.eye_color)
		print("Number of toys - "+str(self.number_of_toys)) #为了能打印出来 将其封装在串函数中
		
		
		
billy_cyrus = Parent("Cyrus", "blue")
#print (billy_cyrus.last_name)
billy_cyrus.show_info()

milly_cyrus = Child("Cyrus", "blue", 5)
#print (milly_cyrus.last_name)
#print (milly_cyrus.number_of_toys)
milly_cyrus.show_info()   #当自己的类中有这个函数的时候就调用自己的函数 也就是覆盖了从Parent类中的继承