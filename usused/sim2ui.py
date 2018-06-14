#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  simulation.py
#  
#  Copyright 2013 Corey McCarty <cmccarty@PhoenixFire>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from Simulation import *


def main():
	shapes=("wire","box","block","tube","rod","plates")
	image=0
	while not image in shapes:
		for w in shapes:
			print w
		try:
			image=raw_input("What simulation would you like to run today?")
		except ValueError:
			print 'Invalid Selection'
	if not image=='plates':
		args=('y','n','yes','no')
		temp=0
		while not temp=='y'or temp=='yes' or temp=='n' or temp=='no':	
			try:
				temp=raw_input('Should it be infinite? y/n')
			except ValueError:
				print 'Invalid Selection'
		if temp=='y' or temp=='yes':
			inf=1
		else:
			inf=0
	if image=='plates':
		s="Please enter the potential difference"
	elif inf==1:
		s="Please enter the linear charge density"
	else:
		s="Please enter the total charge on the object"
	mag=0
	while not mag:
		try:
			mag=float(raw_input(s))
		except ValueError:
			print 'Invalid Number'
	size=0
	while not size:
		try:
			size=int(raw_input("please enter a size for the simulation"))
		except ValueError:
			print"Invalid Number"
	p=0
	while not (p=='y'or p=='yes' or p=='n' or p=='no'):
		try:
			p=raw_input("would you like to see a picture?")
		except ValueError:
			print"Please enter y/n"
	if p=='y' or p=='yes':
		pic=1
	else:
		pic=0
	
	x=Simulation(inf,image,size,mag)
	if pic:
		x.render()

	else:
		i=int(raw_input("what is your x?"))
		j=int(raw_input("what is your y?"))
		k=int(raw_input("what is your z?"))
		l=x.interrogate(i,j,k,x.square)
		print "your field value is:"
		print l
	return 0

if __name__ == '__main__':
	main()

