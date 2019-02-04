#program to write a class function for ip addressess and their subnet masks
from random import getrandbits
import ipaddress

class ipaddressess():

	def __init__(self,a,b):
		self.a=ipaddress.IPv4Address(a)
		self.b=b

	def __str__(self):
		print ("ipadress is :" ,self.a)
		print("subnetmask is:" ,self.b)
		return

a=getrandbits(32)
c=ipaddressess(a,32)
print(c)
