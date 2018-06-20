#Q1


import math
class circle:
	
	
	def __init__(self,radius):
		self.radius=radius
	def getArea(self):
		area=math.pi*(self.radius**2)
		print(area)
		
	
	def getCircumference(self):
		crcm=2*(math.pi*self.radius)
		print(crcm)

c1= circle(7)
c1.getArea()


c2=circle(7)
c2.getCircumference()

#Q2



class Student:
	def __init__(self,name,roll):
		self.name=name
		self.roll=roll
	def info(self):
		print(self.name,self.roll)
name=input("enter your name=")	
roll=int(input("enter the roll number="))
	
s1=Student(name,roll)
s1.info()

#Q3



class temperature:
	def __init__(self,celsius,fahrenheit):
		self.celsius=celsius
		self.fahrenheit=fahrenheit
		
	def convertfahrenheit(self):
		fahrenheit=(celsius * 1.8) + 32
		print(fahrenheit)
		
	def convertcelcius(self):
		celsius=(fahrenheit - 32) / 1.8
		print(celsius)
		
celsius=int(input("enter temp in celcius="))
fahrenheit=int(input("enter temp in fahrenheit="))

s1=temperature(celsius,fahrenheit)
s1.convertfahrenheit()
s1.convertcelcius()

#Q4



class MovieDetails:
	def __init__(self,movname,artname,year,rating):
		self.movname=movname
		self.artname=artname
		self.year=year
		self.rating=rating
	print("")
		
	def display(self):
		print("movie=",self.movname)
		print("artist name=",self.artname)
		print("release year=",self.year)
		print("rating out of 5=",self.rating)
	print("")
	def update(self):
		self.movname=input("enter the new updated movie=")
		self.artname=input("enter the artist name=")
		self.year=(input("enter its release year="))
		self.rating=(input("enter the rating out of 5="))
		
movname=input(" movie=")
artname=input("artist name=")
year=(input("release year="))
rating=(input("rating out of 5="))		
s1=MovieDetails(movname,artname,year,rating)
s1.display()
s1.update()
s1.display()

#Q5


class Expenditure:
	def __init__(self,expenditure,savings):
		self.expenditure=expenditure
		self.savings=savings
	def display(self):
		print("expenditure:",self.expenditure)
		print("savings",self.savings)
	def totalsalary(self):
		salary=self.expenditure+self.savings
		print("total salary:",salary)

expenditure=int(input("enter your expenditure="))
savings=int(input("enter your savings="))
s1=Expenditure(expenditure,savings)
s1.display()
s1.totalsalary()
