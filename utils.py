import os

def factorial(n):
  """
  Retorn n!.
  :param :n int.
  :return int fatorial de n.
  """
  f = 1
  until = int(n)+1
  for c in range(1, until):
    f*=c
  return f

def clear():
  """
  Limpa a tela do terminal
  """
  os.system('cls' if os.name == 'nt' else 'clear')

def banner():
  """
  Faz o cabeçalho do programa
  """
  f = open('logo.txt')
  logo = f.read()
  f.close
  
  print('\033[36m',logo,'\033[m')

def erro(error = 'Digite apenas números!\n'):
  """
  Escreve um erro na tela
  """
  print('\n\033[1;31m',error,'\033[m')

def eq_divs(a, b, c, tipo):
  """
  Calcula equações do primeiro grau que contenha divisão
  :param :a int
  :param :b int
  :param :c int
  :param :tipo str
  :return int|float
  """
  if tipo == 'a':
    result = int(b)*int(c)
  elif tipo == 'b':
    result = int(a)/int(c)
  elif tipo == 'c':
    result = int(a)/int(b)
  
  if(int(result) == result):
    result = int(result)
  
  return result;


def eq_mult(a, b, c, tipo):
  """
  Calcula equações do primeiro grau que contenha multiplicação
  :param :a int
  :param :b int
  :param :c int
  :param :tipo str
  :return int|float
  """
  if tipo == 'a':
    result = int(c)/int(b)
  elif tipo == 'b':
    result = int(c)/int(a)
  elif tipo == 'c':
    result = int(a)*int(b)
  
  if(int(result) == result):
    result = int(result)
  
  return result;

def eq_subt(a, b, c, tipo):
  """
  Calcula equações do primeiro grau que contenha subtração
  :param :a int
  :param :b int
  :param :c int
  :param :tipo str
  :return int
  """
  if tipo == 'a':
    result = int(b)+int(c)
  elif tipo == 'b':
    result = int(a)-int(c)
  elif tipo == 'c':
    result = int(a)-int(b)
  
  return result;

def eq_soma(a, b, c, tipo):
  """
  Calcula equações do primeiro grau que contenha soma
  :param :a int
  :param :b int
  :param :c int
  :param :tipo str
  :return :int
  """
  if tipo == 'a':
    result = int(c)-int(b)
  elif tipo == 'b':
    result = int(c)-int(a)
  elif tipo == 'c':
    result = int(a)+int(b)
  
  return result;


def eq_type(a, b, c):
  """
  Retorna onde esta a incógnita da equação
  :param :a str|int
  :param :b str|int
  :param :c str|int
  :return str
  """
  if (a.isdigit() and c.isdigit() and not b.isdigit()):
    return 'b'
  elif (a.isdigit() and b.isdigit() and not c.isdigit()):
    return 'c'
  elif (b.isdigit() and c.isdigit() and not a.isdigit()):
    return 'a'
  else: 
    return False
