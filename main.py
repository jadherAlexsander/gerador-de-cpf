import random, re

qntd_cpf = ''
qntd_cpf_int = 0

def gerar_cpf(reps):
  cpfs_gerados = []
  for i in range(reps):
    penultimo_digito = 0
    ultimo_digito = 0
    multiplicando_1 = 10
    multiplicando_2 = 11
    cpf_multiplicado_1 = 0
    cpf_multiplicado_2 = 0
    nove_digitos = ''
    dez_digitos = ''

    # Gera os nove primeiros digitos do CPF aleatoriamente
    for i in range(9):
      nove_digitos += str(random.randint(0, 9))
    # Itera sobre cada digito e os multiplica por um multiplicando(10) que diminui em 1 a cada iteração 
    # e logo em seguida multiplica o resultado da operação anterior por 10
    for digito in nove_digitos:
      cpf_multiplicado_1 += (int(digito) * multiplicando_1) * 10
      multiplicando_1 -= 1
    # Se o multiplicando chegar a 1 o penúltimo digito recebe o resto da divisão da multiplicação 
    # anterior por 11 e o loop é encerrado 
      if(multiplicando_1 < 2): penultimo_digito = cpf_multiplicado_1 % 11; break
    # Se o resto da divisão for menor ou igual a nove, o penultimo digito é ele mesmo, senão ele é 0
    penultimo_digito = penultimo_digito if penultimo_digito <= 9 else 0
    # A variável dez digitos recebe os nove primeiros digitos concatenados com o penultimo
    dez_digitos = f'{nove_digitos}{penultimo_digito}'
      # Itera sobre cada um dos dez digitos e os multiplica por um multiplicando(11) que diminui em 1 a
      # cada iteração e logo em seguida multiplica o resultado da operação anterior por 10
    for digito in dez_digitos:
      cpf_multiplicado_2 += (int(digito) * multiplicando_2) * 10
      multiplicando_2 -= 1
    # Se o multiplicando chegar a 1 o último digito recebe o resto da divisão da multiplicação 
    # anterior por 11 e o loop é encerrado 
      if(multiplicando_2 < 2): ultimo_digito = cpf_multiplicado_2 % 11; break
    ultimo_digito = ultimo_digito if ultimo_digito <= 9 else 0
    # Se o resto da divisão for menor ou igual a nove, o último digito é ele mesmo, senão ele é 0
    cpfs_gerados.append(f'{nove_digitos[:3]}.{nove_digitos[3:6]}.{nove_digitos[6:9:]}-{penultimo_digito}{ultimo_digito}')
    # Retorna um CPF válido para o usuário
  return cpfs_gerados
  
while True:
  qntd_cpf = input("Digite quantos CPF's quer que eu gere: ")

  try:
    qntd_cpf_int = int(qntd_cpf)
  except ValueError:
    print('Por favor apenas números.')
    continue
  except Exception:
    print('Erro desconhecido.')
    continue
  print(*gerar_cpf(qntd_cpf_int), sep = '\n')