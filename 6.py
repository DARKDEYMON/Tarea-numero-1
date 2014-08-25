#!/usr/bin/env python
# -*- coding: utf-8 -*-

def numeroLetrasNum(a):
	num=0
	let=0
	for x in range(1,len(a)):
		if(a[x].isdigit()):
			num=num+1
		if(a[x].isalpha()):
			let=let+1
	print("hay: "+str(num)+" numeros")
	print("hay: "+str(let)+" letras")
numeroLetrasNum("¡Hola amigos! 12345")