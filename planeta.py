#_*_ coding: utf-8 _*_
#!/usr/bin/env python

import numpy as np

class planeta(object):
	def __init__(self,nome,massa,x = 0,y = 0):
		self.n = nome
		self.m = massa
		self.x = x
		self.y = y
	def __sub__(self,oth):
		return np.sqrt((self.x - oth.getX())**2+(self.y - oth.getY())**2)
	def __str__(self):
		return '(%g,%g)'%(self.x,self.y)
	#setters
	def setNome(self,nome):
		self.n = nome
	def setMassa(self,massa):
		self.m = massa
	def setX(self,x):
		self.x = x
	def setY(self,y):
		self.y = y
	#getters
	def getNome(self):
		return self.n
	def getMassa(self):
		return self.m
	def getX(self):
		return self.x
	def getY(self):
		return self.y
	#method
	def distancia(self):
		return np.sqrt(self.x**2+self.y**2)
	def forca_g(self):
		return (6.67e-11*self.m*1.99e30)/(self.distancia())**2
	def periodo(self):
		#T^2 = (4π^2/GM)r^3
		return np.sqrt((4*np.pi**2 * (np.sqrt(self.x**2+self.y**2))**3)/(6.67e-11*1.99e30))/31557600
	def detail(self):
		return [self.n,self.m,self.x,self.y]
#end class

Terra = planeta('Terra',5.98e24,1.5e11*np.cos(np.pi/4),1.5e11*np.sin(np.pi/4))
Marte = planeta('Marte',6.42e23,2.28e11*np.cos(np.pi/4),2.28e11*np.sin(np.pi/4))

print 'pos: ',Terra,Marte
print 'detalhes: ',Terra.detail(),Marte.detail()
print 'Periodo da Terra: ',Terra.periodo(),"anos"
print 'Periodo de Marte: ',Marte.periodo(),"anos"
print 'distancia Terra-Marte: ',Terra - Marte,"m"
 




