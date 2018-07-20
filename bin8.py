import sys
import math
import random

def principal(m1,m2):
	LAMBDA = 16 #security parameter
	N = LAMBDA	
	P = LAMBDA ** 2
	Q = LAMBDA ** 5
	m1 = bin(m1)
	m2 = bin(m2)
	return m2

def keygen(n):
	key = random.getrandbits(P)
	while(key % 2 == 0):
		key = random.getrandbits(P)
	return key

def encrypt(key, aBit):
	q = random.getrandbits(Q)
	m_a = 2 * random.getrandbits(N - 1)
	c = key * q + m_a + aBit
	return c

def decrypt(key, cipherText):
	return mod(cipherText, key) % 2

def add(cipherText1, cipherText2):
	return cipherText1 + cipherText2

def mult(cipherText1, cipherText2):
	return cipherText1 * cipherText2

def bin(numero):
	binario = ""
	listaN = []
	listaRn = []
	if (numero >0):
		while (numero >0):
			if(numero%2 ==0):
				listaN.append(0)
				binario="0"+binario
			else:
				listaN.append(1)
				binario = "1"+ binario
			numero = int (math.floor(numero/2))
	else:
		if (numero ==0):
			listaN.append(0)
			return listaN
		else:
			return " no se pudo convertir el numero. ingrese solo numeros positivos"	
	for i in reversed(listaN):
		listaRn.append(i)
	return listaRn

if __name__ == '__main__':
	principal(m1,m2)