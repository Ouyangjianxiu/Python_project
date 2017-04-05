# -*- coding: utf-8 -*-
import turtle  #移动并画东西
def draw_square():
	window = turtle.Screen() #为turtle创建一个背景  
	window.bgcolor("red")    #给背景设置一个颜色
	an = 0
	
	brad = turtle.Turtle() #使用这个函数 需要创建一个对象 这里就是brad  这里Turtle是模块turtle中的一个类
	brad.shape("turtle")   #可以定义形状 颜色 速度
	brad.speed(4)
	brad.color("yellow")
	while (an<72):	#循环化正方形 形成一个圆
		brad.forward(100)      #在乌龟的方向上 前进 移动特定的距离
		brad.right(90)       #右转一定角度
		brad.forward(100) 
		brad.right(90)
		brad.forward(100)
		brad.right(90)
		brad.forward(100)
		brad.right(90)
		an += 1
		
	
		brad.right(5)
		
	
	#angie = turtle.Turtle()#改变形状 颜色
	#angie.shape("arrow")
	#angie.color("blue")
	#angie.circle(100)
	
	#ca = turtle.Turtle()    #画三角
	#ca.shape("turtle")
	#ca.color("white")
	#ca.right(90)
	#ca.forward(100)
	#ca.right(120)
	#ca.forward(100)
	#ca.right(120)
	#ca.forward(100)
	#ca.right(120)
	
	
	window.exitonclick()  #任意键退出


#有关类
#当调用一个类的时候，类中的init函数也就是初始化函数 在内存中开辟一个空间给Turtle类的新的实例或者对象 这里对象(实例)
#实际上就是brad，这样brad就可以访问类中的所有方法
draw_square()