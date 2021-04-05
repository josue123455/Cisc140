import ctypes
import random
import sys
import stdio
import stdarray



class DArray:
	def __init__(self):
		self.n = 0
		self.capacity = 100
		self.A = self.make_array(self.capacity)


	def __getitem__(self, k):

		if not 0 <= k <self.n:

			raise IndexError

		return self.A[k]

	def __setitem__(self, i, new):
		if self.n == 0:
			raise IndexError
		self.A[i] = new


	def addelem(self,x):
		if len(self.A) != self.n:
			value = x
			self.A[self.n] = value
			self.n += 1

		else:
			if self.n == self.capacity:
				self.make_array()
				self.A[self.n]= x
				self.n += 1
			CD = self.n + x
			i = 0
			for i in range (self.n):

				darray = stdaary.create1D(CD, None)
				darray[i] = self.A[i]
				i += 1
			self.A = darray

			value = x
			self.A[self.n] = value
			self.n += 1

	def __len__(self):
		return self.n

	def __str__(self):
		M = ""
		#result = "[" +M+ "]"
		for i in range(self.n):
			M = self.A[i]
		result = "[" +str(M)+ "]"

			#result += str(self.A[i])
			#result += repr(self.A[i])
		return result

	def make_array(self, new_cap):
		return (new_cap * ctypes.py_object)()







#c = DArray()
#c.addelem([1,3,4,5,6,7,8])
#
