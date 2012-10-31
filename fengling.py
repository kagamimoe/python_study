# usr/sbin/fengling.py
#coding:UTF-8
import random

class soul_item:
	color = ""
	property_type = ""
	propertynumber = 0
	
	def refresh(self):
		self.color = self.random_color()
		self.propertytype = self.random_propertytype()
		self.propertynumber = self.random_propertynumber(self.propertytype,self.color)	

	def random_color(self):
		a = random.random()
		if a<0.3:
			self_color = 'green'
		elif a<0.8:
			self_color = 'blue'
		elif a<0.95:
			self_color = 'purple'
		else:
			self_color = 'golden'
		return self_color

	def random_propertytype(self):
		a = random.randint(1,5)
		if a ==1:
			self_propertytype = 'hp'
		elif a == 2:
			self_propertytype = 'normal_atk'
		elif a == 3:
			self_propertytype = 'normal_def'
		elif a == 4:
			self_propertytype = 'magic_atf'
		else :
			self_propertytype = 'magic_def'
		return self_propertytype

	def random_propertynumber(self,self_propertytype,self_color):
		if self_propertytype == 'hp':
			mina = 10
			maxa = 35
		else:
			mina = 20
			maxa = 120
		#print mina
		#print maxa
		if self_color == 'green':
			self_propertynumber = random.randint(mina,mina+(maxa-mina)*0.2-1)
		elif self_color == 'blue':
			self_propertynumber = random.randint(mina+(maxa-mina)*0.2,mina+(maxa-mina)*0.8-1)
		elif self_color == 'purple':
			self_propertynumber = random.randint(mina+(maxa-mina)*0.8,maxa-1)
		elif self_color == 'golden':
			self_propertynumber = maxa
		if self_propertytype == 'hp':
			return self_propertynumber*100
		else:
			return self_propertynumber*5


	def show(self):
		print 'now soul_item\'s property is:'
		print 'color:' + self.color
		print 'property_type:' + self.propertytype
		print 'propertynumber:' + str(self.propertynumber)
		

new_soul_item = soul_item()
new_soul_item.refresh()
new_soul_item.show()

while True:
	flag = raw_input("Do you want to refresh it? y/n")
	print flag
	if flag == "y":
		new_soul_item.refresh()
		new_soul_item.show()
	else: 
		print 'ok,it\'s over'
		break