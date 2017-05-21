from numpy import*
import getopt,sys

#constant
h = 10e-9
#public variable
funcao = 0
x = 1
#end

class derivada(object):
	def __call__(self):
		y = x+h
		dfuncao = funcao.replace('x','y')
		return (eval(dfuncao) - eval(funcao))/h
	
opcao,valor = getopt.getopt(sys.argv[1:],'f:a: ')

for opcao,valor in opcao:
	if opcao == '-f':
		funcao = str(valor)
	if opcao == '-a':
		x = double(valor)

deriv = derivada()

print 'derivada de ',funcao,' = ',deriv()