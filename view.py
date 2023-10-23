from models.cliente import Cliente, NCliente
from models.servicos import Servico, NServico

class View:
  @classmethod
  def cliente_inserir(cls, nome, email, fone):
    cliente = Cliente(0, nome, email, fone)
    NCliente.inserir(cliente)
  @classmethod
  def cliente_listar(cls):
    return NCliente.listar()
  @classmethod
  def cliente_atualizar(cls, id, nome, email, fone):
    cliente = Cliente(id, nome, email, fone)
    NCliente.atualizar(cliente)
  @classmethod
  def cliente_excluir(cls, id):
    cliente = Cliente(id, "", "", "")
    NCliente.excluir(cliente)
  @classmethod
  def servico_inserir(cls, desc, valor, duracao):
    servico = Servico(0, desc, valor, duracao)
    NServico.inserir(servico)
  @classmethod
  def servico_listar(cls):
    return NServico.listar()

    