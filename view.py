from models.cliente import Cliente, NCliente

class View:
  @classmethod
  def cliente_inserir(cls, nome, email, fone):
    cliente = Cliente(0, nome, email, fone)
    NCliente.inserir(cliente)
  @classmethod
  def cliente_listar(cls):
    return NCliente.listar()
  @classmethod
  def cliente_atualizar(cls, nome, email, fone):
    cliente = Cliente(0, nome, email, fone)
    NCliente.atualizar(cliente)
    
