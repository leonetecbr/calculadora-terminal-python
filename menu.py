import utils, math, re

def start(error = ''):
  """
  Inicia o programa e lista as opções
  :param :error str
  """
  utils.clear()
  utils.banner()
  
  functions = ['Fatorial', 'Raiz Quadrada', 'Soma', 'Equação do primeiro grau']
  
  print('O que você quer calcular ?\n\n')
  
  i = 1
  for fun in functions:
    print(f'   [\033[32m{i}\033[m] {fun}')
    i += 1
  
  print('\n\n   [\033[31m0\033[m] Sair')
  
  if not error == '':
    utils.erro(error)
    error = ''
  
  c = input('\n  > ')
  
  if c.isdigit():
    c = int(c)
  else:
    start('Digite um número!')
    return True
  
  utils.clear()
  utils.banner()
  print('\n')
  
  operations(c)
  
  cont = input('\nDeseja continuar ? (s/n) ')
  
  if cont == 's' or cont == 'S':
    start()
  else:
    utils.clear()
    exit()

def operations(c):
  """
  Direciona o usuário para a função desejada
  :param :c int
  """
  if c == 1:
    n = input('Digite o número para fatorar: ')
    
    if n.isdigit():
      n = int(n)
    else:
      utils.erro()
      operations(c)
      return True
    
    fat = utils.factorial(n)
    print(f'\nO fatorial de \033[1;32m{n}\033[m é \033[1;32m{fat}\033[m. \033[1;34m{n}! = {fat}\033[m\n')
  elif c==2:
    n = input('Digite um número para obter sua raiz quadrada: ')
    
    if n.isdigit():
      n = int(n)
    else:
      utils.erro()
      operations(c)
      return True
    
    sqrt = math.sqrt(n)
    if sqrt == int(sqrt):
      sqrt = int(sqrt)
      print(f'\nA raiz quadrada de \033[1;32m{n}\033[m é \033[1;32m{i}\033[m. \033[1;34m√{n} = {sqrt}\033[m')
    else:
      print(f'\nA raiz quadrada de \033[1;32m{n}\033[m é \033[1;32m{sqrt}\033[m. \033[1;34m√{n} = {sqrt}...\033[m')
  elif c==3:
    n1 = input('Digite o primeiro número a ser somado: ')
    
    if n1.isdigit():
      n1 = int(n1)
    else:
      utils.clear()
      utils.banner()
      utils.erro()
      operations(c)
      return True

    n2 = input('\nDigite o segundo número a ser somado: ')
    
    if n2.isdigit():
      n2 = int(n2)
    else:
      utils.clear()
      utils.banner()
      utils.erro()
      operations(c)
      return True
    
    soma = n1+n2
    print(f'\nA soma entre \033[1;32m{n1}\033[m e \033[1;32m{n2}\033[m é igual a \033[1;32m{soma}\033[m. \033[1;34m{n1} + {n2} = {soma}\033[m')
  elif (c==4):
    eq = input('Digite a equação simplificada: ').strip()
    
    matches = re.match('^(\w+?) ?(\+|\-|\*?|\/) ?(\w+) ?= ?(\w+)$', eq)

    if matches == None:
      utils.erro('Digite a equação no formato "x + 5 = 9"\n')
      operations(c)
      return True
    
    a = matches.group(1)
    op = matches.group(2)
    b = matches.group(3)
    c = matches.group(4)
    
    if op == '' and not b.isdigit():
      op = '*'
    
    tipo = utils.eq_type(a, b, c)
    
    if tipo == False:
      utils.erro('Digite a equação no formato "x + 5 = 9"\n')
      operations(c)
      return True
    
    if op == '+':
      result = utils.eq_soma(a, b, c, tipo)
    elif op == '-':
      result = utils.eq_subt(a, b, c, tipo)
    elif op == '*':
      result = utils.eq_mult(a, b, c, tipo)
    else:
      result = utils.eq_divs(a, b, c, tipo)
      
      
    if tipo == 'a':
      i = a
    elif tipo == 'b':
      i = b
    else:
      i = c
    
    print(f'Na equação \033[1;32m{a} {op} {b} = {c}\033[m, \033[1;32m{i}\033[m é igual a \033[1;32m{result}\033[m.\n\033[1;34m{a} {op} {b} = {c}\nx = {result}\033[m');

  elif c==0:
    utils.clear()
    exit()
  else:
    start()
