import sys
import math

def principal(m1,m2):
	m1 = bin(m1)
	m2 = bin(m2)
	return m1

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