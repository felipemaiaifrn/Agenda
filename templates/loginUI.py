import streamlit as st
import pandas as pd
from views import View

class LoginUI:
  def main():
    st.header("Login")
    LoginUI.inserir()

  def inserir():
    email = st.text_input("Informe o e-mail")
    senha = st.text_input("Informe a senha")
    clientes = View.cliente_listar()

    if st.button("Fazer login"):
        x = View.Cliente_Login(email, senha)
        if x == True:
            st.success("Login realizado com sucesso")
        else:
            st.write("Usuário ou senha inválidos")