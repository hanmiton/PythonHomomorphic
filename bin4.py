import sys
import math

def enc1(n1)
	return bin(n1)

def enc2(n2)
	return bin(n2)

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
    m1 = float(sys.argv[1])
    sys.stdout.write(str(enc1(m1)))
    m2 = float(sys.argv[1])
    sys.stdout.write(str(enc2(m2)))