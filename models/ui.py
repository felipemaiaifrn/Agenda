from cliente import Cliente, NCliente
from servicos import Servico, NServico


class UI:
  @classmethod
  def Main(cls):
    op = 99
    while(op != 0):
      op = UI.Menu()
      if op == 1: UI.ClienteInserir()
      if op == 2: UI.ClienteListar()
      if op == 3: UI.ClienteAtualizar()
      if op == 4: UI.ClienteExcluir()
      if op == 5: UI.ServicoInserir()
      if op == 6: UI.ServicoListar()
      if op == 7: UI.ServicoAtualizar()
      if op == 8: UI.ServicoExcluir()    
        
  @classmethod
  def Menu(cls):
    print("\nClientes: ")
    print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir")
    print("\nServiços: ")
    print("5-Inserir, 6-Listar, 7-Atualizar, 8-Excluir")
    print("\n0 - Sair")
    return int(input())
  
  @classmethod
  def ClienteInserir(cls):
    # id = int(input("Id: "))
    nome = input("Nome: ")
    email = input("E-mail: ")
    fone = input("fone: ")
    cliente = Cliente(0, nome, email, fone)
    NCliente.inserir(cliente)
    
  @classmethod
  def ClienteListar(cls):
    for cliente in NCliente.listar():
      print(cliente)
      
  @classmethod
  def ClienteAtualizar(cls):
    UI.ClienteListar()
    id = int(input("Id do cliente a ser atualizado: "))
    nome = input("Novo nome: ")
    email = input("Novo e-mail: ")
    fone = input("Novo fone: ")
    cliente = Cliente(id, nome, email, fone)
    NCliente.atualizar(cliente)   
    
  @classmethod
  def ClienteExcluir(cls):
    UI.ClienteListar()
    id = int(input("Id do cliente a ser excluído: "))
    cliente = Cliente(id, "", "", "")
    NCliente.excluir(cliente)

  @classmethod
  def ServicoInserir(cls):
    # id = int(input("Id: "))
    desc = input("Descrição: ")
    valor = input("Valor (R$): ")
    duracao = input("Duração (min): ")
    servico = Servico(0, desc, valor, duracao)
    NServico.inserir(servico)
    
  @classmethod
  def ServicoListar(cls):
    for servico in NServico.listar():
      print(servico)
      
  @classmethod
  def ServicoAtualizar(cls):
    UI.ServicoListar()
    id = int(input("Id do serviço a ser atualizado: "))
    desc = input("Nova Descrição: ")
    valor = input("Novo Valor (R$): ")
    duracao = input("Nova Duração (min): ")
    servico = Servico(id, desc, valor, duracao)
    NServico.atualizar(servico)  
    
  @classmethod
  def ServicoExcluir(cls):
    UI.ServicoListar()
    id = int(input("Id do serviço a ser excluído: "))
    servico = Servico(id, "", "", "")
    NServico.excluir(servico)

UI.Main()
